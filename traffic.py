class Traffic:
    def ageArray(age):
        ageEighteenToThirty = 0
        ageThirtyOneToFifty= 0
        ageOverFifthyOne = 0
        ageUnderEighteen = 0
        
        if (age == "1"):
            ageEighteenToThirty = 1
        elif (age == "2"):
            ageThirtyOneToFifty= 1
        elif (age == "3"):
            ageOverFifthyOne = 1
        elif (age == "4"):
            ageUnderEighteen = 1
        
        return [ageEighteenToThirty, ageThirtyOneToFifty, ageOverFifthyOne, ageUnderEighteen]

    def genderArray(gender):
        male = 0
        female = 0
        if (gender == "1"):
            male = 1
        else:
            female = 1
        
        return [male, female]
    
    def driverExpArray(driverexp):
        driverExpOneToTwoYear = 0
        driverExpTwoToFiveYear = 0
        driverExpFiveToTenYear = 0
        driverExpAboveTenYear = 0
        driverExpBelowOneYear = 0
        driverExpNoLicense = 0
        if (driverexp == "1"):
            driverExpOneToTwoYear = 1
        elif (driverexp == "2"):
            driverExpTwoToFiveYear = 1
        elif (driverexp == "3"):
            driverExpFiveToTenYear = 1
        elif (driverexp == "4"):
            driverExpAboveTenYear = 1
        elif (driverexp == "5"):
            driverExpBelowOneYear = 1
        elif (driverexp == "6"):
            driverExpNoLicense = 1
        
        return [driverExpOneToTwoYear, driverExpTwoToFiveYear, driverExpFiveToTenYear, driverExpAboveTenYear,driverExpBelowOneYear, driverExpNoLicense]
        
    def weatherArray(weather):
        weatherCloudy = 0
        weatherForOrMist = 0
        weatherNormal = 0
        weatherOther = 0
        weatherRaining = 0
        weatherRainingAndWindy = 0
        weatherSnow = 0
        weatherWindy = 0
        if (weather == "1"):
            weatherCloudy = 1
        elif (weather == "2"):
            weatherForOrMist = 1
        elif (weather == "3"):
            weatherNormal = 1
        elif (weather == "4"):
            weatherOther = 1
        elif (weather == "5"):
            weatherRaining = 1
        elif (weather == "6"):
            weatherRainingAndWindy = 1
        elif (weather == "7"):
            weatherSnow = 1
        elif (weather == "8"):
            weatherWindy = 1
        
        return [weatherCloudy, weatherForOrMist, weatherNormal, weatherOther, weatherRaining, weatherRainingAndWindy, weatherSnow, weatherWindy]
    
    # get value from input and return 2d array for model prediction
    # array structure for model prediction
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
    def arrayAtribute(age, gender, driverexp, weather):
        ageVal = Traffic.ageArray(age)
        genderVal = Traffic.genderArray(gender)
        driverExpVal = Traffic.driverExpArray(driverexp)
        weatherVal = Traffic.weatherArray(weather)
        
        return [ageVal + genderVal + driverExpVal + weatherVal]