from flask import Flask, render_template, request, url_for,session, redirect

# import pyrebase
from firebase import Firebase
import Calculat as Cal

# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import db



config = {
    "apiKey": "AIzaSyAh2ji3JKKX-QHZv53sxXlNbpc_qet9yDU",
    "authDomain": "quiz-game-37caa.firebaseapp.com",
    "databaseURL": "https://quiz-game-37caa.firebaseio.com",
    "projectId": "quiz-game-37caa",
    "storageBucket": "quiz-game-37caa.appspot.com",
    "messagingSenderId": "699719760867",
    "appId": "1:699719760867:web:52dfbfbb32972b3692bed6",
    "measurementId": "G-L1E1RDRKYQ"
}

firebase = Firebase(config)

db = firebase.database()
auth = firebase.auth()

Sub = db.child('Subject/').get()
for subject in Sub.each():
    print(subject.key())
    print(subject.val()['SubID'])



# email = input("E-mail : \n")
# password = input("Password : \n")

# user = auth.create_user_with_email_and_password(email,password)
# user = auth.sign_in_with_email_and_password(email,password)

# auth.send_password_reset_email(email)
# auth.send_email_verification(user['idToken'])
# print(auth.get_account_info(user['idToken']))


app = Flask(__name__,template_folder='template')

@app.route("/Addchoice") #URL
def hello():
    Sub = db.child('Subject').get()
    return render_template('Addchoice.html', data = Sub)

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

        if Answer == 'Answer1':
            Answer = choice1
        elif Answer == 'Answer2':
            Answer = choice2
        elif Answer == 'Answer3':
            Answer = choice3
        elif Answer == 'Answer4':
            Answer = choice4

        Avgtime = Cal.Calchoice(Answer)

        
        checkdata = db.child("items-Hunter").get().val()
        
        if checkdata == None:
            db.child("items-Hunter").child("1").set({'subject':subject,'Qu':Propo,'C1':choice1,'C2':choice2,'C3':choice3,'C4':choice4,'ans':Answer,'Time':Avgtime,'ID':'1'})
        else:
            countDataQuiz = str(len(db.child("items-Hunter").get().val()))
            db.child("items-Hunter").child(countDataQuiz).set({'subject':subject,'Qu':Propo,'C1':choice1,'C2':choice2,'C3':choice3,'C4':choice4,'ans':Answer,'Time':Avgtime,'ID':countDataQuiz})
        return redirect(url_for('hello'))



@app.route("/AddSubject")
def AddSubject():
    return render_template('AddSubject.html')

@app.route("/inserSubject", methods=['GET','POST'])
def insertMember():
    return render_template('AddSubject.html')

@app.route("/Register", methods=['GET','POST'])
def Signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['email']
        try:
            user = auth.create_user_with_email_and_password(email,password)
            auth.send_email_verification(user['idToken'])
            return "Seccess"

        except:
            return "Fail"
    return render_template('signup.html')

@app.route("/Login")
def Login():
    return render_template('Login.html')

@app.route("/CheckLogin", methods=['GET','POST'])
def CheckLogin():
    unlogin = 'Check E-mail and Password'
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            auth.sign_in_with_email_and_password(email,password)
            # auth.get_account_info(user['idToken'])

            return render_template('Addchoice.html')
        except:
            return render_template('Login.html', us=unlogin)




@app.route("/Update")
def Update():
    to =  db.child("items/")
    
    return render_template('Update.html', data = to)

# all_users = db.child("ID/").get()
# # # print(all_users['name'])
# for key in all_users.each():

#     childz = key.key()
# #     # print(childz)
#     x = db.child("ID/"+childz).get().val()
#     print("ยืนยันรหัส : ",x['copassword'])
#     print("Name : ",x['name'])
#     print("Email : ",x['email'])




if __name__ == "__main__":
    app.run(debug=True)

