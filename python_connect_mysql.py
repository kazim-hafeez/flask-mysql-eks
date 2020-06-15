from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import os
from flask import jsonify
host = os.environ['host']
app = Flask(__name__)
app.config['MYSQL_HOST'] = host
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234567'
app.config['MYSQL_DB'] = 'test'

mysql = MySQL(app)

@app.route('/home')
def home():
     return render_template('index2.html')
@app.route('/insert', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        firstName = details['fname']
        lastName = details['lname']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
        mysql.connection.commit()
        cur.close()
        return render_template('index3.html')
    return render_template('index.html')
@app.route('/get',methods=['GET'])
def get_data():
    data_list = []
    cur = mysql.connection.cursor()
    cur.execute("Select * from MyUsers")
    myresult = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    for x in myresult:
        data_list.append(x)
    resp = {'dataa': data_list}
    return jsonify(resp)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port='5011',debug=True)
