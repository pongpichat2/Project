from flask import Flask, render_template, request, url_for, redirect, session, jsonify
import math
import json
# import pyrebase
from firebase import Firebase
import Calculat as Cal
from array import *
import random

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

app = Flask(__name__,template_folder='template')
app.secret_key = "hello"



@app.route("/")
def Login():

    return render_template('Login.html')

@app.route("/CheckLogin", methods=['GET','POST'])
def CheckLogin():
    if request.method == 'POST':
        Username = request.form['Username']
        Password = request.form['password']
        root = db.child('Admin')

        if Username in root.get().val():
            
            ref = db.child('Admin').child(Username).get()
                # เก็บ session 
            if ref.val()['Password'] == Password :
                session['Admin'] = Username
                session['EmailAdmin'] = ref.val()['Email']
                Status = ref.val()['Status']
                if Status == 'teacher':

                    return redirect(url_for("Home"))
                else:
                    return redirect(url_for("HomeAdmin"))
            else:
                ErrorPass = "Password Error check password please !"
                return render_template('Login.html' , ErrorPass = ErrorPass)
        else:
            ErrorUsername = "Username Error check Username please !"
            return render_template('Login.html' , ErrorUser = ErrorUsername)
    return redirect(url_for('Login'))


@app.route("/Home")
def Home():
    if session.get('Admin') == None:
        return redirect(url_for('Login'))
    else:
        IDAdmin = session['Admin']
        EmailAdmin = session['EmailAdmin']

        SubLock = ""
        Admin_Subject = db.child('Admin').child(IDAdmin).child('Subject_pro').get()
        
        for Check in Admin_Subject.each():
            Check_Status = db.child('Admin').child(IDAdmin).child('Subject_pro').child(Check.key()).get()
            if(Check_Status.val()['Status'] == "Unlock"):
                # SubLock = Check.key()+" Locked"+SubLock
                # print(SubLock)
                continue
                # return render_template('Home.html',name = EmailAdmin ,DataSubject = Admin_Subject)
            elif((Check_Status.val()['Status'] == "Lock")):
                
                SubLock = Check.key()+" , "+SubLock
                # print(SubLock)
 
        if(len(SubLock) == 0):
            return render_template('Home.html',name = EmailAdmin ,DataSubject = Admin_Subject)
        else:
            AdminNameLock = Check_Status.val()['AdminLock']
            return render_template('Home.html',name = EmailAdmin ,DataSubject = Admin_Subject,SubLock = SubLock,AdminNameLock =AdminNameLock)
        
        

        

@app.route("/HomeAdmin")
def HomeAdmin():
    if session.get('Admin') == None:
        return redirect(url_for('Login'))
    else:
        IDAdmin = session['Admin']
        EmailAdmin = session['EmailAdmin']

        return render_template('HomeAdmin.html',name = EmailAdmin)


@app.route("/HomeAdmin_TH")
def HomeAdmin_TH():
    if session.get('Admin') == None:
        return redirect(url_for('Login'))
    else:
        IDAdmin = session['Admin']
        EmailAdmin = session['EmailAdmin']
 
        return render_template('HomeAdmin_TH.html',name = EmailAdmin )

@app.route("/Home_TH")
def Home_TH():
    if session.get('Admin') == None:
        return redirect(url_for('Login'))
    else:
        IDAdmin = session['Admin']
        EmailAdmin = session['EmailAdmin']
        Admin_Subject = db.child('Admin').child(IDAdmin).child('Subject_pro').get()
        return render_template('Home_TH.html',name = EmailAdmin ,DataSubject = Admin_Subject)
        
@app.route("/Addchoice") #URL
def hello():
    if session.get('Admin') == None:
        return redirect(url_for('Login'))
    else:
        IDAdmin = session['Admin']
        EmailAdmin = session['EmailAdmin']
        Sub = db.child('Admin').child(IDAdmin).child('Subject_pro').get()
        Admin_Subject = db.child('Admin').child(IDAdmin).child('Subject_pro').get()
        return render_template('Addchoice.html',name = EmailAdmin, data = Sub,DataSubject = Admin_Subject)

@app.route("/Addchoice_TH") #URL
def Addchoice_TH():
    if session.get('Admin') == None:
        return redirect(url_for('Login'))
    else:
        IDAdmin = session['Admin']
        EmailAdmin = session['EmailAdmin']
        Sub = db.child('Admin').child(IDAdmin).child('Subject_pro').get()
        Admin_Subject = db.child('Admin').child(IDAdmin).child('Subject_pro').get()
        return render_template('Addchoice_TH.html',name = EmailAdmin, data = Sub,DataSubject = Admin_Subject)

# Insert คำถามลงใน Database #
@app.route("/insertChoice", methods=['GET','POST'])
def insertChoice():
    user = session['Admin']

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
        
        checkdata = db.child('Class').child(subject).get().val()
        # checkdata = db.child("Subject").child(subject).child("Quiz").get().val()
        
        if checkdata == None:
            db.child('Class').child(subject).child("NO1").set({'subject':subject,'Qu':Propo,'C1':choice1,'C2':choice2,'C3':choice3,'C4':choice4,'ans':Answer,'Time':Avgtime,'ID':'1'})
            # db.child("Subject").child(subject).child("Quiz").child("NO_1").set({'subject':subject,'Qu':Propo,'C1':choice1,'C2':choice2,'C3':choice3,'C4':choice4,'ans':Answer,'Time':Avgtime,'ID':'1'})
            db.child("Admin").child(user).child("Subject_pro").child(subject).update({'DataNum':'1','Sub_name':subject})
            db.child("Class_Subject").child(subject).set({'Status':'Unlock'})
        else:

            countDataQuiz = str(len(db.child('Class').child(subject).get().val())+1)
            # for 
            # countDataQuiz= 1
          
            db.child('Class').child(subject).child('NO'+countDataQuiz).set({'subject':subject,'Qu':Propo,'C1':choice1,'C2':choice2,'C3':choice3,'C4':choice4,'ans':Answer,'Time':Avgtime,'ID':countDataQuiz})
            db.child("Admin").child(user).child("Subject_pro").child(subject).update({'DataNum':countDataQuiz,'Sub_name':subject})
            db.child("Class_Subject").child(subject).set({'Status':'Unlock'})
        return redirect(url_for('hello'))

# Insert คำถามลงใน Database #
@app.route("/insertChoice_TH", methods=['GET','POST'])
def insertChoice_TH():
    user = session['Admin']

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
        
        checkdata = db.child('Class').child(subject).get().val()
        # checkdata = db.child("Subject").child(subject).child("Quiz").get().val()
        
        if checkdata == None:
            db.child('Class').child(subject).child("NO1").set({'subject':subject,'Qu':Propo,'C1':choice1,'C2':choice2,'C3':choice3,'C4':choice4,'ans':Answer,'Time':Avgtime,'ID':'1'})
            # db.child("Subject").child(subject).child("Quiz").child("NO_1").set({'subject':subject,'Qu':Propo,'C1':choice1,'C2':choice2,'C3':choice3,'C4':choice4,'ans':Answer,'Time':Avgtime,'ID':'1'})
            db.child("Admin").child(user).child("Subject_pro").child(subject).update({'DataNum':'1','Sub_name':subject})
            db.child("Class_Subject").child(subject).set({'Status':'Unlock'})
        else:
            countDataQuiz = str(len(db.child('Class').child(subject).get().val())+1)
            db.child('Class').child(subject).child('NO'+countDataQuiz).set({'subject':subject,'Qu':Propo,'C1':choice1,'C2':choice2,'C3':choice3,'C4':choice4,'ans':Answer,'Time':Avgtime,'ID':countDataQuiz})
            db.child("Admin").child(user).child("Subject_pro").child(subject).update({'DataNum':countDataQuiz,'Sub_name':subject})
            db.child("Class_Subject").child(subject).set({'Status':'Unlock'})
        return redirect(url_for('Addchoice_TH'))


@app.route("/Subject", methods=['GET','POST'])
def Subject():
    if session.get('Admin') == None:
        return redirect(url_for('Login'))
    else:
        EmailAdmin = session['EmailAdmin']
        user = session['Admin']
        Detil = db.child('Admin').child(user).child('Subject_pro').get()
        Admin_Subject = db.child('Admin').child(user).child('Subject_pro').get()
        if request.method == 'POST':
            Sub_name = request.form['Subname']
            session['Subname_Update'] = Sub_name

            ShowSub = db.child('Class').child(Sub_name).get()
            if ShowSub.val() == None :
                textError = "None"
                return render_template('Subject.html',data = Detil,Show = ShowSub ,Headtext = Sub_name,DataSubject = Admin_Subject , NoneData = textError,name = EmailAdmin)
            else:
                textHave = "haveData"
                return render_template('Subject.html',data = Detil,Show = ShowSub ,Headtext = Sub_name,DataSubject = Admin_Subject , haveData = textHave,name = EmailAdmin)

        return render_template('Subject.html',data = Detil,DataSubject = Admin_Subject,name = EmailAdmin)

@app.route("/Subject_TH", methods=['GET','POST'])
def Subject_TH():
    if session.get('Admin') == None:
        return redirect(url_for('Login'))
    else:
        EmailAdmin = session['EmailAdmin']
        user = session['Admin']
        Detil = db.child('Admin').child(user).child('Subject_pro').get()
        Admin_Subject = db.child('Admin').child(user).child('Subject_pro').get()
        if request.method == 'POST':
            Sub_name = request.form['Subname']
            session['Subname_Update'] = Sub_name

            ShowSub = db.child('Class').child(Sub_name).get()
            if ShowSub.val() == None :
                textError = "None"
                return render_template('Subject_TH.html',data = Detil,Show = ShowSub ,Headtext = Sub_name,DataSubject = Admin_Subject , NoneData = textError,name = EmailAdmin)
            else:
                textHave = "haveData"
                return render_template('Subject_TH.html',data = Detil,Show = ShowSub ,Headtext = Sub_name,DataSubject = Admin_Subject , haveData = textHave,name = EmailAdmin)

        return render_template('Subject_TH.html',data = Detil,DataSubject = Admin_Subject,name = EmailAdmin)

@app.route("/Sub_Update", methods=['GET','POST'])
def Sub_Update():
    user = session['Admin']
    Subname = session['Subname_Update']
    if request.method == 'POST':
        NO_Sub = request.form['NO_Sub']
        Quiz = request.form['Quiz']
        C1 = request.form['C1']
        C2 = request.form['C2']
        C3 = request.form['C3']
        C4 = request.form['C4']

        TypeUp = request.form['Type_Up']

        if TypeUp == 'Edit':
            Answer = request.form['Answer']
            if(Answer == '1'):
                Answer = C1
            elif(Answer == '2'):
                Answer = C2
            elif(Answer == '3'):
                Answer = C3
            elif(Answer == '4'):
                Answer = C4
            AvgUpdate = Cal.Calchoice(Answer)
            db.child('Class').child(Subname).child('NO'+NO_Sub).update({"Qu":Quiz,"C1":C1,"C2":C2,"C3":C3,"C4":C4,"ans":Answer,"Time":AvgUpdate})
        elif TypeUp == 'Delete':
            db.child('Class').child(Subname).child('NO'+NO_Sub).remove()
            try:
                countDataQuiz = str(len(db.child('Class').child(Subname).get().val()))
                db.child('Admin').child(user).child('Subject_pro').child(Subname).update({"DataNum":countDataQuiz})
            except:
                db.child('Admin').child(user).child('Subject_pro').child(Subname).update({"DataNum":0})

    return redirect(url_for('Subject'))

@app.route("/Evopage", methods=['GET','POST'])
def Evopage():
    if session.get('Admin') == None:
        return redirect(url_for('Login'))
    else:
        user = session['Admin']
        EmailAdmin = session['EmailAdmin']
        ShowSubject = db.child('Admin').child(user).child('Subject_pro').get()
        Admin_Subject = db.child('Admin').child(user).child('Subject_pro').get()

        if request.method == 'POST':
            Sub = request.form['Sub_name']
            if Sub == 'ALL':
                SubMem = db.child('Subject').child(Sub).child('Member').get()
            else:
                SubMem = db.child('Subject').child(Sub).child('Member').get()

                session['SubjectRef'] = Sub
                if SubMem.val() == None:
                    ErrorText = "ยังไม่มีผู้เล่นในรายวิชานี้"
                    return render_template('evo.html',Subject = ShowSubject , ErrorA = ErrorText ,DataSubject = Admin_Subject,name = EmailAdmin)
                else:
                    
                    return render_template('evo.html',Subject = ShowSubject , ShowData = SubMem,DataSubject = Admin_Subject ,SubjectName = Sub,name = EmailAdmin) 

        return render_template('evo.html', Subject = ShowSubject,DataSubject = Admin_Subject,name = EmailAdmin)

@app.route("/Evopage_TH", methods=['GET','POST'])
def Evopage_TH():
    if session.get('Admin') == None:
        return redirect(url_for('Login'))
    else:
        user = session['Admin']
        EmailAdmin = session['EmailAdmin']
        ShowSubject = db.child('Admin').child(user).child('Subject_pro').get()
        Admin_Subject = db.child('Admin').child(user).child('Subject_pro').get()

        if request.method == 'POST':
            Sub = request.form['Sub_name']
            SubMem = db.child('Subject').child(Sub).child('Member').get()

            session['SubjectRef'] = Sub
            if SubMem.val() == None:
                ErrorText = "ยังไม่มีผู้เล่นในรายวิชานี้"
                return render_template('evo_TH.html',Subject = ShowSubject , ErrorA = ErrorText ,DataSubject = Admin_Subject,name = EmailAdmin)
            else:
                
                return render_template('evo_TH.html',Subject = ShowSubject , ShowData = SubMem,DataSubject = Admin_Subject ,SubjectName = Sub,name = EmailAdmin) 

        return render_template('evo_TH.html', Subject = ShowSubject,DataSubject = Admin_Subject,name = EmailAdmin)

@app.route("/ShowEvo", methods=['GET','POST'])
def ShowEvo():
    if session.get('Admin') == None:
        return redirect(url_for('Login'))
    else:
        SubRef = session['SubjectRef']
        EmailAdmin = session['EmailAdmin']
        ShowMem = db.child('Subject').child(SubRef).child('Member').get()
        Admin_Subject = db.child('Admin').child(session['Admin']).child('Subject_pro').get()
        if request.method == 'POST':
            Member = request.form['Username']
            session['Member'] = Member

            DataUser = db.child('Subject').child(SubRef).child('Member').child(session['Member']).get()

            Name = DataUser.val()['Name']
            Email = DataUser.val()['Email']

            session['NameMember'] = Name
            session['Email'] = Email
        return render_template('ShowEvo.html',name = EmailAdmin, SubName = SubRef, NAME = session['NameMember'] , email = session['Email'], ShowData = ShowMem ,DataSubject = Admin_Subject)

@app.route("/ShowEvo_TH", methods=['GET','POST'])
def ShowEvo_TH():
    if session.get('Admin') == None:
        return redirect(url_for('Login'))
    else:
        SubRef = session['SubjectRef']
        EmailAdmin = session['EmailAdmin']
        ShowMem = db.child('Subject').child(SubRef).child('Member').get()
        Admin_Subject = db.child('Admin').child(session['Admin']).child('Subject_pro').get()
        if request.method == 'POST':
            Member = request.form['Username']
            session['Member'] = Member

            DataUser = db.child('Subject').child(SubRef).child('Member').child(session['Member']).get()

            Name = DataUser.val()['Name']
            Email = DataUser.val()['Email']

            session['NameMember'] = Name
            session['Email'] = Email
        return render_template('ShowEvo_TH.html',name = EmailAdmin, SubName = SubRef, NAME = session['NameMember'] , email = session['Email'], ShowData = ShowMem ,DataSubject = Admin_Subject)

@app.route("/ShowEvoAlpha", methods=['GET','POST'])
def ShowEvoAlpha():
    if session.get('Admin') == None:
        return redirect(url_for('Login'))
    else:
        Admin_Subject = db.child('Admin').child(session['Admin']).child('Subject_pro').get()
        ShowMem = db.child('IntroGame').child('Alphabet').get()
        EmailAdmin = session['EmailAdmin']
        if request.method == 'POST':
            Member = request.form['Username']
            session['Member'] = Member
            DataUser = db.child('IntroGame').child('Alphabet').child(session['Member']).get()
            Name = DataUser.val()['Name']
            Email = DataUser.val()['Email']
            session['NameMember'] = Name
            session['Email'] = Email

        return render_template('ShowEvoAlpha.html', NAME = session['NameMember'] , email = session['Email'], ShowData = ShowMem ,DataSubject = Admin_Subject,name = EmailAdmin)
@app.route("/ShowEvoAlpha_TH", methods=['GET','POST'])
def ShowEvoAlpha_TH():
    if session.get('Admin') == None:
        return redirect(url_for('Login'))
    else:
        Admin_Subject = db.child('Admin').child(session['Admin']).child('Subject_pro').get()
        ShowMem = db.child('IntroGame').child('Alphabet').get()
        EmailAdmin = session['EmailAdmin']
        if request.method == 'POST':
            Member = request.form['Username']
            session['Member'] = Member
            DataUser = db.child('IntroGame').child('Alphabet').child(session['Member']).get()
            Name = DataUser.val()['Name']
            Email = DataUser.val()['Email']
            session['NameMember'] = Name
            session['Email'] = Email

        return render_template('ShowEvoAlpha_TH.html',name = EmailAdmin, NAME = session['NameMember'] , email = session['Email'], ShowData = ShowMem ,DataSubject = Admin_Subject)

@app.route("/ShowEvoShoot", methods=['GET','POST'])
def ShowEvoShoot():
    if session.get('Admin') == None:
        return redirect(url_for('Login'))
    else:
        Admin_Subject = db.child('Admin').child(session['Admin']).child('Subject_pro').get()
        ShowMem = db.child('IntroGame').child('ShootGame').get()
        EmailAdmin = session['EmailAdmin']
        if request.method == 'POST':
            Member = request.form['Username']
            session['Member'] = Member
            DataUser = db.child('IntroGame').child('ShootGame').child(session['Member']).get()
            Name = DataUser.val()['Name']
            Email = DataUser.val()['Email']
            session['NameMember'] = Name
            session['Email'] = Email

        return render_template('ShowEvoShootGame.html',name = EmailAdmin, NAME = session['NameMember'] , email = session['Email'], ShowData = ShowMem ,DataSubject = Admin_Subject)

@app.route("/ShowEvoShoot_TH", methods=['GET','POST'])
def ShowEvoShoot_TH():
    if session.get('Admin') == None:
        return redirect(url_for('Login'))
    else:
        Admin_Subject = db.child('Admin').child(session['Admin']).child('Subject_pro').get()
        ShowMem = db.child('IntroGame').child('ShootGame').get()
        EmailAdmin = session['EmailAdmin']
        if request.method == 'POST':
            Member = request.form['Username']
            session['Member'] = Member
            DataUser = db.child('IntroGame').child('ShootGame').child(session['Member']).get()
            Name = DataUser.val()['Name']
            Email = DataUser.val()['Email']
            session['NameMember'] = Name
            session['Email'] = Email

        return render_template('ShowEvoShoot_TH.html',name = EmailAdmin, NAME = session['NameMember'] , email = session['Email'], ShowData = ShowMem ,DataSubject = Admin_Subject)

@app.route("/Evoindex", methods=['GET','POST'])
def Evoindex():
    if session.get('Admin') == None:
        return redirect(url_for('Login'))
    else:
        IDAdmin = session['Admin']
        EmailAdmin = session['EmailAdmin']
        Sub = db.child('Admin').child(IDAdmin).child('Subject_pro').get()
        Admin_Subject = db.child('Admin').child(IDAdmin).child('Subject_pro').get()
        if request.method == 'POST':
            Game_Evo = request.form['NameGame']
            if Game_Evo == 'Alphabet':
                return redirect('/Evoalpha')
            elif Game_Evo == 'Adventure':
                return redirect('/Evopage')
            elif Game_Evo == 'Shoot':
                return redirect('/Evoshoot')
        return render_template('evoindex.html',DataSubject = Admin_Subject,name = EmailAdmin)

@app.route("/Evoalpha", methods=['GET','POST'])
def Evoalpha():
    if session.get('Admin') == None:
        return redirect(url_for('Login'))
    else:
        IDAdmin = session['Admin']
        EmailAdmin = session['EmailAdmin']
        Sub = db.child('Admin').child(IDAdmin).child('Subject_pro').get()
        Admin_Subject = db.child('Admin').child(IDAdmin).child('Subject_pro').get()
        mainGameAlpha = db.child('IntroGame').child('Alphabet').get()
        if mainGameAlpha.val() == None:
            error = 'ไม่มีผู้เล่น'
            return render_template('evoalpha.html',DataSubject = Admin_Subject,error = error,name = EmailAdmin)
        else:
            havedata ='มีผู้เล่น'
            return render_template('evoalpha.html',DataSubject = Admin_Subject,havedata = havedata,mainGameAlpha = mainGameAlpha,name = EmailAdmin)

@app.route("/Evoalpha_TH", methods=['GET','POST'])
def Evoalpha_TH():
    if session.get('Admin') == None:
        return redirect(url_for('Login'))
    else:
        IDAdmin = session['Admin']
        EmailAdmin = session['EmailAdmin']
        Sub = db.child('Admin').child(IDAdmin).child('Subject_pro').get()
        Admin_Subject = db.child('Admin').child(IDAdmin).child('Subject_pro').get()
        mainGameAlpha = db.child('IntroGame').child('Alphabet').get()
        if mainGameAlpha.val() == None:
            error = 'ไม่มีผู้เล่น'
            return render_template('evoalpha_TH.html',DataSubject = Admin_Subject,error = error,name = EmailAdmin)
        else:
            havedata ='มีผู้เล่น'
            return render_template('evoalpha_TH.html',DataSubject = Admin_Subject,havedata = havedata,mainGameAlpha = mainGameAlpha,name = EmailAdmin)


@app.route("/Evoshoot", methods=['GET','POST'])
def Evoshoot():
    if session.get('Admin') == None:
        return redirect(url_for('Login'))
    else:
        IDAdmin = session['Admin']
        EmailAdmin = session['EmailAdmin']
        Sub = db.child('Admin').child(IDAdmin).child('Subject_pro').get()
        Admin_Subject = db.child('Admin').child(IDAdmin).child('Subject_pro').get()
        mainGameShoot= db.child('IntroGame').child('ShootGame').get()
        if mainGameShoot.val() == None:
            error = 'ไม่มีผู้เล่น'
            return render_template('evoshoot.html',DataSubject = Admin_Subject,error = error,name = EmailAdmin)
        else:
            havedata ='มีผู้เล่น'
            return render_template('evoshoot.html',DataSubject = Admin_Subject,havedata = havedata,mainGameShoot = mainGameShoot,name = EmailAdmin)
@app.route("/Evoshoot_TH", methods=['GET','POST'])
def Evoshoot_TH():
    if session.get('Admin') == None:
        return redirect(url_for('Login'))
    else:
        IDAdmin = session['Admin']
        EmailAdmin = session['EmailAdmin']
        Sub = db.child('Admin').child(IDAdmin).child('Subject_pro').get()
        Admin_Subject = db.child('Admin').child(IDAdmin).child('Subject_pro').get()
        mainGameShoot= db.child('IntroGame').child('ShootGame').get()
        if mainGameShoot.val() == None:
            error = 'ไม่มีผู้เล่น'
            return render_template('evoshoot_TH.html',DataSubject = Admin_Subject,error = error,name = EmailAdmin)
        else:
            havedata ='มีผู้เล่น'
            return render_template('evoshoot_TH.html',DataSubject = Admin_Subject,havedata = havedata,mainGameShoot = mainGameShoot,name = EmailAdmin)

@app.route("/Evoindex_TH", methods=['GET','POST'])
def Evoindex_TH():
    if session.get('Admin') == None:
        return redirect(url_for('Login'))
    else:
        IDAdmin = session['Admin']
        EmailAdmin = session['EmailAdmin']
        Sub = db.child('Admin').child(IDAdmin).child('Subject_pro').get()
        Admin_Subject = db.child('Admin').child(IDAdmin).child('Subject_pro').get()
        if request.method == 'POST':
            Game_Evo = request.form['NameGame']
            if Game_Evo == 'Alphabet':
                return redirect('/Evoalpha_TH')
            elif Game_Evo == 'Adventure':
                return redirect('/Evopage_TH')
            elif Game_Evo == 'Shoot':
                return redirect('/Evoshoot_TH')
        return render_template('evoindex_TH.html',DataSubject = Admin_Subject,name = EmailAdmin)


@app.route("/DeleteSub_allPage", methods=['GET','POST'])
def DeleteSub_allPage():
    Admin = session['Admin']
    if request.method == 'POST':
        Sub_Before = request.form['Subject_Befor']
        db.child('Admin').child(Admin).child('Subject_pro').child(Sub_Before).remove()
        db.child('Class').child(Sub_Before).remove()
        db.child('All_Subject').child(Sub_Before).remove()

    return redirect(url_for('Home'))

@app.route("/AddSub_allPage", methods=['GET','POST'])
def AddSub_allPage():
    Admin = session['Admin']
    EmailAdmin = session['EmailAdmin']
    Admin_Subject = db.child('Admin').child(Admin).child('Subject_pro').get()
    if request.method == 'POST':
        AddSub = request.form.getlist('Sub[]')
        CheckSubject = db.child('Admin').child(Admin).child("Subject_pro").get()
        CheckSubjectAll = db.child('Class').get()
        Subindata = "มีอยู่แล้วในฐานข้อมูล"
        if(len(AddSub) == 1):
            if(AddSub[0] in CheckSubject.val()):
                SubError = "วิชา : "+AddSub[0]+" "+Subindata
                return render_template('Home.html',name = EmailAdmin ,DataSubject = Admin_Subject, ErrorSub = SubError)
            elif(AddSub[0] in CheckSubjectAll.val()):
                SubError = "วิชา : "+AddSub[i]+" "+Subindata
                return render_template('Home.html',name = EmailAdmin ,DataSubject = Admin_Subject, ErrorSub = SubError)
            else:
                
                db.child("Admin").child(Admin).child("Subject_pro").child(AddSub[0]).set({"Sub_name":AddSub[0],"DataNum":"0","Status":"Unlock"})
                db.child("All_Subject").child(AddSub[0]).set({"owner":Admin,"Status":"Unlock"})
          
        else:
            for i in range(len(AddSub)) :
                
                if AddSub[i] in CheckSubject.val():
                    SubError = "วิชา : "+AddSub[i]+" "+Subindata
                    return render_template('Home.html',name = EmailAdmin ,DataSubject = Admin_Subject, ErrorSub = SubError)
                elif AddSub[i] in CheckSubjectAll.val():
                    SubError = "วิชา : "+AddSub[i]+" "+Subindata
                    return render_template('Home.html',name = EmailAdmin ,DataSubject = Admin_Subject, ErrorSub = SubError)
                else:

                    db.child("Admin").child(Admin).child("Subject_pro").child(AddSub[i]).set({"Sub_name":AddSub[i],"DataNum":"0","Status":"Unlock"})
                    db.child("All_Subject").child(AddSub[i]).set({"owner":Admin,"Status":"Unlock"})
  

    return redirect(url_for('Home'))

@app.route("/ChangePass_allPage", methods=['GET','POST'])
def ChangePass_allPage():
    Admin = session['Admin']
    EmailAdmin = session['EmailAdmin']
    Admin_Subject = db.child('Admin').child(Admin).child('Subject_pro').get()
    if request.method == 'POST':
        Pass_Be = request.form['Pass_Before']
        Pass_Af = request.form['Pass_After'] 
        Pass_co = request.form['CoPass_After']
        Data = db.child('Admin').child(Admin).get()
        if Data.val()['Password'] == Pass_Be:
            db.child('Admin').child(Admin).update({"Password":Pass_Af,"Co_Pass":Pass_co})
            SuccessPass = "Success"
            return render_template('Home.html',name = EmailAdmin ,DataSubject = Admin_Subject, SuccessPass = SuccessPass)
        else:
            ChangeError = "รหัสผ่านผิด"
            return render_template('Home.html',name = EmailAdmin ,DataSubject = Admin_Subject, Error = ChangeError)

    return redirect(url_for('Home'))

@app.route("/AddTeacher", methods=['GET','POST'])
def AddTeacher():
    if session.get('Admin') == None:
        return redirect(url_for('Login'))
    else:
        IDAdmin = session['Admin']
        EmailAdmin = session['EmailAdmin']

        return render_template('AddTeacher.html',name = EmailAdmin)



@app.route("/AddTeacher_TH", methods=['GET','POST'])
def AddTeacher_TH():
    if session.get('Admin') == None:
        return redirect(url_for('Login'))
    else:
        IDAdmin = session['Admin']
        EmailAdmin = session['EmailAdmin']

        return render_template('AddTeacher_TH.html',name = EmailAdmin)

@app.route("/LockSubject")
def LockSubject():
    if session.get('Admin') == None:
        return redirect(url_for('Login'))
    else:
        IDAdmin = session['Admin']
        EmailAdmin = session['EmailAdmin']

        dataSub = db.child("All_Subject").get()
        return render_template('LockSubject.html',name = EmailAdmin ,dataSub = dataSub)

@app.route("/Up_LockSubject", methods=['GET','POST'])
def Up_LockSubject():
    if session.get('Admin') == None:
        return redirect(url_for('Login'))
    else:
        IDAdmin = session['Admin']
        if request.method == 'POST':
            Name_Sub = request.form['Sub_name']
            Status = request.form['Status']

            db.child('All_Subject').child(Name_Sub).update({'Status':Status})
            Key = db.child('All_Subject').child(Name_Sub).get().val()
            if(Status == 'Lock'):
                db.child('Admin').child(Key['owner']).child('Subject_pro').child(Name_Sub).update({'Status':Status,'AdminLock':IDAdmin})
                db.child("Class_Subject").child(Name_Sub).update({'Status':Status})
            elif(Status == 'Unlock'):
                db.child('Admin').child(Key['owner']).child('Subject_pro').child(Name_Sub).update({'Status':Status,'AdminLock':IDAdmin})
                db.child("Class_Subject").child(Name_Sub).update({'Status':Status})
                

            return redirect(url_for('LockSubject'))

@app.route("/Edittime")
def Edittime():
    if session.get('Admin') == None:
        return redirect(url_for('Login'))
    else:
        IDAdmin = session['Admin']
        EmailAdmin = session['EmailAdmin']
        with open('Time.json') as f:
            data = json.load(f)

        for emp in data['TimeManhattan']:
            
  
            timeText = emp['TimeText']
    
            timedistance = emp['timedistance']

            timeSpacbar = emp['TimeText'] 

            timeDuplicate = emp['timeDuplicate']

        return render_template('Edittime.html',name = EmailAdmin,timeText=timeText,timedistance=timedistance,timeSpacbar=timeSpacbar,timeDuplicate=timeDuplicate)

@app.route("/EdittimeJson", methods=['GET','POST'])
def EdittimeJson():
    if session.get('Admin') == None:
        return redirect(url_for('Login'))
    else:
        if request.method == 'POST':
            timeText = request.form['timeText']
            timeSpacbar = request.form['timeSpacbar']
            timeDuplicate = request.form['timeDuplicate']
            timeDistance = request.form['Distance']

            a_file = open("Time.json", "r")
            json_object = json.load(a_file)

            data = json_object["TimeManhattan"]

            for time in data:
                time["TimeText"] = timeText
                time["timedistance"] = timeDistance
                time["timeDuplicate"] = timeDuplicate
                time["timeSpacbar"] = timeSpacbar

            a_file = open("Time.json", "w")
            json.dump(json_object, a_file)
            a_file.close()
            
            Class = db.child('Class').get()
            for AllClass in Class.each():
                Sub = db.child('Class').child(AllClass.key()).get()
                for AllSub in Sub.each():
                    if AllSub.key() == 'Status':
                        continue
                    elif AllSub.key() == 'owner':
                        continue
                    else:
                        Answer = AllSub.val()['ans']
                        Avgtime = Cal.Calchoice(Answer)

                        db.child('Class').child(AllClass.key()).child(AllSub.key()).update({"Time":Avgtime})
        return redirect(url_for('Edittime'))

@app.route("/ChangePass_allPage_Admin", methods=['GET','POST'])
def ChangePass_allPage_Admin():
    Admin = session['Admin']
    EmailAdmin = session['EmailAdmin']
    Admin_Subject = db.child('Admin').child(Admin).child('Subject_pro').get()
    if request.method == 'POST':
        Pass_Be = request.form['Pass_Before']
        Pass_Af = request.form['Pass_After'] 
        Pass_co = request.form['CoPass_After']
        Data = db.child('Admin').child(Admin).get()
        if Data.val()['Password'] == Pass_Be:
            db.child('Admin').child(Admin).update({"Password":Pass_Af,"Co_Pass":Pass_co})
            SuccessPass = "Success"
            return render_template('HomeAdmin.html',name = EmailAdmin ,DataSubject = Admin_Subject, SuccessPass = SuccessPass)
        else:
            ChangeError = "รหัสผ่านผิด"
            return render_template('HomeAdmin.html',name = EmailAdmin ,DataSubject = Admin_Subject, Error = ChangeError)

    return redirect(url_for('HomeAdmin'))

@app.route("/Register", methods=['GET','POST'])
def Register():
    if request.method == 'POST':
        EmailAdmin = session['EmailAdmin']
        Username = request.form['Username']
        Pass = request.form['Password']
        Co_pass = request.form['Con_Pass']
        Email = request.form['Email']
        Sub = request.form.getlist('Sub[]')

        CheckMember = db.child('Admin').get().val()

        CheckSubject = db.child('All_Subject').get().val()
            # การเช็คว่า มี Username ซ้ำ
        
        if Username in CheckMember :
            Usernamerepea = "Already have a user account"
            return render_template('AddTeacher.html',name = EmailAdmin, Usernamerepea = Usernamerepea)
        
        else:
            
            db.child("Admin").child(Username).set({"Username":Username,"Password":Pass,"Co_Pass": Co_pass,"Email":Email,"Status":"teacher"})

                # การบันทึก Subject หลายๆค่า หรือค่าเดียว
            if (len(Sub) == 1 ):
                
                if Sub[0] in CheckSubject:
                    Suberror = "Adding Subject Error"
                    db.child("Admin").child(Username).remove()
                    return render_template('AddTeacher.html',name = EmailAdmin , Suberror = Suberror)
                else:
                    db.child("Admin").child(Username).child("Subject_pro").child(Sub[0]).set({"Sub_name":Sub[0],"DataNum":"0","Status":"Unlock"})
                    db.child("All_Subject").child(Sub[0]).set({"owner":Username,"Status":"Unlock"})
     
            else:
                for i in range(len(Sub)):
                    if Sub[i] in CheckSubject:
                        Suberror = Sub[i]+" Adding Subject Error please Login"
                        return render_template('AddTeacher.html',name = EmailAdmin , Suberror = Suberror)
                    else:
                        db.child("Admin").child(Username).child("Subject_pro").child(Sub[i]).set({"Sub_name":Sub[i],"DataNum":"0","Status":"Unlock"})
                        db.child("All_Subject").child(Sub[i]).set({"owner":Username,"Status":"Unlock"})
        

  
    return redirect(url_for('AddTeacher'))

@app.route("/Register_TH", methods=['GET','POST'])
def Register_TH():
    if request.method == 'POST':
        EmailAdmin = session['EmailAdmin']
        Username = request.form['Username']
        Pass = request.form['Password']
        Co_pass = request.form['Con_Pass']
        Email = request.form['Email']
        Sub = request.form.getlist('Sub[]')

        CheckMember = db.child('Admin').get().val()

        CheckSubject = db.child('All_Subject').get().val()
            # การเช็คว่า มี Username ซ้ำ
        
        if Username in CheckMember :
            Usernamerepea = "Already have a user account"
            return render_template('AddTeacher.html',name = EmailAdmin, Usernamerepea = Usernamerepea)
        
        else:
            
            db.child("Admin").child(Username).set({"Username":Username,"Password":Pass,"Co_Pass": Co_pass,"Email":Email,"Status":"teacher"})

                # การบันทึก Subject หลายๆค่า หรือค่าเดียว
            if (len(Sub) == 1 ):
                
                if Sub[0] in CheckSubject:
                    Suberror = "Adding Subject Error"
                    db.child("Admin").child(Username).remove()
                    return render_template('AddTeacher.html',name = EmailAdmin , Suberror = Suberror)
                else:
                    db.child("Admin").child(Username).child("Subject_pro").child(Sub[0]).set({"Sub_name":Sub[0],"DataNum":"0","Status":"Unlock"})
                    db.child("All_Subject").child(Sub[0]).set({"owner":Username,"Status":"Unlock"})
        
            else:
                for i in range(len(Sub)):
                    if Sub[i] in CheckSubject:
                        Suberror = Sub[i]+" Adding Subject Error please Login"
                        return render_template('AddTeacher.html',name = EmailAdmin , Suberror = Suberror)
                    else:
                        db.child("Admin").child(Username).child("Subject_pro").child(Sub[i]).set({"Sub_name":Sub[i],"DataNum":"0","Status":"Unlock"})
                        db.child("All_Subject").child(Sub[i]).set({"owner":Username,"Status":"Unlock"})
         

  
    return redirect(url_for('AddTeacher_TH'))

@app.route("/DataChart_GameAlpha")
def DataChart_GameAlpha():
    Member = session['Member']
    DataRefGame1 = db.child('IntroGame').child('Alphabet').child(Member).child('score').get()
            # Chart Member main 
    DatachartGame1 = ['0']
    arrayGame1 = []
    AVG_Array = ['0',]
    labels_G1 = ['0','1','2']
    if DataRefGame1.val() == None:
        DatachartGame1 = ['0']
    else:
        for G1 in DataRefGame1.each():
            
            DatachartGame1.append(G1.val()['Correct'])
    
    # การหา AVG ของเกมที่1
    # คนที่ส่งเข้ามา เพื่อที่หาจำนวนครั้งในการเล่น
    if DataRefGame1.val() == None:
        AVG_Array = ['0']
    else:
        mainDataScore_1 = db.child('IntroGame').child('Alphabet').child(Member).child('score').get()
        CountLabel = 3
        for CountData_1 in mainDataScore_1.each():
            labels_G1.append(CountLabel)
            CountLabel += 1
            CountData_arr_1 = []
            arrayGame1.append(CountData_arr_1)

        all_score_Game_1 = db.child('IntroGame').child('Alphabet').get()
        for allMember_in_Game_1 in all_score_Game_1.each():
            posi_arr_1 = 0 
            Name_member_1 = allMember_in_Game_1.key()
            time_Score_1 = db.child('IntroGame').child('Alphabet').child(Name_member_1).child('score').get()
            
            for Score_in_Game_1 in time_Score_1.each():

                try:
                    arrayGame1[posi_arr_1].append(Score_in_Game_1.val()['Correct'])
                except:
                    continue
                posi_arr_1 += 1


        # T-mean
        for CountArray_1 in range(len(arrayGame1)):
            NumArray_1 = len(arrayGame1[CountArray_1])
            if NumArray_1 < 20 :
                continue
            else:
                sortArray_G1 = sorted(arrayGame1[CountArray_1])
                lenData_G1 = sortArray_G1
                lengthCut_1 = len(lenData_G1)*0.025
                
                if "." in str(lengthCut_1):
                    Onepoint_1 = '%.2f'%(lengthCut_1)
                    Backpoint = str(Onepoint_1).split(".")[-1]

                    if int(Backpoint) >= 5 :
                        Cut_G1 = math.ceil(float(lengthCut_1))
                    else:
                        Cut_G1 = math.floor(float(lengthCut_1))
                    
                    if Cut_G1 == 0:
                        continue
                    else:
                        for removeData_G1 in range(Cut_G1):
                            arrayGame1[CountArray_1].remove(sortArray_G1[removeData_G1])
                            arrayGame1[CountArray_1].remove(sortArray_G1[(removeData_G1+1)*-1])

        for AVG in range(len(arrayGame1)):
            AVG_Score = '%.1f'%(sum(arrayGame1[AVG])/len(arrayGame1[AVG]))
    
            AVG_Array.append(AVG_Score)

    return jsonify({'ChartDataGame1':DatachartGame1,'AVGGame1':AVG_Array,'Label_G1':labels_G1})

@app.route("/DataChart_GameShoot")
def DataChart_GameShoot():
    Member = session['Member']
    DataRefGame2 = db.child('IntroGame').child('ShootGame').child(Member).child('score').get()
    DatachartGame2 = ['0']
    arrayGame2 = []
    AVG_Array2 = ['0',]
    labels_G2 = ['0','1','2']

    if DataRefGame2.val() == None:
        DatachartGame2 = ['0']
    else:
        for G2 in DataRefGame2.each():
            DatachartGame2.append(G2.val()['score'])
    
    if DataRefGame2.val() == None:
        AVG_Array2 = ['0']
    else:
        # การหาเกม 2
        mainDataScore_2 = db.child('IntroGame').child('ShootGame').child(Member).child('score').get()
        CountLabel = 3
        for CountData_2 in mainDataScore_2.each():
            labels_G2.append(CountLabel)
            CountLabel += 1
            CountData_arr_2 = []
            arrayGame2.append(CountData_arr_2)

        all_score_Game_2 = db.child('IntroGame').child('ShootGame').get()

        for allMember_in_Game_2 in all_score_Game_2.each():
            posi_arr_2 = 0 
            Name_member_2 = allMember_in_Game_2.key()
            time_Score_2 = db.child('IntroGame').child('ShootGame').child(Name_member_2).child('score').get()
            
            for Score_in_Game_2 in time_Score_2.each():

                try:
                    arrayGame2[posi_arr_2].append(Score_in_Game_2.val()['score'])
                except:
                    continue
                posi_arr_2 += 1

        # T-mean
        for CountArray_2 in range(len(arrayGame2)):
            NumArray_2 = len(arrayGame2[CountArray_2])
            if NumArray_2 <= 20 :
                continue
            else:
                sortArray_G2 = sorted(arrayGame2[CountArray_2])
                lenData_G2 = sortArray_G2
                lengthCut_2 = len(lenData_G2)*0.025
                
                if "." in str(lengthCut_2):
                    Onepoint_2 = '%.2f'%(lengthCut_2)
                    Backpoint = str(Onepoint_2).split(".")[-1]

                    if int(Backpoint) >= 5 :
                        Cut_G2 = math.ceil(float(lengthCut_2))
                    else:
                        Cut_G2 = math.floor(float(lengthCut_2))
                    if Cut_G2 == 0:
                        continue
                    else:
                        for removeData_G2 in range(Cut_G2):
                            arrayGame2[CountArray_2].remove(sortArray_G2[removeData_G2])
                            arrayGame2[CountArray_2].remove(sortArray_G2[(removeData_G2+1)*-1])

        for AVG_G2 in range(len(arrayGame2)):
            AVG_Score_G2 = '%.1f'%(sum(arrayGame2[AVG_G2])/len(arrayGame2[AVG_G2]))

            AVG_Array2.append(AVG_Score_G2)
        
    return jsonify({'ChartDataGame2':DatachartGame2,'AVGGame2':AVG_Array2,'Label_G2':labels_G2})

@app.route("/dataChart")
def DataChart():
    Member = session['Member']

    SubjectRef = session['SubjectRef']

    DataRefGame3 = db.child('Subject').child(SubjectRef).child('Member').child(Member).child('AdventuresGame').get()

    DatachartGame3 = ['0']


    if DataRefGame3.val() == None:
        DatachartGame3 = ['0']
    else:
        for G3 in DataRefGame3.each():
            
            DatachartGame3.append(G3.val()['score'])

    arrayGame3 = []
    AVG_Array3 = ['0',]

    labels_G3 = ['0','1','2']


    if DataRefGame3.val() == None:
        AVG_Array3 = ['0']
    else:
        
        mainDataScore_3 = db.child('Subject').child(SubjectRef).child('Member').child(Member).child('AdventuresGame').get()
        CountLabel = 3
        for CountData_3 in mainDataScore_3.each():
            labels_G3.append(CountLabel)
            CountLabel += 1
            CountData_arr_3 = []
            arrayGame3.append(CountData_arr_3)

        all_score_Game_3 = db.child('Subject').child(SubjectRef).child('Member').get()
        for allMember_in_Game_3 in all_score_Game_3.each():
            posi_arr_3 = 0 
            Name_member_3 = allMember_in_Game_3.key()
            time_Score_3 = db.child('Subject').child(SubjectRef).child('Member').child(Name_member_3).child('AdventuresGame').get()
            
            for Score_in_Game_3 in time_Score_3.each():

                try:
                    arrayGame3[posi_arr_3].append(Score_in_Game_3.val()['score'])
                except:
                    continue
                posi_arr_3 += 1

        # T-mean
        for CountArray_3 in range(len(arrayGame3)):
            NumArray_3 = len(arrayGame3[CountArray_3])
            if NumArray_3 <= 20 :
                continue
            else:
                sortArray_G3 = sorted(arrayGame3[CountArray_3])
                lenData_G3 = sortArray_G3
                lengthCut_3 = len(lenData_G3)*0.025
                
                if "." in str(lengthCut_3):
                    Onepoint_3 = '%.2f'%(lengthCut_3)
                    Backpoint = str(Onepoint_3).split(".")[-1]

                    if int(Backpoint) >= 5 :
                        Cut_G3 = math.ceil(float(lengthCut_3))
                    else:
                        Cut_G3 = math.floor(float(lengthCut_3))
                    
                    if Cut_G3 == 0 :
                        continue
                    else:
                        for removeData_G3 in range(Cut_G3):
                            arrayGame3[CountArray_3].remove(sortArray_G3[removeData_G3])
                            arrayGame3[CountArray_3].remove(sortArray_G3[(removeData_G3+1)*-1])
        
        for AVG_G3 in range(len(arrayGame3)):
     
            AVG_Score_G3 = '%.1f'%(sum(arrayGame3[AVG_G3])/len(arrayGame3[AVG_G3]))

            AVG_Array3.append(AVG_Score_G3)



    return jsonify({'ChartDataGame3':DatachartGame3,'AVGGame3':AVG_Array3,'Label_G3':labels_G3})

@app.route("/Logout")
def Logout():
    session.clear()
    return redirect(url_for('Login'))

if __name__ == "__main__":
    #asdasd
    app.run(debug=True)

