from flask import Flask, render_template
#import requests
#import pickle
#import numpy
#import sklearn

app = Flask(__name__)

#model = pickle.load(open('final_model.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict():
    if request.method == 'POST':
        Year = int(request.form['Year'])
        Odometer = int(request.form['Odometer'])
        Brand_Name = str(request.form['Brand_Name'])
        Model_Name = str(request.form['Model_Name'])
        Condition = str(request.form['Condition'])
        
        #prediction = model.predict([[Year,Odometer,Brand_Name,Model_Name,Condition]])
        #output = round(prediction[0],2)
        output = 35000
        if output<0:
            return render_template('index.html',prediction_text='This car has no remaining value and should be retired.')
        else:
            return render_template('index.html', prediction_text='The fair market value for {} {} {} is {} dollars.'.format(Year, Brand_Name, Model_Name, output))
    else:
        return render_template('index.html')
