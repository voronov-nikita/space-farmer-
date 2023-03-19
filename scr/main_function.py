from requests import get
from json import loads
import numpy as np
import sqlite3 as sql
from random import randint

gg = randint
# <------------------ Создание простой Базы данных --------------->
db = sql.connect("information.db")
cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS info(
    number_id INTEGER,
    count_day INTEGER,
    remain_resources INTEGER,
    now_resource INTEGER,
    power_reactor FLOAT,
    len_population INTEGER,
    autotoclava TEXT
)
""")
db.commit()

# <------------ Обьявление функций -------------->

# вычисление стоимости в кредитах
class PriceInfo():
    def __init__(self, count_oxygen, count_fuel):
        # стоимость кислорода по количеству(должно быть четным!)
        self.oxygen = 14*(count_oxygen//2)
        # стоимость единиц топлива по количетву 
        self.fuel = (14 * (10//2)) * count_fuel


def get_new_flight_assigment(url="https://dt.miet.ru/ppo_it_final"):
    token = "46u76vrf"
    sait = get(url, headers={'X-Auth-Token': token})
    return dict(loads(sait.text))["message"]


def speeds(w, m):
    return 2 * (w/80) * (200/m)


def energy(T):
    return sum([i for i in range(0, T+1)])


def len_new_population_G(g1, g2, K):
    return g1 + g2 * K


def coeficent_K(T, Oxi):
    p = np.pi
    d = np.sin((-p / 2) + (p * (T + 0.5 * Oxi) / 40))
    return d


def massa():
    m = []
    for i in range(len(get_new_flight_assigment())):
        mm = 192
        for ii in range(len(get_new_flight_assigment()[i]['points'])):
            mm += get_new_flight_assigment()[i]['points'][ii]['SH']
        m.append(mm)
    return m

def count_SH():
    otv=8
    for i in get_new_flight_assigment():
        otv+=i['points'][0]["SH"]
    return otv


#количество единиц sh выгружаемых в точке
def shintochka(n):
    return (8 * 2 ** n) - 8


def from_bd():
    with open("information.db", 'r') as file:
        for i in file:
            print(i)


# <------------ Основной алгоритм программы -------------->

for i in range(len(get_new_flight_assigment())):
    cursor.execute(f"""INSERT INTO info(number_id, count_day, remain_resources, now_resource, power_reactor, len_population, autotoclava) 
            VALUES({i}, {10*i}, {0},{0}, {gg(1, 10+1)/10}, {count_SH()-get_new_flight_assigment()[0]['points'][0]["SH"]}, "{gg(0, 30), 60*count_SH()}");
        """)
    db.commit()

