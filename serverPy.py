import os
from flask import Flask, request, render_template

app = Flask(__name__)

#constants
FEET_CONVERSION = 12
FORMULA_CONSTANT = 703

@app.route("/", methods = ["GET", "POST"])
def BMICalculations():
    if request.method == "POST":
        Feet = int(request.form.get("Feet"))
        Inches = int(request.form.get("Inches"))
        Pounds = float(request.form.get("Pounds"))

        total = BMICalculatorFun(Feet, Inches, Pounds)
        stringResults = StringDeterminedResults(total)

        return render_template("BMI_home.html", result = total, categoryResult = stringResults) 
    # when you are returning these variables they need to be established in the html first 
    else:
        return render_template("BMI_home.html")

# function used in order to calculate BMI
def BMICalculatorFun(feet, inches, pounds):
    feet_converted = ((feet * FEET_CONVERSION) + inches)
    pre = (pounds*FORMULA_CONSTANT) / feet_converted
    return float(format((pre / feet_converted), ".1f"))

def StringDeterminedResults(calculatedTotal):

    if(calculatedTotal < 18.5):
        return "Underweight"
    elif(calculatedTotal >= 18.5 and calculatedTotal <= 24.9):
        return "Healthy"
    elif(calculatedTotal >= 25.0 and calculatedTotal <= 29.9):
        return "Overweight"
    return "Obesity"

if __name__=="__main__":
    app.run(host="0.0.0.0")