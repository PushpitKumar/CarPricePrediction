from flask import Flask, render_template, request
from flask_cors import cross_origin
import jsonify
import requests
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('random_forest_regression_model.pkl','rb'))

@app.route('/',methods=['GET'])
@cross_origin()
def Home():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
@cross_origin()
def predict():
    if request.method=='POST':

        #Present Price
        Present_Price = float(request.form['Present Price'])

        #Kilometers Driven
        Kms_Driven = float(request.form['Kms_Driven'])

        #Owner
        Owner = int(request.form['Owner'])

        #Age of Car
        Age_of_Car = float(request.form['Age of Car'])

        #Fuel Type
        Fuel_Type = request.form['Fuel Type']
        if Fuel_Type == 'Petrol':
            Fuel_Type_Petrol = 1
            Fuel_Type_Diesel = 0
        elif Fuel_Type == 'Diesel':
            Fuel_Type_Petrol = 0
            Fuel_Type_Diesel = 1
        else:
            #Fuel_Type_CNG = 1
            Fuel_Type_Petrol = 0
            Fuel_Type_Diesel = 0

        #Seller Type
        Seller_Type = request.form['Seller Type']
        if Seller_Type == 'Individual':
            Seller_Type_Individual = 1
        else:
            Seller_Type_Individual = 0

        #Transmission Type
        Transmission_Type = request.form['Transmission Type']
        if Transmission_Type == 'Manual':
            Transmission_Type_Manual = 1
        else:
            Transmission_Type_Manual = 0

        prediction = model.predict([[
        Present_Price,
        Kms_Driven,
        Owner,
        Age_of_Car,
        Fuel_Type_Diesel,
        Fuel_Type_Petrol,
        Seller_Type_Individual,
        Transmission_Type_Manual
        ]])

        result = round(prediction[0],2)

        return render_template('index.html',prediction_text="You can Sell Your Car at Rs {} Lacs".format(result))

    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)
