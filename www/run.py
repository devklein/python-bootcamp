from flask import Flask, render_template, request

app = Flask(__name__)

class Fruits():
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
      

@app.route("/")

def start():
    items = [
        Fruits("Apfel", 5),
        Fruits("Birne", 3),
        Fruits("Banane", 8)
        ]
    # same with a dictionary instead of an objects from class Fruits
    items = [
       {"name": "Apfel", "amount": 5},
       {"name": "Birne", "amount": 3},
       {"name": "Banane", "amount": 8}
       ]

    person = ("Max", "Mustermann")
        
    return render_template("start.html", person=person, fruits=items)


@app.route("/test")

def test():
    name = request.args.get("name")
    age = request.args.get("age")
    return render_template("test.html", name=name, age=age)


@app.route("/currency")

def currency():
    currency1 = request.args.get("currency1")
    currency2 = request.args.get("currency2")
    rate = request.args.get("rate")

    

    qty = [1, 5, 10, 50, 100, 200, 500, 1000]
    result = {}

    if currency1 != None or currency2 != None or rate != None:
        rate_float = float(rate.replace(",", "."))
        for item in qty:
            result[item] = round(item * rate_float, 2)


    return render_template("currency.html", currency1=currency1, currency2=currency2, rate=rate, result=result)