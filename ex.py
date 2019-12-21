from flask import Flask, render_template, request
import json
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict' , methods=['POST'])
def predict():
    msg = ""
    home = request.form['home']
    age = request.form['age']
    income = request.form['income']
    experience = request.form['experience']
    #creating a json file
    payload = [{"Home":home,"Age":int(age),"Income":int(income),"Experience":int(experience)}]
    #sending request to restAPI
    r = requests.post('http://127.0.0.1:5000/predict', json=payload)
    pred = int(json.loads(r.content)['prediction'][1])
    if pred  == 1:
        msg = "Congrats! You are eligible for a loan"
    else:
        msg = "Sorry! You are not eligiable for a loan"
    return render_template('index.html', home=home, age=age,income=income,experience=experience, data=payload,r=r.content,msg=msg)

if __name__ == "__main__":
    app.run(debug=True,port=5001)