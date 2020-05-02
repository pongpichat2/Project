from flask import Flask,render_template,request,redirect,url_for,session
# import pymysql.cursors

from firebase import firebase
import Calculat as Cal

# URL Project #
url = "https://project-e54fe.firebaseio.com" 
# ตัวกำการเชื่อมกับ Firebase #
messenger = firebase.FirebaseApplication(url, None)


app = Flask(__name__,template_folder='template')

@app.route("/Addchoice") #URL
def hello():
    return render_template('Addchoice.html') 

# Insert คำถามลงใน Database #
@app.route("/insertChoice", methods=['GET','POST'])
def insertChoice():
    if request.method == "POST":
        subject = request.form['Subject']
        Propo = request.form['Proposition']
        choice1 = request.form['Ch1']
        choice2 = request.form['Ch2']
        choice3 = request.form['Ch3']
        choice4 = request.form['Ch4']
        Answer = request.form['Answer']

        # Cal.Calchoice(Answer)
        Insert = {'Subject':subject,'Quiz':Propo,'Ch1':choice1,'Ch2':choice2,'Ch3':choice3,'Ch4':choice4,'Answer':Answer}
        
        result = messenger.post('/Quiz',Insert)
        

        



       
if __name__ == "__main__":
    app.run(debug=True)