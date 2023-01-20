from flask import Flask, render_template, url_for, request, flash
from joblib import load

app = Flask(__name__)

model = load('model_traffic.joblib')

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        age = request.form["age"]
        gender = request.form["gender"]
        driverexp = request.form["driverexp"]
        weather = request.form["weather"]
        
        if (age == "1"):
            ageEighteenToThirty = 1
            ageThirtyOneToFifty= 0
            ageOverFifthyOne = 0
            ageUnderEighteen = 0
        elif (age == "2"):
            ageEighteenToThirty = 0
            ageThirtyOneToFifty= 1
            ageOverFifthyOne = 0
            ageUnderEighteen = 0
        elif (age == "3"):
            ageEighteenToThirty = 0
            ageThirtyOneToFifty= 0
            ageOverFifthyOne = 1
            ageUnderEighteen = 0
        elif (age == "4"):
            ageEighteenToThirty = 0
            ageThirtyOneToFifty= 0
            ageOverFifthyOne = 0
            ageUnderEighteen = 1
            
        if (gender == "1"):
            male = 1
            female = 0
        else:
            male = 0
            female = 1
        
        if (driverexp == "1"):
            driverExpOneToTwoYear = 1
            driverExpTwoToFiveYear = 0
            driverExpFiveToTenYear = 0
            driverExpAboveTenYear = 0
            driverExpBelowOneYear = 0
            driverExpNoLicense = 0
        elif (driverexp == "2"):
            driverExpOneToTwoYear = 0
            driverExpTwoToFiveYear = 1
            driverExpFiveToTenYear = 0
            driverExpAboveTenYear = 0
            driverExpBelowOneYear = 0
            driverExpNoLicense = 0
        elif (driverexp == "3"):
            driverExpOneToTwoYear = 0
            driverExpTwoToFiveYear = 0
            driverExpFiveToTenYear = 3
            driverExpAboveTenYear = 0
            driverExpBelowOneYear = 0
            driverExpNoLicense = 0
        elif (driverexp == "4"):
            driverExpOneToTwoYear = 0
            driverExpTwoToFiveYear = 0
            driverExpFiveToTenYear = 0
            driverExpAboveTenYear = 1
            driverExpBelowOneYear = 0
            driverExpNoLicense = 0
        elif (driverexp == "5"):
            driverExpOneToTwoYear = 0
            driverExpTwoToFiveYear = 0
            driverExpFiveToTenYear = 0
            driverExpAboveTenYear = 0
            driverExpBelowOneYear = 1
            driverExpNoLicense = 0
        elif (driverexp == "6"):
            driverExpOneToTwoYear = 0
            driverExpTwoToFiveYear = 0
            driverExpFiveToTenYear = 0
            driverExpAboveTenYear = 0
            driverExpBelowOneYear = 0
            driverExpNoLicense = 1
        
        
        if (weather == "1"):
            weatherCloudy = 1
            weatherForOrMist = 0
            weatherNormal = 0
            weatherOther = 0
            weatherRaining = 0
            weatherRainingAndWindy = 0
            weatherSnow = 0
            weatherWindy = 0
        elif (weather == "2"):
            weatherCloudy = 0
            weatherForOrMist = 1
            weatherNormal = 0
            weatherOther = 0
            weatherRaining = 0
            weatherRainingAndWindy = 0
            weatherSnow = 0
            weatherWindy = 0
        elif (weather == "3"):
            weatherCloudy = 0
            weatherForOrMist = 0
            weatherNormal = 1
            weatherOther = 0
            weatherRaining = 0
            weatherRainingAndWindy = 0
            weatherSnow = 0
            weatherWindy = 0
        elif (weather == "4"):
            weatherCloudy = 0
            weatherForOrMist = 0
            weatherNormal = 0
            weatherOther = 1
            weatherRaining = 0
            weatherRainingAndWindy = 0
            weatherSnow = 0
            weatherWindy = 0
        elif (weather == "5"):
            weatherCloudy = 0
            weatherForOrMist = 0
            weatherNormal = 0
            weatherOther = 0
            weatherRaining = 1
            weatherRainingAndWindy = 0
            weatherSnow = 0
            weatherWindy = 0
        elif (weather == "6"):
            weatherCloudy = 0
            weatherForOrMist = 0
            weatherNormal = 0
            weatherOther = 0
            weatherRaining = 0
            weatherRainingAndWindy = 1
            weatherSnow = 0
            weatherWindy = 0
        elif (weather == "7"):
            weatherCloudy = 0
            weatherForOrMist = 0
            weatherNormal = 0
            weatherOther = 0
            weatherRaining = 0
            weatherRainingAndWindy = 0
            weatherSnow = 1
            weatherWindy = 0
        elif (weather == "8"):
            weatherCloudy = 0
            weatherForOrMist = 0
            weatherNormal = 0
            weatherOther = 0
            weatherRaining = 0
            weatherRainingAndWindy = 0
            weatherSnow = 0
            weatherWindy = 1
        
        y_pred = [[
            ageEighteenToThirty, ageThirtyOneToFifty, ageOverFifthyOne, ageUnderEighteen,
            male, female,
            driverExpOneToTwoYear, driverExpTwoToFiveYear, driverExpFiveToTenYear, driverExpAboveTenYear, driverExpBelowOneYear, driverExpNoLicense,
            weatherCloudy, weatherForOrMist, weatherNormal, weatherOther, weatherRaining, weatherRainingAndWindy, weatherSnow, weatherWindy
        ]]
        
        severityPrediction = model.predict(y_pred)
        if severityPrediction == 1:
            flash("Slighty Injury", "success")
        elif severityPrediction == 2:
            flash("Serious Injury", "warning")
        elif severityPrediction == 3:
            flash("Fatal Injury", "danger")
        else:
            return "Unknowm"
        
    return render_template("index.html")


@app.route('/load')
def loadmodel():
    # input: under 18, female, no license, raining and windy
    return str(model.predict([[
            0, 0, 0, 1,
            0,1,
            0,0,0,0,0,1,
            0,1,0,0,0,0,0,0
            ]]))


# [[
# ---- age ----
#   "18-30",  "31-50", "Over 51", "Under 18",  
# ----- gender ---
#   "Male", "Female",  
# ---- driving_exp ------
#   "1-2yr", "2-5yr", "5-10yr", "Above 10yr", "Below 1yr","No License", 
# ----- weather -----
#   "Cloudy", "Fog or mist", "Normal", "Other", "Raining", "Raining and Windy", "Snow", "Windy"
# ]]

if __name__ == '__main__':
    app.secret_key = 'uniks3cr3tk3y'
    app.run(debug=True)
