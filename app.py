from flask import Flask, render_template, request, url_for, redirect, session

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


# Login
# Sub = db.child('Admin/')

# nameInput = 'Waew'
# for subject in Sub.get().val():
#     if(subject == nameInput):
#         print("In data")
#         Key = db.child('Admin/').child('Waew').get()
#         if(Key.val()['Pass'] == "aaa"):
#             print("Password in database")
#         else:
#             print("Password not in  database")

#     elif(subject != nameInput):
#         print("not in data")

    

    
    # if(subject == 'aew'):
    #     print('Waew in database')
    #     Key = db.child('Admin/').child('Pongpichat').get()
    #     if(Key.val()['Pass'] == "aaa"):
    #         print("Password in database")
    #     else:
    #         print("Password not in  database")


# LIKE 
# query =  database.getReference().child("StoreAds").orderByChild("University").startAt("ps").endAt("\uf8ff");


# email = input("E-mail : \n")
# password = input("Password : \n")

# user = auth.create_user_with_email_and_password(email,password)
# user = auth.sign_in_with_email_and_password(email,password)

# auth.send_password_reset_email(email)
# auth.send_email_verification(user['idToken'])
# print(auth.get_account_info(user['idToken']))


app = Flask(__name__,template_folder='template')
app.secret_key = "hello"

@app.route("/Login")
def Login():

    return render_template('Login.html')

@app.route("/CheckLogin", methods=['GET','POST'])
def CheckLogin():
    if request.method == 'POST':
        Username = request.form['Username']
        Password = request.form['password']

        root = db.child('Admin')

        for check in root.get().val():
            if check == Username:

                ref = db.child('Admin').child(Username).get()

                # เก็บ session 
                if ref.val()['Password'] == Password :
                    session['User'] = Username
                    print(session['User'])
                    print('Go to Page Home')
                    return redirect(url_for("Home"))
    
    # return redirect(url_for('Login'))



@app.route("/Register", methods=['GET','POST'])
def Register():
    if request.method == 'POST':

        Username = request.form['Username']
        Pass = request.form['Password']
        Co_pass = request.form['Con_Pass']
        Email = request.form['Email']
        Sub = request.form.getlist('Sub[]')


        for C in db.child('Admin').get().val():
            # การเช็คว่า มี Username ซ้ำ
            if C == Username :
                print("Username มีผู้ใช้แล้ว")
            else:
                db.child("Admin").child(Username).set({"Username":Username,"Password":Pass,"Co_Pass": Co_pass,"Email":Email})

                # การบันทึก Subject หลายๆค่า หรือค่าเดียว
                if (len(Sub) == 1 ):
                    db.child("Admin").child(Username).child("Subject_pro").child(Sub[0]).set({"Sub_name":Sub[0],"DataNum":"0"})
                else:
                    for i in range(len(Sub)) :
                        db.child("Admin").child(Username).child("Subject_pro").child(Sub[i]).set({"Sub_name":Sub[i],"DataNum":"0"})

                    return redirect(url_for('Home'))


@app.route("/Home")
def Home():
    user = session['User']

    return render_template('Home.html',name = user)

@app.route("/Addchoice") #URL
def hello():

    IDuser = session['User']
    Sub = db.child('Admin').child(IDuser).child('Subject_pro').get()
    return render_template('Addchoice.html', data = Sub)

# Insert คำถามลงใน Database #
@app.route("/insertChoice", methods=['GET','POST'])
def insertChoice():
    user = session['User']

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
        
        checkdata = db.child("Subject").child(subject).child("Quiz").get().val()
        
        if checkdata == None:
            db.child("Subject").child(subject).child("Quiz").child("NO_1").set({'subject':subject,'Qu':Propo,'C1':choice1,'C2':choice2,'C3':choice3,'C4':choice4,'ans':Answer,'Time':Avgtime,'ID':'1'})
            db.child("Admin").child(user).child("Subject_pro").child(subject).set({'DataNum':'1','Sub_name':subject})
        else:
            countDataQuiz = str(len(db.child("Subject").child(subject).child("Quiz").get().val())+1)
            db.child("Subject").child(subject).child("Quiz").child("NO_"+countDataQuiz).set({'subject':subject,'Qu':Propo,'C1':choice1,'C2':choice2,'C3':choice3,'C4':choice4,'ans':Answer,'Time':Avgtime,'ID':countDataQuiz})
            db.child("Admin").child(user).child("Subject_pro").child(subject).set({'DataNum':countDataQuiz,'Sub_name':subject})
        return redirect(url_for('hello'))

# @app.route("/AddSubject", methods=['GET','POST'])
# def AddSubject():
#     if request.method == 'POST':
#         subname = request.form['Subname']
#         subid = request.form['Subid']
#         checkdata = db.child("Subject").get().val()

#         if checkdata == None:
#             db.child("Subject").child("1").set({"SUBNAME":subname,"SUBID" : subid})
#         else:
#             countDataSub = str(len(db.child("Subject").get().val()))
#             db.child("Subject").child(countDataSub).set({"SUBNAME":subname,"SUBID" : subid,"NO":countDataSub})
        
#     return redirect(url_for('hello'))

# @app.route("/SubjectHome")
# def SubjectHome():
#     to =  db.child("Subject/")

#     return render_template('AddSubject.html',data = to)

# @app.route("/AddSubjectHome", methods=['GET','POST'])
# def Subject():
    
#     if request.method == 'POST':
#         subname = request.form['Subname']
#         subid = request.form['SubID']

#         checkdata = db.child("Subject").get().val()
#         if checkdata == None:
#             db.child("Subject").child("1").set({"SUBNAME":subname,"SUBID" : subid,"NO":"1"})
#             return redirect(url_for('SubjectHome'))

#         else:
#             countDataSub = str(len(db.child("Subject").get().val()))
#             db.child("Subject").child(countDataSub).set({"SUBNAME":subname,"SUBID" : subid,"NO":countDataSub})
#             return redirect(url_for('SubjectHome'))
        

@app.route("/Update")
def Update():
    to =  db.child("items/")
    return render_template('Update.html', data = to)

@app.route("/UpdateSubject", methods=['GET','POST'])
def UpDatesub():
    
    if request.method == 'POST':
        no = request.form['NOSUB']
        subname = request.form['Subname']
        subid = request.form['SubID']
        button = request.form['BTN']

        if no == "":
            return redirect(url_for('SubjectHome'))
        elif button == "Edit":
            db.child("Subject").child(no).update({"SUBNAME":subname,"SUBID":subid})
            return redirect(url_for('SubjectHome'))
        elif button == "Delete":
            db.child("Subject").child(no).remove()
            return redirect(url_for('SubjectHome'))


@app.route("/Subject", methods=['GET','POST'])
def Subject():
    user = session['User']
    Detil = db.child('Admin').child(user).child('Subject_pro').get()

    if request.method == 'POST':
        Sub_name = request.form['Subname']

        # ref = db.child('Admin').child(user).child('Subject_pro').get()
        # print(Sub_name)

        ShowSub = db.child('Subject').child(Sub_name).child('Quiz').get()
        return render_template('Subject.html',data = Detil,Show = ShowSub ,Headtext = Sub_name)


    return render_template('Subject.html',data = Detil)

@app.route("/Evopage", methods=['GET','POST'])
def Evopage():
    user = session['User']
    ShowSubject = db.child('Admin').child(user).child('Subject_pro').get()

    if request.method == 'POST':
        Sub = request.form['Sub_name']

        SubMem = db.child('Subject').child(Sub).child('Member').get()

        session['SubjectRef'] = Sub

        if SubMem.val() == None:
            ErrorText = "ยังไม่มีผู้เล่นในรายวิชานี้"
            return render_template('evo.html',Subject = ShowSubject , ErrorA = ErrorText )
        else:
            return render_template('evo.html',Subject = ShowSubject , ShowData = SubMem ) 

    return render_template('evo.html', Subject = ShowSubject)


@app.route("/ShowEvo", methods=['GET','POST'])
def ShowEvo():
    SubRef = session['SubjectRef']
    if request.method == 'POST':
        User = request.form['Username']

        DataUser = db.child('Subject').child(SubRef).child('Member').child(User).get()

        Name = DataUser.val()['Name']
        Stu_Code = DataUser.val()['Stu_Code']
        return render_template('ShowEvo.html', SubName = SubRef , NAME = Name , StuCode = Stu_Code )

    return render_template('ShowEvo.html')


@app.route("/Logout")
def Logout():
    session.pop('User', None)
    return redirect(url_for('Login'))


# SubMem = db.child('Subject').child('Anatome').child('Member').get()
# for a in SubMem.each():
#     print(a.key())





if __name__ == "__main__":
    app.run(debug=True)

