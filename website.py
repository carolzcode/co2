import csv
import os
import random
from datetime import date
import re
from urllib import request
import pymysql
import ar_master
import smtplib, ssl
from flask import Flask, render_template, flash, request, session, current_app, send_from_directory
from werkzeug.utils import redirect, secure_filename
app = Flask(__name__, static_folder="static")
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
user='root'
password=''
host='localhost'
 
mm = ar_master.master_flask_code()


@app.route("/")
def homepage():
    return render_template('index.html')


@app.route("/user_home")
def user_home():
    return render_template('user_home.html')



@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/register")
def register():
    return render_template('register.html')


@app.route("/user_register", methods=['GET', 'POST'])
def user_register():
    if request.method == 'POST':
       name = request.form['name']

       contact = request.form['mobile']

       password = request.form['password']

       maxin = mm.find_max_id("user_details")
       qry = ("insert into user_details values('" + str(maxin) + "','" + str(name) + "','" + str( contact) + "','" + str(password) + "','0')")
       result = mm.insert_query(qry)
       return render_template('login.html')
    return render_template('register.html')



@app.route("/user_login", methods=['GET', 'POST'])
def user_login():
    error = None
    if request.method == 'POST':
        un = request.form['uname']
        pa = request.form['pass']
        usern = mm.select_direct_query(
            "select * from user_details where name='" + str(un) + "' and password='" + str(pa) + "' and status='0'")
        if usern:
            session['user'] = un
            return render_template('user_home.html', msg1="Login Success",data=False)
        else:

            return render_template('login.html', msg="Username or Password Incorrect")
    return render_template('login.html')


def csv_predict_data(make,model,class_name,enigne_size,cylinder,engine_no):
    print(make,model,class_name,enigne_size,cylinder,engine_no)
    ob = 'CO2 Emissions_Canada.csv'
    file = ob
    with open(file) as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            t1 = row['Make'].lower()
            t2 = row['Model'].lower()
            t3 = row['Vehicle Class'].lower()
            t4 = row['CO2 Emissions(g/km)'].lower()
            t5 = row['engine_no'].lower()
            tmp=int(t4)
            # if t1==make and t2==model and t3==class_name and t5==engine_no and tmp<150:
            if t1==make and t2==model and t3==class_name and t5==engine_no and tmp<150:
                return "Low",str(tmp)
                break
            elif t1 == make and t2 == model and t3 == class_name and t5 == engine_no and tmp <= 255:
                return "Medium",str(tmp)
                break
            elif t1 == make and t2 == model and t3 == class_name and t5 == engine_no and tmp > 255:
                return "High",str(tmp)
                break
        return "No data found",""





@app.route("/predict_data", methods=['GET', 'POST'])
def predict_data():
    sample=["Encourage the use of electric or hybrid vehicles"
        ,"Advocate for the development of publictransportation systems"
        ,"Raise awareness about the benefits of regular vehicle maintenance to improve fuel efficiency"
        ,"Encourage use of bicycles or walking for short tripsinstead of driving"
        ,"Plant trees and sapport reforestation efforts."]
    n=3

    if request.method == 'POST':
        # name = request.form['name']
        make = request.form['make']
        model = request.form['model']
        class_name = request.form['class_name']
        engine_size = request.form['engine_size']
        cylinder = request.form['cylinder']
        engine_no = request.form['engine_no']
        result,value=csv_predict_data(make.lower(), model.lower(), class_name.lower(), engine_size.lower(), cylinder.lower(), engine_no.lower())
        print(result,value)
        if result =="High":
            xx=(random.sample(sample, n))
            return render_template('user_home.html',result=result,value=value,items=xx,data=True)
        else:
            return render_template('user_home.html',result=result,value=value,data=True)

    return render_template('user_home.html',data=False)




######################################
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

