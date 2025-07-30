import os
from flask import Flask, request, render_template

app = Flask(__name__)

FEET_CONVERSION = 12
FORMULA_CONSTANT = 703

@app.route("/", methods = ["GET", "POST"])
def BMICalculations():
    if request.method == "POST":
        Feet = int(request.form.get("Feet"))
        Inches = int(request.form.get("Inches"))
        Pounds = float(request.form.get("Pounds"))

        result = BMICalculator(Feet, Inches, Pounds)
        return render_template("BMI_home.html", result = result)
    else:
        return render_template("BMI_home.html")


def BMICalculator(feet, inches, pounds):
    return format(FORMULA_CONSTANT * (pounds / ((feet * FEET_CONVERSION) + inches)), ".2f")

if __name__=="__main__":
    app.run(host="0.0.0.0")