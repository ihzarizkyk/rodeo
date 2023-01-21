class Traffic:
    def ageArray(age):
        """create an array for driver age
        ["18-30",  "31-50", "Over 51", "Under 18"]
        
        Args:
            age (string): "1" to "4"

        Returns:
            array: 1D array represent age value
        """
        
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
        """create an array for driver gender
        ["male", "female"]

        Args:
            gender (string): "1" for male otherwise female

        Returns:
            array: 1D array represent gender value
        """
        
        male = 0
        female = 0
        if (gender == "1"):
            male = 1
        else:
            female = 1
        
        return [male, female]
    
    def driverExpArray(driverexp):
        """create an array for driver experience,
        ["1-2yr", "2-5yr", "5-10yr", "Above 10yr", "Below 1yr","No License"]

        Args:
            driverexp (string): "1" to "6"

        Returns:
            array: 1D array represent driver experience
        """
        
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
        """create an array for weather condition
        ["Cloudy", "Fog or mist", "Normal", "Other", "Raining", "Raining and Windy", "Snow", "Windy"]
        
        Args:
            weather (string): "1" to "8"

        Returns:
            array: 1D array represent weather condition
        """
        
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
    def severityArray(age, gender, driverexp, weather):
        """create an array for the DecisionTreeClassifier.predict models

        Args:
            age (string): Age value "1" to "4"
            gender (string): Gender value "1" for male otherwise female
            driverexp (string): Driver Experience, value "1" to "6"
            weather (string): Weather condition, value "1" to "8"

        Returns:
            array: 2D array for DecisionTreeClassifier model
        """
        
        ageVal = Traffic.ageArray(age)
        genderVal = Traffic.genderArray(gender)
        driverExpVal = Traffic.driverExpArray(driverexp)
        weatherVal = Traffic.weatherArray(weather)
        
        return [ageVal + genderVal + driverExpVal + weatherVal]