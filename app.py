from flask import Flask, render_template, request
import requests
import joblib
import numpy
import sklearn
import xgboost
import pandas

app = Flask(__name__)

#model = joblib.load("final_model.joblib")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict():
    if request.method == 'POST':
        Year = int(request.form['Year'])
        Odometer = int(request.form['Odometer'])
        Brand_Name = int(request.form['Brand_Name'])
        Model_Name = int(request.form['Model_Name'])
        Condition = int(request.form['Condition'])
        
        loaded_model = joblib.load("final_model.joblib")
        t = {'ODOMETER':[Odometer],'MODEL_YEAR':[Year],'BRAND_NAME':[Brand_Name],'MODEL_NAME':[Model_Name],'CONDITION_GRADE':[Condition]}
        test = pd.DataFrame(data = t)
        prediction = loaded_model.predict(test)
        output = round(prediction[0],2)

        if output<0:
            return render_template('index.html',prediction_text='This car has no remaining value and should be retired.')
        else:
            return render_template('index.html', prediction_text='The fair market value for {} {} {} is ${} dollars.'.format(Year, Brand_Name, Model_Name, output))
    else:
        return render_template('index.html')
