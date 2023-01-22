# Rodeo App for Final Project (Team 4)

Dataset from [Kaggle - Road Traffic Accident Dataset of Addis Ababa City](https://www.kaggle.com/datasets/saurabhshahane/road-traffic-accidents)

## How To run this project

1. open directory project on terminal
2. run `pip install -r "requirement.txt"` to install package
3. then run `python app.py` to start flask
4. open http://127.0.0.1:5000 on your browser

**if you using python3 :**

1. run `pip3 install -r requirements.txt` to install package

**if you got error :**

1. run `pip3 instal-r requirements.txt --ignore-installed`

## How to Run Flask App

`export FLASK_APP=name`

**Debug On:** 
`export FLASK_DEBUG=1`

**Run Flask:** 
`flask run`

## Files in repo

`traffic_model.ipynb` is the Implementation of Decision Tree Classification Model. Run ini jika ingin tahu proses tiap baris kode

`traffic_model.py` is the Implementation of joblib model. Run file ini untuk generate model

`app.py` is the Flask Implementation of the Model. main file untuk menjalankan flask website

`traffic.py` helper class.

`templates/index.html` contains the front end for the Web Application.

`static` contains bootstrap assets for website


*This is repo deployed with vercel host*