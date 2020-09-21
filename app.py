from flask import Flask, render_template, request, url_for, redirect, session, jsonify
import math
# import pyrebase
from firebase import Firebase
import Calculat as Cal
from array import *



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
                    # print(session['User'])
                    # print('Go to Page Home')
                return redirect(url_for("Home"))
            else:
                ErrorPass = "Password Error check password please !"
                return render_template('Login.html' , ErrorPass = ErrorPass)
        else:
            ErrorUsername = "Username Error check Username please !"
            return render_template('Login.html' , ErrorUser = ErrorUsername)
    return redirect(url_for('Login'))



@app.route("/Register", methods=['GET','POST'])
def Register():
    if request.method == 'POST':

        Username = request.form['Username']
        Pass = request.form['Password']
        Co_pass = request.form['Con_Pass']
        Email = request.form['Email']
        Sub = request.form.getlist('Sub[]')

        CheckMember = db.child('Admin').get().val()

            # การเช็คว่า มี Username ซ้ำ
        if Username in CheckMember :
            Usernamerepea = "Already have a user account"
            return render_template('Login.html' , Usernamerepea = Usernamerepea)
        else:
            db.child("Admin").child(Username).set({"Username":Username,"Password":Pass,"Co_Pass": Co_pass,"Email":Email})

                # การบันทึก Subject หลายๆค่า หรือค่าเดียว
            if (len(Sub) == 1 ):
                db.child("Admin").child(Username).child("Subject_pro").child(Sub[0]).set({"Sub_name":Sub[0],"DataNum":"0"})
            else:
                for i in range(len(Sub)) :
                    db.child("Admin").child(Username).child("Subject_pro").child(Sub[i]).set({"Sub_name":Sub[i],"DataNum":"0"})
                session['Admin'] = Username
                return redirect(url_for('Home'))


@app.route("/Home")
def Home():
    if session.get('Admin') == None:
        return redirect(url_for('Login'))
    else:
        IDAdmin = session['Admin']
        Admin_Subject = db.child('Admin').child(IDAdmin).child('Subject_pro').get()
        return render_template('Home.html',name = IDAdmin ,DataSubject = Admin_Subject)

@app.route("/Home_TH")
def Home_TH():
    if session.get('Admin') == None:
        return redirect(url_for('Login'))
    else:
        IDAdmin = session['Admin']
        Admin_Subject = db.child('Admin').child(IDAdmin).child('Subject_pro').get()
        return render_template('Home_TH.html',name = IDAdmin ,DataSubject = Admin_Subject)
        
@app.route("/Addchoice") #URL
def hello():
    if session.get('Admin') == None:
        return redirect(url_for('Login'))
    else:
        IDAdmin = session['Admin']
        Sub = db.child('Admin').child(IDAdmin).child('Subject_pro').get()
        Admin_Subject = db.child('Admin').child(IDAdmin).child('Subject_pro').get()
        return render_template('Addchoice.html', data = Sub,DataSubject = Admin_Subject)

@app.route("/Addchoice_TH") #URL
def Addchoice_TH():
    if session.get('Admin') == None:
        return redirect(url_for('Login'))
    else:
        IDAdmin = session['Admin']
        Sub = db.child('Admin').child(IDAdmin).child('Subject_pro').get()
        Admin_Subject = db.child('Admin').child(IDAdmin).child('Subject_pro').get()
        return render_template('Addchoice_TH.html', data = Sub,DataSubject = Admin_Subject)

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
        
        checkdata = db.child(subject).get().val()
        # checkdata = db.child("Subject").child(subject).child("Quiz").get().val()
        
        if checkdata == None:
            db.child(subject).child("NO1").set({'subject':subject,'Qu':Propo,'C1':choice1,'C2':choice2,'C3':choice3,'C4':choice4,'ans':Answer,'Time':Avgtime,'ID':'1'})
            # db.child("Subject").child(subject).child("Quiz").child("NO_1").set({'subject':subject,'Qu':Propo,'C1':choice1,'C2':choice2,'C3':choice3,'C4':choice4,'ans':Answer,'Time':Avgtime,'ID':'1'})
            db.child("Admin").child(user).child("Subject_pro").child(subject).set({'DataNum':'1','Sub_name':subject})
        else:
            countDataQuiz = str(len(db.child(subject).get().val())+1)
            db.child(subject).child('NO'+countDataQuiz).set({'subject':subject,'Qu':Propo,'C1':choice1,'C2':choice2,'C3':choice3,'C4':choice4,'ans':Answer,'Time':Avgtime,'ID':countDataQuiz})
            db.child("Admin").child(user).child("Subject_pro").child(subject).set({'DataNum':countDataQuiz,'Sub_name':subject})
        return redirect(url_for('hello'))

@app.route("/Subject", methods=['GET','POST'])
def Subject():
    if session.get('Admin') == None:
        return redirect(url_for('Login'))
    else:
        user = session['Admin']
        Detil = db.child('Admin').child(user).child('Subject_pro').get()
        Admin_Subject = db.child('Admin').child(user).child('Subject_pro').get()
        if request.method == 'POST':
            Sub_name = request.form['Subname']
            session['Subname_Update'] = Sub_name

            ShowSub = db.child(Sub_name).get()
            if ShowSub.val() == None :
                textError = "None"
                return render_template('Subject.html',data = Detil,Show = ShowSub ,Headtext = Sub_name,DataSubject = Admin_Subject , NoneData = textError)
            else:
                textHave = "haveData"
                return render_template('Subject.html',data = Detil,Show = ShowSub ,Headtext = Sub_name,DataSubject = Admin_Subject , haveData = textHave)

        return render_template('Subject.html',data = Detil,DataSubject = Admin_Subject)

@app.route("/Subject_TH", methods=['GET','POST'])
def Subject_TH():
    if session.get('Admin') == None:
        return redirect(url_for('Login'))
    else:
        user = session['Admin']
        Detil = db.child('Admin').child(user).child('Subject_pro').get()
        Admin_Subject = db.child('Admin').child(user).child('Subject_pro').get()
        if request.method == 'POST':
            Sub_name = request.form['Subname']
            session['Subname_Update'] = Sub_name

            ShowSub = db.child(Sub_name).get()
            if ShowSub.val() == None :
                textError = "None"
                return render_template('Subject_TH.html',data = Detil,Show = ShowSub ,Headtext = Sub_name,DataSubject = Admin_Subject , NoneData = textError)
            else:
                textHave = "haveData"
                return render_template('Subject_TH.html',data = Detil,Show = ShowSub ,Headtext = Sub_name,DataSubject = Admin_Subject , haveData = textHave)

        return render_template('Subject_TH.html',data = Detil,DataSubject = Admin_Subject)

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
            db.child(Subname).child('NO'+NO_Sub).update({"Qu":Quiz,"C1":C1,"C2":C2,"C3":C3,"C4":C4,"ans":Answer,"Time":AvgUpdate})
        elif TypeUp == 'Delete':
            db.child(Subname).child('NO'+NO_Sub).remove()
            try:
                countDataQuiz = str(len(db.child(Subname).get().val()))
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
                    return render_template('evo.html',Subject = ShowSubject , ErrorA = ErrorText ,DataSubject = Admin_Subject)
                else:
                    
                    return render_template('evo.html',Subject = ShowSubject , ShowData = SubMem,DataSubject = Admin_Subject ,SubjectName = Sub) 

        return render_template('evo.html', Subject = ShowSubject,DataSubject = Admin_Subject)

@app.route("/Evopage_TH", methods=['GET','POST'])
def Evopage_TH():
    if session.get('Admin') == None:
        return redirect(url_for('Login'))
    else:
        user = session['Admin']
        ShowSubject = db.child('Admin').child(user).child('Subject_pro').get()
        Admin_Subject = db.child('Admin').child(user).child('Subject_pro').get()

        if request.method == 'POST':
            Sub = request.form['Sub_name']
            SubMem = db.child('Subject').child(Sub).child('Member').get()

            session['SubjectRef'] = Sub
            if SubMem.val() == None:
                ErrorText = "ยังไม่มีผู้เล่นในรายวิชานี้"
                return render_template('evo_TH.html',Subject = ShowSubject , ErrorA = ErrorText ,DataSubject = Admin_Subject)
            else:
                
                return render_template('evo_TH.html',Subject = ShowSubject , ShowData = SubMem,DataSubject = Admin_Subject ,SubjectName = Sub) 

        return render_template('evo_TH.html', Subject = ShowSubject,DataSubject = Admin_Subject)

@app.route("/ShowEvo", methods=['GET','POST'])
def ShowEvo():
    if session.get('Admin') == None:
        return redirect(url_for('Login'))
    else:
        SubRef = session['SubjectRef']
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
        return render_template('ShowEvo.html', SubName = SubRef, NAME = session['NameMember'] , email = session['Email'], ShowData = ShowMem ,DataSubject = Admin_Subject)

@app.route("/ShowEvo_TH", methods=['GET','POST'])
def ShowEvo_TH():
    if session.get('Admin') == None:
        return redirect(url_for('Login'))
    else:
        SubRef = session['SubjectRef']
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
        return render_template('ShowEvo_TH.html', SubName = SubRef, NAME = session['NameMember'] , email = session['Email'], ShowData = ShowMem ,DataSubject = Admin_Subject)

@app.route("/ShowEvoAlpha", methods=['GET','POST'])
def ShowEvoAlpha():
    if session.get('Admin') == None:
        return redirect(url_for('Login'))
    else:
        Admin_Subject = db.child('Admin').child(session['Admin']).child('Subject_pro').get()
        ShowMem = db.child('IntroGame').child('Alphabet').get()
        if request.method == 'POST':
            Member = request.form['Username']
            session['Member'] = Member
            DataUser = db.child('IntroGame').child('Alphabet').child(session['Member']).get()
            Name = DataUser.val()['Name']
            Email = DataUser.val()['Email']
            session['NameMember'] = Name
            session['Email'] = Email

        return render_template('ShowEvoAlpha.html', NAME = session['NameMember'] , email = session['Email'], ShowData = ShowMem ,DataSubject = Admin_Subject)
@app.route("/ShowEvoAlpha_TH", methods=['GET','POST'])
def ShowEvoAlpha_TH():
    if session.get('Admin') == None:
        return redirect(url_for('Login'))
    else:
        Admin_Subject = db.child('Admin').child(session['Admin']).child('Subject_pro').get()
        ShowMem = db.child('IntroGame').child('Alphabet').get()
        if request.method == 'POST':
            Member = request.form['Username']
            session['Member'] = Member
            DataUser = db.child('IntroGame').child('Alphabet').child(session['Member']).get()
            Name = DataUser.val()['Name']
            Email = DataUser.val()['Email']
            session['NameMember'] = Name
            session['Email'] = Email

        return render_template('ShowEvoAlpha_TH.html', NAME = session['NameMember'] , email = session['Email'], ShowData = ShowMem ,DataSubject = Admin_Subject)

@app.route("/ShowEvoShoot", methods=['GET','POST'])
def ShowEvoShoot():
    if session.get('Admin') == None:
        return redirect(url_for('Login'))
    else:
        Admin_Subject = db.child('Admin').child(session['Admin']).child('Subject_pro').get()
        ShowMem = db.child('IntroGame').child('ShootGame').get()
        if request.method == 'POST':
            Member = request.form['Username']
            session['Member'] = Member
            DataUser = db.child('IntroGame').child('ShootGame').child(session['Member']).get()
            Name = DataUser.val()['Name']
            Email = DataUser.val()['Email']
            session['NameMember'] = Name
            session['Email'] = Email

        return render_template('ShowEvoShootGame.html', NAME = session['NameMember'] , email = session['Email'], ShowData = ShowMem ,DataSubject = Admin_Subject)

@app.route("/ShowEvoShoot_TH", methods=['GET','POST'])
def ShowEvoShoot_TH():
    if session.get('Admin') == None:
        return redirect(url_for('Login'))
    else:
        Admin_Subject = db.child('Admin').child(session['Admin']).child('Subject_pro').get()
        ShowMem = db.child('IntroGame').child('ShootGame').get()
        if request.method == 'POST':
            Member = request.form['Username']
            session['Member'] = Member
            DataUser = db.child('IntroGame').child('ShootGame').child(session['Member']).get()
            Name = DataUser.val()['Name']
            Email = DataUser.val()['Email']
            session['NameMember'] = Name
            session['Email'] = Email

        return render_template('ShowEvoShoot_TH.html', NAME = session['NameMember'] , email = session['Email'], ShowData = ShowMem ,DataSubject = Admin_Subject)

@app.route("/Evoindex", methods=['GET','POST'])
def Evoindex():
    if session.get('Admin') == None:
        return redirect(url_for('Login'))
    else:
        IDAdmin = session['Admin']
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
        return render_template('evoindex.html',DataSubject = Admin_Subject)

@app.route("/Evoalpha", methods=['GET','POST'])
def Evoalpha():
    if session.get('Admin') == None:
        return redirect(url_for('Login'))
    else:
        IDAdmin = session['Admin']
        Sub = db.child('Admin').child(IDAdmin).child('Subject_pro').get()
        Admin_Subject = db.child('Admin').child(IDAdmin).child('Subject_pro').get()
        mainGameAlpha = db.child('IntroGame').child('Alphabet').get()
        if mainGameAlpha.val() == None:
            error = 'ไม่มีผู้เล่น'
            return render_template('evoalpha.html',DataSubject = Admin_Subject,error = error)
        else:
            havedata ='มีผู้เล่น'
            return render_template('evoalpha.html',DataSubject = Admin_Subject,havedata = havedata,mainGameAlpha = mainGameAlpha)

@app.route("/Evoalpha_TH", methods=['GET','POST'])
def Evoalpha_TH():
    if session.get('Admin') == None:
        return redirect(url_for('Login'))
    else:
        IDAdmin = session['Admin']
        Sub = db.child('Admin').child(IDAdmin).child('Subject_pro').get()
        Admin_Subject = db.child('Admin').child(IDAdmin).child('Subject_pro').get()
        mainGameAlpha = db.child('IntroGame').child('Alphabet').get()
        if mainGameAlpha.val() == None:
            error = 'ไม่มีผู้เล่น'
            return render_template('evoalpha_TH.html',DataSubject = Admin_Subject,error = error)
        else:
            havedata ='มีผู้เล่น'
            return render_template('evoalpha_TH.html',DataSubject = Admin_Subject,havedata = havedata,mainGameAlpha = mainGameAlpha)


@app.route("/Evoshoot", methods=['GET','POST'])
def Evoshoot():
    if session.get('Admin') == None:
        return redirect(url_for('Login'))
    else:
        IDAdmin = session['Admin']
        Sub = db.child('Admin').child(IDAdmin).child('Subject_pro').get()
        Admin_Subject = db.child('Admin').child(IDAdmin).child('Subject_pro').get()
        mainGameShoot= db.child('IntroGame').child('ShootGame').get()
        if mainGameShoot.val() == None:
            error = 'ไม่มีผู้เล่น'
            return render_template('evoshoot.html',DataSubject = Admin_Subject,error = error)
        else:
            havedata ='มีผู้เล่น'
            return render_template('evoshoot.html',DataSubject = Admin_Subject,havedata = havedata,mainGameShoot = mainGameShoot)
@app.route("/Evoshoot_TH", methods=['GET','POST'])
def Evoshoot_TH():
    if session.get('Admin') == None:
        return redirect(url_for('Login'))
    else:
        IDAdmin = session['Admin']
        Sub = db.child('Admin').child(IDAdmin).child('Subject_pro').get()
        Admin_Subject = db.child('Admin').child(IDAdmin).child('Subject_pro').get()
        mainGameShoot= db.child('IntroGame').child('ShootGame').get()
        if mainGameShoot.val() == None:
            error = 'ไม่มีผู้เล่น'
            return render_template('evoshoot_TH.html',DataSubject = Admin_Subject,error = error)
        else:
            havedata ='มีผู้เล่น'
            return render_template('evoshoot_TH.html',DataSubject = Admin_Subject,havedata = havedata,mainGameShoot = mainGameShoot)

@app.route("/Evoindex_TH", methods=['GET','POST'])
def Evoindex_TH():
    if session.get('Admin') == None:
        return redirect(url_for('Login'))
    else:
        IDAdmin = session['Admin']
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
        return render_template('evoindex_TH.html',DataSubject = Admin_Subject)


@app.route("/DeleteSub_allPage", methods=['GET','POST'])
def DeleteSub_allPage():
    Admin = session['Admin']
    if request.method == 'POST':
        Sub_Before = request.form['Subject_Befor']
        db.child('Admin').child(Admin).child('Subject_pro').child(Sub_Before).remove()
        db.child('Subject').child(Sub_Before).remove()

    return redirect(url_for('Home'))

@app.route("/AddSub_allPage", methods=['GET','POST'])
def AddSub_allPage():
    Admin = session['Admin']
    Admin_Subject = db.child('Admin').child(Admin).child('Subject_pro').get()
    if request.method == 'POST':
        AddSub = request.form.getlist('Sub[]')
        Subindata = "มีอยู่แล้วในฐานข้อมูล"
        for i in range(len(AddSub)) :
            CheckSubject = db.child('Admin').child(Admin).child("Subject_pro").get()
            if AddSub[i] in CheckSubject.val():
                SubError = "วิชา : "+AddSub[i]+" "+Subindata
                return render_template('Home.html',name = Admin ,DataSubject = Admin_Subject, ErrorSub = SubError)
            else:
                db.child("Admin").child(Admin).child("Subject_pro").child(AddSub[i]).set({"Sub_name":AddSub[i],"DataNum":"0"})

    return redirect(url_for('Home'))

@app.route("/ChangePass_allPage", methods=['GET','POST'])
def ChangePass_allPage():
    Admin = session['Admin']
    Admin_Subject = db.child('Admin').child(Admin).child('Subject_pro').get()
    if request.method == 'POST':
        Pass_Be = request.form['Pass_Before']
        Pass_Af = request.form['Pass_After'] 
        Pass_co = request.form['CoPass_After']
        Data = db.child('Admin').child(Admin).get()
        if Data.val()['Password'] == Pass_Be:
            db.child('Admin').child(Admin).update({"Password":Pass_Af,"Co_Pass":Pass_co})
            SuccessPass = "Success"
            return render_template('Home.html',name = Admin ,DataSubject = Admin_Subject, SuccessPass = SuccessPass)
        else:
            ChangeError = "รหัสผ่านผิด"
            return render_template('Home.html',name = Admin ,DataSubject = Admin_Subject, Error = ChangeError)

    return redirect(url_for('Home'))

@app.route("/dataChart")
def DataChart():
    Member = session['Member']

    SubjectRef = session['SubjectRef']
    DataRefGame1 = db.child('IntroGame').child('Alphabet').child(Member).child('score').get()
    DataRefGame2 = db.child('IntroGame').child('ShootGame').child(Member).child('score').get()
    DataRefGame3 = db.child('Subject').child(SubjectRef).child('Member').child(Member).child('AdventuresGame').get()

        # Chart Member main 
    DatachartGame1 = ['0']
    DatachartGame2 = ['0']
    DatachartGame3 = ['0']

    # Sub_NameMem = db.child('Subject').child(SubjectRef).child('Member').child(Member).get()
    # NameMember = Sub_NameMem.val()['Name']
    if DataRefGame1.val() == None:
        DatachartGame1 = ['0']
    else:
        for G1 in DataRefGame1.each():
            
            DatachartGame1.append(G1.val()['score'])
    if DataRefGame2.val() == None:
        DatachartGame2 = ['0']
    else:
        for G2 in DataRefGame2.each():
            DatachartGame2.append(G2.val()['score'])
    if DataRefGame3.val() == None:
        DatachartGame3 = ['0']
    else:
        for G3 in DataRefGame3.each():
            
            DatachartGame3.append(G3.val()['score'])

    arrayGame1 = []
    AVG_Array = ['0',]
    arrayGame2 = []
    AVG_Array2 = ['0',]
    arrayGame3 = []
    AVG_Array3 = ['0',]

    labels_G1 = ['0','1','2']
    labels_G2 = ['0','1','2']
    labels_G3 = ['0','1','2']

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
                    arrayGame1[posi_arr_1].append(Score_in_Game_1.val()['score'])
                except:
                    continue
                posi_arr_1 += 1


        ValBeeteew = 10
        for Data_Game1 in range(len(arrayGame1)):
            countCheckData_G1 = len(arrayGame1[Data_Game1])
            if countCheckData_G1 <= 2:
                continue
            else :
                Xi = (len(arrayGame1[Data_Game1])+1)/2
                datasort = sorted(arrayGame1[Data_Game1])

                if "." in str(Xi):
                    ValDina = str(Xi).split(".")[-1]
                    if ValDina == '0':
                        mid =  datasort[int(Xi-1)]
                        # print(mid)
                        # print(datasort)
                        for test in range(len(datasort)):
                            # print(datasort[test])
                            if datasort[test] > (mid-ValBeeteew) and datasort[test] <= (mid+ValBeeteew):
                                # print(str(datasort[test]) +'อยู่ในช่วง')
                                continue
                            else :
                                arrayGame1[Data_Game1].remove(datasort[test])
                                # print(str(datasort[test]) +'ไม่อยู่ในช่วง'+str(mid-10)+"และ"+str(mid+10))
                elif ValDina == '5':
                    XiMax = math.ceil(Xi)
                    Ximin = math.floor(Xi)
                    median = (datasort[Ximin-1]+datasort[XiMax-1])/2
                    for Posi in range(len(datasort)):
                        # print(datasort[Posi])
                        if datasort[Posi] > (median-ValBeeteew) and datasort[Posi] <= (median+ValBeeteew):
                            # print(str(datasort[Posi]) +'อยู่ในช่วง')
                            continue
                        else :
                            arrayGame3[Data_Game1].remove(datasort[Posi])

        for AVG in range(len(arrayGame1)):
            AVG_Score = '%.1f'%(sum(arrayGame1[AVG])/len(arrayGame1[AVG]))
    
            AVG_Array.append(AVG_Score)

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

        #การหาค่ามัธยฐาน
        ValBeeteew = 10
        for Data_Game2 in range(len(arrayGame2)):
            countCheckData_G2 = len(arrayGame2[Data_Game2])
            if countCheckData_G2 <= 2:
                continue
            else :
                Xi = (len(arrayGame3[Data_Game2])+1)/2
                datasort = sorted(arrayGame3[Data_Game2])

                if "." in str(Xi):
                    ValDina = str(Xi).split(".")[-1]
                    if ValDina == '0':
                        mid =  datasort[int(Xi-1)]
                        # print(mid)
                        # print(datasort)
                        for test in range(len(datasort)):
                            # print(datasort[test])
                            if datasort[test] > (mid-ValBeeteew) and datasort[test] <= (mid+ValBeeteew):
                                # print(str(datasort[test]) +'อยู่ในช่วง')
                                continue
                            else :
                                arrayGame2[Data_Game2].remove(datasort[test])
                                # print(str(datasort[test]) +'ไม่อยู่ในช่วง'+str(mid-10)+"และ"+str(mid+10))
                elif ValDina == '5':
                    XiMax = math.ceil(Xi)
                    Ximin = math.floor(Xi)
                    median = (datasort[Ximin-1]+datasort[XiMax-1])/2
                    for Posi in range(len(datasort)):
                        # print(datasort[Posi])
                        if datasort[Posi] > (median-ValBeeteew) and datasort[Posi] <= (median+ValBeeteew):
                            # print(str(datasort[Posi]) +'อยู่ในช่วง')
                            continue
                        else :
                            arrayGame2[Data_Game2].remove(datasort[Posi])

        for AVG_G2 in range(len(arrayGame2)):
            AVG_Score_G2 = '%.1f'%(sum(arrayGame2[AVG_G2])/len(arrayGame2[AVG_G2]))

            AVG_Array2.append(AVG_Score_G2)


    # การหาคนที่ 3

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


        # การหาค่ามัธยฐาน
        ValBeeteew = 10
        for Data_Game3 in range(len(arrayGame3)):
            countCheckData_G3 = len(arrayGame3[Data_Game3])
            if countCheckData_G3 <= 2:
                continue
            else :
                Xi = (len(arrayGame3[Data_Game3])+1)/2
                datasort = sorted(arrayGame3[Data_Game3])

                if "." in str(Xi):
                    ValDina = str(Xi).split(".")[-1]
                    if ValDina == '0':
                        mid =  datasort[int(Xi-1)]
                        # print(mid)
                        # print(datasort)
                        for test in range(len(datasort)):
                            # print(datasort[test])
                            if datasort[test] > (mid-ValBeeteew) and datasort[test] <= (mid+ValBeeteew):
                                
                                continue
                            else :
                                arrayGame3[Data_Game3].remove(datasort[test])
                                # print(str(datasort[test]) +'ไม่อยู่ในช่วง'+str(mid-10)+"และ"+str(mid+10))
                elif ValDina == '5':
                    XiMax = math.ceil(Xi)
                    Ximin = math.floor(Xi)
                    median = (datasort[Ximin-1]+datasort[XiMax-1])/2
                    for Posi in range(len(datasort)):
                        # print(datasort[Posi])
                        if datasort[Posi] > (median-ValBeeteew) and datasort[Posi] <= (median+ValBeeteew):
                            
                            continue
                        else :
                            arrayGame3[Data_Game3].remove(datasort[Posi])


        for AVG_G3 in range(len(arrayGame3)):
            AVG_Score_G3 = '%.1f'%(sum(arrayGame3[AVG_G3])/len(arrayGame3[AVG_G3]))

            AVG_Array3.append(AVG_Score_G3)


    return jsonify({'ChartDataGame1':DatachartGame1,'ChartDataGame2':DatachartGame2,'ChartDataGame3':DatachartGame3,'AVGGame1':AVG_Array,'AVGGame2':AVG_Array2,'AVGGame3':AVG_Array3
    ,'Label_G3':labels_G3,'Label_G2':labels_G2,'Label_G1':labels_G1})

@app.route("/Logout")
def Logout():
    session.clear()
    return redirect(url_for('Login'))

if __name__ == "__main__":
    app.run(debug=True)

