from flask import Flask, render_template, url_for, request, flash
from joblib import load
from traffic import Traffic

app = Flask(__name__)

model = load('model_traffic.joblib')

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        age = request.form["age"]
        gender = request.form["gender"]
        driverexp = request.form["driverexp"]
        weather = request.form["weather"]
        
        if (age == "0" or gender == "0" or driverexp == "0" or weather == "0"):
            flash(validationMessage(age, gender, driverexp, weather), "danger")
            return render_template("index.html")
            
        
        y_pred = Traffic.severityArray(age, gender, driverexp, weather)
        
        severityPrediction = model.predict(y_pred)
        
        if severityPrediction == 1:
            flash("slightly Injury", "success")
        elif severityPrediction == 2:
            flash("Serious Injury", "warning")
        elif severityPrediction == 3:
            flash("Fatal Injury", "danger")
        else:
            return "Unknowm"
        
    return render_template("index.html")

@app.route('/tes')
def method_name():
    return str(Traffic.severityArray("1","1","1","1"))

@app.route('/load')
def loadmodel():
    """tes model secara langsung

    Returns:
        string: severity level, 1 = slightly injury, 2 = serious injury, 3 = fatal injury
    """
    
    # input: under 18, female, no license, raining and windy
    return str(model.predict([[
            0, 0, 0, 1,
            0,1,
            0,0,0,0,0,1,
            0,1,0,0,0,0,0,0
            ]]))
    
def validationMessage(inputAge, inputGender, inputExp, inputWeather):
    message = "Input Not Valid"
    if (inputAge == "0"):
        message = "Choose Driver Age"
    elif (inputGender == "0"):
        message = "Choose Driver Gender"
    elif (inputExp == "0"):
        message = "Choose Driver Experience"
    elif (inputWeather == "0"):
        message = "Choose Weather Condition"

    return message

if __name__ == '__main__':
    app.secret_key = 'uniks3cr3tk3y'
    app.run(debug=True)
