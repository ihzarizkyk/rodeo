import pandas as pd

data = pd.read_csv('dataset_traffic.csv', sep=";")

from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(sparse=False, dtype=int)
data[["18-30", "31-50", "Over 51", "Under 18"]] = ohe.fit_transform(data[["age"]])
data[["Male", "Female"]] = ohe.fit_transform(data[["gender"]])
data[["1-2yr", "2-5yr", "5-10yr", "Above 10yr", "Below 1yr", "No License"]] = ohe.fit_transform(data[["driving_exp"]])
data[["Cloudy", "Fog or mist", "Normal", "Other", "Raining", "Raining and Windy", "Snow", "Windy"]] = ohe.fit_transform(data[["weather"]])

data.dropna()

X = data[["18-30", "31-50", "Over 51", "Under 18", "Male", "Female", "1-2yr", "2-5yr", "5-10yr", "Above 10yr", "Below 1yr", "No License", "Cloudy", "Fog or mist", "Normal", "Other", "Raining", "Raining and Windy", "Snow", "Windy"]]
y = data[["severity"]]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()

model.fit(X_train, y_train)

from joblib import dump

dump(model, 'model_traffic.joblib')