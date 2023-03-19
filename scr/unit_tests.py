import mainapp

def check_mass(result):
    if mainapp.massa() == result:
        return "The test is Completed!"
    return "Test Failed!"


def check_energy(result, *args):
    if mainapp.energy(*args) == result:
        return "The test is Completed!"
    return "Test Failed!"


def check_connect():
    if mainapp.get_new_flight_assigment():
        return "The test is Completed!"
    return "Test Failed!"

def check_K(result, *args):
    if round(mainapp.coeficent_K(*args), 1)==result:
        return "The test is Completed!"
    return "Test Failed!"

# <----------------------- Вызов проверки ----------------------->
print()
print(check_mass([696, 5800, 199]))
print(check_energy(36, 8))
print(check_connect())
print(check_K(-0.5, 8, 10))
print()
