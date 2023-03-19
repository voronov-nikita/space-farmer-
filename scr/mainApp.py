import os
from flask import Flask, render_template

import main_function

app = Flask(__name__)

points = main_function.get_new_flight_assigment()

days = [i for i in range(1, 8)]
rem_res = [(0, 0)] * len(days)
spent_res = [(0, 0)] * len(days)
react = [(0, 0)] * len(days)
auto = [(0, 0)] * len(days)
sh = [0] * len(days)
money = 0

@app.route('/')
def hello():
    return render_template('index.html', days=days, rem_res=rem_res, spent_res=spent_res,
                           react=react, auto=auto, sh=sh, length=len(days), money=money)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)