import flask
from flask import Flask, request, render_template, redirect, url_for
import pickle
import numpy as np
import time

app = Flask(__name__)

lc_model = pickle.load(open('models/LCmodel.pkl', 'rb'))
ts_model = pickle.load(open('models/TSmodel.pkl', 'rb'))

@app.route('/')

def home():
    return render_template('home.html')

@app.route('/predict_lung_cancer/', methods=['GET','POST'])
def predict_lung_cancer() -> "html":
    if request.method == 'GET':
        return render_template('cancer_form.html')
    else:
        int_lc_features = [int(x) for x in request.form.values()]
        lc_features = [np.array(int_lc_features)]
        lc_output = lc_model.predict(lc_features)
        if (lc_output==0):
            #lc_text = "Result: The patient has not got lung cancer.
            return render_template('cancer_false.html') #lc_prediction_text=lc_text)
        else:
            return render_template('survival_form.html')

    



@app.route('/survival', methods=['GET','POST'])
def survival() -> "html":
    if request.method == 'GET':
        return render_template('survival_form.html')
    elif request.method =='POST':
        int_ts_features = [int(x) for x in request.form.values()]
        ts_features = [np.array(int_ts_features)]
        ts_output = ts_model.predict(ts_features)
        if (ts_output==0):
            #ts_text = "Result: The patient will survive a year or even more after surgery."
            return render_template('survival_false.html')
        else:
            #ts_text = "Result: The patient will not survive a  whole year after surgery."
            return render_template('survival_true.html') #, ts_prediction_text=ts_text)



if __name__ == "__main__":
    app.run()
    

