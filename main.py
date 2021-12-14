import numpy as np
import pandas as pd


from flask import Flask, render_template, request
from flask_cors import CORS,cross_origin

import os
import pickle


model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])  # To render Homepage
@cross_origin()
def home_page():
    return render_template('index.html')


@app.route('/result', methods=['POST'])  # To render Result page
@cross_origin()
def result():
    if request.method == 'POST':
        try:
            input_features = request.form.to_dict()
            print(input_features)
            input_features = {k.strip(): [float(v)] for k, v in input_features.items()}
            print(input_features)
            data = pd.DataFrame(input_features)

            result = model.predict(data)[0]
            print(f'Result is: {result}')

            cls = {
                0: 'c-CS-m',
                1: 'c-CS-s',
                2: 'c-SC-m',
                3: 'c-SC-s',
                4: 't-CS-m',
                5: 't-CS-s',
                6: 't-SC-m',
                7: 't-SC-s'
            }
            final_pred = cls[result]

            print(f'Predicted Class: {final_pred}')
            return render_template('result.html', result=result)
            
        except Exception as e:
            print('The Exception message is: \n',e)
            return 'Something went wrong'
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

