from flask import Flask, render_template,request
import mysql.connector
import pickle
import numpy as np

#Loading the imported model to this ide
model = pickle.load(open('model3.pkl', 'rb'))

app = Flask(__name__)

#Database connection
conn=mysql.connector.connect(host="sql6.freesqldatabase.com",user="sql6690645",password="FprweRcQHP",database="sql6690645")
cursor=conn.cursor()


#Redirects to login.html page
@app.route('/')
def login1():
    return render_template('login.html')


#Redirects to about.html page
@app.route('/about')
def about1():
    return render_template('about.html')


#Redirects to login.html page
@app.route('/login')
def login():
    return render_template('login.html')


#Redirects to register.html page
@app.route('/register')
def register():
    return render_template('register.html')

#Redirects to home.html page
@app.route('/home')
def home():
    return render_template('home.html')

#Redirects to privacy.html page
@app.route('/privacy')
def privacy1():
    return render_template('privacy.html')

#For login credentials storing page
@app.route('/login_validation', methods=['POST'])
def login_validation():
    email = request.form.get('email')
    password = request.form.get('password')

    cursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}'""".format(email, password))

    users = cursor.fetchall()
    if len(users)>0:
        return render_template('home.html')
    else:
        return render_template('login.html')


#For the Registration data storing page
@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form.get('uname')
    email = request.form.get('uemail')
    password = request.form.get('upassword')

    cursor.execute("""INSERT INTO `users` (`name`,`email`,`password`) VALUES ('{}','{}','{}')""".format(name, email, password))
    conn.commit()
    return "User Registered successfully"

#For the Privacy wala Page
@app.route('/privacy', methods=['POST'])
def privacy():
    data1 = request.form['age']
    data2 = request.form['sex']
    data3 = request.form['cp']
    data4 = request.form['trestbps']
    data5 = request.form['chol']
    data6 = request.form['fbs']
    data7 = request.form['restecg']
    data8 = request.form['thalach']
    data9 = request.form['exang']
    data10 = request.form['oldpeak']
    data11 = request.form['slope']
    data12 = request.form['ca']
    data13 = request.form['thal']

    arr = np.array([[data1, data2, data3, data4, data5, data6, data7, data8,
                     data9, data10, data11, data12, data13]])
    pred = model.predict(arr)

    return render_template('after.html', data=pred)
    # return str(pred)

#To avoid multiple runs
if __name__ == '__main__':
    app.run(debug=True)
