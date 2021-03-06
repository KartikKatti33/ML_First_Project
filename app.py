# -*- coding: utf-8 -*-
"""
Created on Sat May 21 17:33:17 2022

@author: kartik
"""

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('D:\Datascience\Projects\classifier\index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)
    print(output)

    return render_template('index.html', prediction_text='Purchase details: $ {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)