import flask
from flask import Flask, request, jsonify
import sqlfile
import mysql.connector as connection

app = Flask(__name__)

@app.route('/calculate/add', methods = ['POST'])


def add():
    if(request.method=='POST'):
        operation = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        if operation == 'add':
            r = num1 + num2
            result = 'summation of '+ str(num1)+' and '+str(num2)+' is: '+ str(r)

        return jsonify(result)

@app.route('/calculate/multiply', methods = ['POST'])
def multiply():
    if (request.method == 'POST'):
        operation = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])

        if operation == 'multiply':
            r = num2 * num1
            result = 'multiplication of ' + str(num1) + ' and ' + str(num2) + ' is: ' + str(r)
        return jsonify(result)

@app.route('/url')
def method_url():
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))
    result = num1 + num2
    return '''<h1>This is my result :  {}</h1>'''.format(result)

'''@app.route('/url1/{num1}/{num2}')
def method_url1():
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))
    result = num1 + num2
    return "<h1>This is my result :  {}</h1>".format(result)'''

@app.route('/createTable', methods = ['POST'])
def table_creation():
    if (request.method == 'POST'):
        table = request.json['table_name']
        conn = connection.connect(host="localhost", user="root", passwd="ashubairagi", use_pure=True)
        cur = conn.cursor()
        cur.execute('create database if not exists flaskDb')
        cur.execute('use flaskDb')
        cur.execute("create table {}(name varchar(20), id int(5))".format(table))
        conn.commit()
        conn.close()
        return jsonify("Table created successfully!")

@app.route('/insertOne', methods = ['POST'])
def insert_one():
    if (request.method == 'POST'):

        name = request.json['name']
        id = request.json['id']
        conn = connection.connect(host="localhost", database = "flaskDb", user="root", passwd="ashubairagi", use_pure=True)
        cur = conn.cursor()
        cur.execute("insert into student values('{}', {})".format(name,id))
        conn.commit()
        conn.close()
        return jsonify("Inserted data successfully!")

@app.route('/insertmany', methods = ['POST'])
def insert_many():
    if (request.method == 'POST'):
        conn = connection.connect(host="localhost", database="flaskDb", user="root", passwd="ashubairagi", use_pure=True)
        cur = conn.cursor()
        cur.execute("insert into student values ('ashutosh', 45)")
        cur.execute("insert into student values ('napalm', 12)")
        cur.execute("insert into student values ('bairagi', 78)")
        cur.execute("insert into student values ('xyz', 41)")
        conn.commit()
        conn.close()
        return "Inserted many records!"

@app.route('/delete', methods = ['POST'])
def delete():
    if (request.method == 'POST'):
        name = request.json['name']
        #id = request.json['id']
        conn = connection.connect(host="localhost", database="flaskDb", user="root", passwd="ashubairagi", use_pure=True)
        cur = conn.cursor()
        cur.execute("delete from student where name = '{}'".format(name))
        conn.commit()
        conn.close()
        return jsonify("Data deleted successfully")

@app.route('/download', methods = ['POST'])
def download_data():
    if (request.method == 'POST'):
        conn = connection.connect(host="localhost", database="flaskDb", user="root", passwd="ashubairagi", use_pure=True)
        cur = conn.cursor()
        cur.execute("select * from student")
        table = cur.fetchall()
        for i in range(len(table)):
            f = open("flaskDb_data.txt", "a")
            f.write(table[i])
            f.close()

        return jsonify("Data saved successfully! Check the txt file....")

if (__name__ == '__main__') :
    app.run()

