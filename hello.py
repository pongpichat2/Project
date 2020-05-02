from flask import Flask,render_template,request,redirect,url_for,session
import pymysql

app = Flask(__name__,template_folder='template')
conn=pymysql.connect('localhost','root','','projectgame') ##connect database

@app.route("/") #URL
def hello():
    with conn:
        cur=conn.cursor()
        cur.execute("select * from mem")
        rows = cur.fetchall()

    return render_template('index.html',data=rows) 

@app.route("/add") #URL
def formadd():
    return render_template('add.html') 

@app.route("/insert",methods=['POST'])
def insert():
    if request.method == "POST":
        fname = request.form['fname']
        lname = request.form['lname']
        with conn.cursor() as cursor:
            sql="INSERT INTO 'mem' ('fname','lname') value(%s,%s)"
            cursor.execute(sql,(fname,lname))
            print(sql)
            conn.commit()
        return redirect(url_for('hello'))


if __name__ == "__main__":
    app.run(debug=True)
