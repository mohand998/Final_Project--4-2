from flask import Flask, request,jsonify
import joblib
import numpy as np
import pickle
import sklearn
model=joblib.load('model2')
model = pickle.load(open('model1.pkl','rw'))
app = Flask(__name__)


@app.route('/')
def home():
    return "Hello World!"

@app.route('/predict',methods=['POST'])
def predict():
  age = request.form.get('age')
  sex = request.form.get('sex')
  cp = request.form.get('cp')
  trestbps = request.form.get('trestbps')
  chol = request.form.get('chol')
  fbs = request.form.get('fbs')
  restecg = request.form.get('restecg')
  thalach = request.form.get('thalach')
  exang = request.form.get('exang')
  oldpeak = request.form.get('oldpeak')
  ca = request.form.get('ca')
  thal = request.form.get('thal')
  # cgpa = request.form['cgpa']
  # age = request.form['age']
  # weight = request.form['weight']

  # result = {'age':age,'sex':sex,'cp':cp,'trestbps':trestbps,'chol':chol,'fbs':fbs,'restecg':restecg,'thalach':thalach,'exang':exang,'oldpeak':oldpeak,'ca':
  #           ca,'thal':thal}
  # result = {'cgpa':cgpa,'age':age,'weight':weight}
  input_query = np.array([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,ca,thal])

  result=model.predict(input_query)[0]


  return jsonify({'target':result})


if __name__ == '__main__':
    app.run(debug=True)