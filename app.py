from flask import Flask, render_template, request, url_for, redirect, session, jsonify

# import pyrebase
from firebase import Firebase
import Calculat as Cal
from array import *

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


# arrayTest = []
# AVG_Array = []
# # คนที่ส่งเข้ามา
# KeyMemname = db.child('Subject').child('Anatome').child('Member').child('Luner').child('TypeGame').child('Game1').get()
# for len_Score in KeyMemname.val():

#     lenScore = [len_Score]
#     arrayTest.append(lenScore)

# # คนที่เล่นเกมนั้นทั้งหมด
# datatest = db.child('Subject').child('Anatome').child('Member')
# for NameMem in datatest.get().val():

#     dataScore = db.child('Subject').child('Anatome').child('Member').child(NameMem).child('TypeGame').child('Game1').get()

#     for Score_test in KeyMemname.val():

#         try:
#             Score = dataScore.val()[Score_test]
#         except :
#             Score = 0

#         # การเพิ่มค่าเข้าไปใน array
#         for i in range(len(arrayTest)):
#             if Score_test in arrayTest[i]:
#                 # print("ทำการเพิ่ม "+str(Score) +' เข้าไปใน array ช่อง '+str(i))
#                 arrayTest[i].append(Score)
#             # else:
#                 # print(str(Score) +'ไม่อยู่ใน array ช่อง'+ str(i))

# # remove Key Score in array
# for Re_Score_test in KeyMemname.val():

#     for ReKey in range(len(arrayTest)):
#         if Re_Score_test in arrayTest[ReKey]:
#             # print(Re_Score_test+"พบ อยู่ใน array..................................")
#             arrayTest[ReKey].remove(Re_Score_test)
#         # else:
#         #     print("ไม่พบ อยู่ใน array")
                
# for AVG in range(len(arrayTest)):
#     AVG_Score = '%.1f'%(sum(arrayTest[AVG])/len(arrayTest[AVG]))
#     print(AVG_Score)
#     AVG_Array.append(AVG_Score)
# print(AVG_Array)




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
        
@app.route("/Addchoice") #URL
def hello():
    if session.get('Admin') == None:
        return redirect(url_for('Login'))
    else:
        IDAdmin = session['Admin']
        Sub = db.child('Admin').child(IDAdmin).child('Subject_pro').get()
        Admin_Subject = db.child('Admin').child(IDAdmin).child('Subject_pro').get()
        return render_template('Addchoice.html', data = Sub,DataSubject = Admin_Subject)

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
        
        checkdata = db.child("Subject").child(subject).child("Quiz").get().val()
        
        if checkdata == None:
            db.child("Subject").child(subject).child("Quiz").child("NO_1").set({'subject':subject,'Qu':Propo,'C1':choice1,'C2':choice2,'C3':choice3,'C4':choice4,'ans':Answer,'Time':Avgtime,'ID':'1'})
            db.child("Admin").child(user).child("Subject_pro").child(subject).set({'DataNum':'1','Sub_name':subject})
        else:
            countDataQuiz = str(len(db.child("Subject").child(subject).child("Quiz").get().val())+1)
            db.child("Subject").child(subject).child("Quiz").child("NO_"+countDataQuiz).set({'subject':subject,'Qu':Propo,'C1':choice1,'C2':choice2,'C3':choice3,'C4':choice4,'ans':Answer,'Time':Avgtime,'ID':countDataQuiz})
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

            ShowSub = db.child('Subject').child(Sub_name).child('Quiz').get()
            if ShowSub.val() == None :
                textError = "None"
                return render_template('Subject.html',data = Detil,Show = ShowSub ,Headtext = Sub_name,DataSubject = Admin_Subject , NoneData = textError)
            else:
                textHave = "haveData"
                return render_template('Subject.html',data = Detil,Show = ShowSub ,Headtext = Sub_name,DataSubject = Admin_Subject , haveData = textHave)

        return render_template('Subject.html',data = Detil,DataSubject = Admin_Subject)

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
        Answer = request.form['Answer']
        if(Answer == '1'):
            Answer = C1
        elif(Answer == '2'):
            Answer = C2
        elif(Answer == '3'):
            Answer = C3
        elif(Answer == '4'):
            Answer = C4

        
        TypeUp = request.form['Type_Up']

        if TypeUp == 'Edit':
            AvgUpdate = Cal.Calchoice(Answer)
            db.child('Subject').child(Subname).child('Quiz').child('NO_'+NO_Sub).update({"Qu":Quiz,"C1":C1,"C2":C2,"C3":C3,"C4":C4,"ans":Answer,"Time":AvgUpdate})
        elif TypeUp == 'Delete':

            db.child('Subject').child(Subname).child('Quiz').child('NO_'+NO_Sub).remove()
            countDataQuiz = str(len(db.child("Subject").child(Subname).child("Quiz").get().val()))
            db.child('Admin').child(user).child('Subject_pro').child(Subname).update({"DataNum":countDataQuiz})

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
            SubMem = db.child('Subject').child(Sub).child('Member').get()

            session['SubjectRef'] = Sub
            if SubMem.val() == None:
                ErrorText = "ยังไม่มีผู้เล่นในรายวิชานี้"
                return render_template('evo.html',Subject = ShowSubject , ErrorA = ErrorText ,DataSubject = Admin_Subject)
            else:
                
                return render_template('evo.html',Subject = ShowSubject , ShowData = SubMem,DataSubject = Admin_Subject ,SubjectName = Sub) 

        return render_template('evo.html', Subject = ShowSubject,DataSubject = Admin_Subject)



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
            Stu_Code = DataUser.val()['Stu_Code']

            session['NameMember'] = Name
            session['StuCode'] = Stu_Code
        return render_template('ShowEvo.html', SubName = SubRef, NAME = session['NameMember'] , StuCode = session['StuCode'], ShowData = ShowMem ,DataSubject = Admin_Subject)



@app.route("/dataChart")
def DataChart():
    Member = session['Member']

    SubjectRef = session['SubjectRef']
    DataRefGame1 = db.child('Subject').child(SubjectRef).child('Member').child(Member).child('TypeGame').child('Game1').get()
    DataRefGame2 = db.child('Subject').child(SubjectRef).child('Member').child(Member).child('TypeGame').child('Game2').get()
    DataRefGame3 = db.child('Subject').child(SubjectRef).child('Member').child(Member).child('TypeGame').child('Game3').get()

        # Chart Member main Game1
    DatachartGame1 = ['0',]
    DatachartGame2 = ['0',]
    DatachartGame3 = ['0',]

        # Count = 1
    Sub_NameMem = db.child('Subject').child(SubjectRef).child('Member').child(Member).get()
    NameMember = Sub_NameMem.val()['Name']
    for G1 in DataRefGame1.each():
        DatachartGame1.append(G1.val())
    for G2 in DataRefGame2.each():
        DatachartGame2.append(G2.val())
    for G3 in DataRefGame3.each():
        DatachartGame3.append(G3.val())

    arrayGame1 = []
    AVG_Array = ['0',]
    arrayGame2 = []
    AVG_Array2 = ['0',]
    arrayGame3 = []
    AVG_Array3 = ['0',]

    # การหา AVG ของเกมที่1
    # คนที่ส่งเข้ามา เพื่อที่หาจำนวนครั้งในการเล่น
    for len_Score in DataRefGame1.val():

        lenScore = [len_Score]
        arrayGame1.append(lenScore)

    # คนที่เล่นเกมนั้นทั้งหมด
    MemberSubject1 = db.child('Subject').child(SubjectRef).child('Member')
    for NameMem in MemberSubject1.get().val():
        dataScore = db.child('Subject').child(SubjectRef).child('Member').child(NameMem).child('TypeGame').child('Game1').get()

        for Score_test in DataRefGame1.val():

            try:
                Score = dataScore.val()[Score_test]
            except :
                Score = 0

            # การเพิ่มค่าเข้าไปใน array
            for i in range(len(arrayGame1)):
                if Score_test in arrayGame1[i]:
                    # print("ทำการเพิ่ม "+str(Score) +' เข้าไปใน array ช่อง '+str(i))
                    arrayGame1[i].append(Score)
                # else:
                    # print(str(Score) +'ไม่อยู่ใน array ช่อง'+ str(i))

# remove Key Score in array
    for Re_Score_test in DataRefGame1.val():

        for ReKey in range(len(arrayGame1)):
            if Re_Score_test in arrayGame1[ReKey]:
                # print(Re_Score_test+"พบ อยู่ใน array..................................")
                arrayGame1[ReKey].remove(Re_Score_test)
            # else:
            #     print("ไม่พบ อยู่ใน array")
                    
    for AVG in range(len(arrayGame1)):
        AVG_Score = '%.1f'%(sum(arrayGame1[AVG])/len(arrayGame1[AVG]))
        # print(AVG_Score)
        AVG_Array.append(AVG_Score)


    # การหาคนที่ 2
    for len_Score_Game2 in DataRefGame2.val():
        lenScoreGame2 = [len_Score_Game2]
        arrayGame2.append(lenScoreGame2)

    MemberSubject2 = db.child('Subject').child(SubjectRef).child('Member')
    for NameMem_Game2 in MemberSubject2.get().val():
        dataScore_Game2 = db.child('Subject').child(SubjectRef).child('Member').child(NameMem_Game2).child('TypeGame').child('Game2').get()
        # print(dataScore_Game2.val())
        for Score_Game2 in DataRefGame2.val():
            try:
                Score_G2 = dataScore_Game2.val()[Score_Game2]

            except :
                Score_G2 = 0

            # การเพิ่มค่าเข้าไปใน array
            for i_G2 in range(len(arrayGame2)):
                if Score_Game2 in arrayGame2[i_G2]:

                    arrayGame2[i_G2].append(Score_G2)

# remove Key Score in array
    for Re_Score_G2 in DataRefGame2.val():
        for ReKey_G2 in range(len(arrayGame2)):
            if Re_Score_G2 in arrayGame2[ReKey_G2]:
                arrayGame2[ReKey_G2].remove(Re_Score_G2)

    for AVG_G2 in range(len(arrayGame2)):
        AVG_Score_G2 = '%.1f'%(sum(arrayGame2[AVG_G2])/len(arrayGame2[AVG_G2]))

        AVG_Array2.append(AVG_Score_G2)

    # การหาคนที่ 3
    for len_Score_Game3 in DataRefGame3.val():
        lenScoreGame3 = [len_Score_Game3]
        arrayGame3.append(lenScoreGame3)

    MemberSubject3 = db.child('Subject').child(SubjectRef).child('Member')
    for NameMem_Game3 in MemberSubject3.get().val():
        dataScore_Game3 = db.child('Subject').child(SubjectRef).child('Member').child(NameMem_Game3).child('TypeGame').child('Game3').get()
        # print(dataScore_Game2.val())
        for Score_Game3 in DataRefGame3.val():
            try:
                Score_G3 = dataScore_Game3.val()[Score_Game3]

            except :
                Score_G3 = 0

            # การเพิ่มค่าเข้าไปใน array
            for i_G3 in range(len(arrayGame3)):
                if Score_Game3 in arrayGame3[i_G3]:

                    arrayGame3[i_G3].append(Score_G3)

# remove Key Score in array
    for Re_Score_G3 in DataRefGame3.val():
        for ReKey_G3 in range(len(arrayGame3)):
            if Re_Score_G3 in arrayGame3[ReKey_G3]:
                arrayGame3[ReKey_G3].remove(Re_Score_G3)

    for AVG_G3 in range(len(arrayGame3)):
        AVG_Score_G3 = '%.1f'%(sum(arrayGame3[AVG_G3])/len(arrayGame3[AVG_G3]))

        AVG_Array3.append(AVG_Score_G3)

    return jsonify({'ChartDataGame1':DatachartGame1,'ChartDataGame2':DatachartGame2,'ChartDataGame3':DatachartGame3,'AVGGame1':AVG_Array,'AVGGame2':AVG_Array2,'AVGGame3':AVG_Array3,'NameMem':NameMember})

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
                print(SubError)
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


@app.route("/Logout")
def Logout():
    session.clear()
    return redirect(url_for('Login'))

@app.route("/test")
def test():
    return render_template('test.html')

@app.route("/dataCharttest")
def DataCharttest():

    
    DataRefGame1 = db.child('Subject').child('Anatome').child('Member').child('Luner').child('TypeGame').child('Game1').get()
    DataRefGame2 = db.child('Subject').child('Anatome').child('Member').child('Luner').child('TypeGame').child('Game2').get()
    DataRefGame3 = db.child('Subject').child('Anatome').child('Member').child('Luner').child('TypeGame').child('Game3').get()

        # Chart Member main Game1
    DatachartGame1 = ['0',]
    DatachartGame2 = ['0',]
    DatachartGame3 = ['0',]

        # Count = 1
    Sub_NameMem = db.child('Subject').child('Anatome').child('Member').child('Luner').get()
    NameMember = Sub_NameMem.val()['Name']
    for G1 in DataRefGame1.each():
        DatachartGame1.append(G1.val())
    for G2 in DataRefGame2.each():
        DatachartGame2.append(G2.val())
    for G3 in DataRefGame3.each():
        DatachartGame3.append(G3.val())

    arrayGame1 = []
    AVG_Array = ['0',]
    arrayGame2 = []
    AVG_Array2 = ['0',]
    arrayGame3 = []
    AVG_Array3 = ['0',]

    # การหา AVG ของเกมที่1
    # คนที่ส่งเข้ามา เพื่อที่หาจำนวนครั้งในการเล่น
    for len_Score in DataRefGame1.val():

        lenScore = [len_Score]
        arrayGame1.append(lenScore)

    # คนที่เล่นเกมนั้นทั้งหมด
    MemberSubject1 = db.child('Subject').child('Anatome').child('Member')
    for NameMem in MemberSubject1.get().val():
        dataScore = db.child('Subject').child('Anatome').child('Member').child(NameMem).child('TypeGame').child('Game1').get()

        for Score_test in DataRefGame1.val():

            try:
                Score = dataScore.val()[Score_test]
            except :
                Score = 0

            # การเพิ่มค่าเข้าไปใน array
            for i in range(len(arrayGame1)):
                if Score_test in arrayGame1[i]:
                    # print("ทำการเพิ่ม "+str(Score) +' เข้าไปใน array ช่อง '+str(i))
                    arrayGame1[i].append(Score)
                # else:
                    # print(str(Score) +'ไม่อยู่ใน array ช่อง'+ str(i))

# remove Key Score in array
    for Re_Score_test in DataRefGame1.val():

        for ReKey in range(len(arrayGame1)):
            if Re_Score_test in arrayGame1[ReKey]:
                # print(Re_Score_test+"พบ อยู่ใน array..................................")
                arrayGame1[ReKey].remove(Re_Score_test)
            # else:
            #     print("ไม่พบ อยู่ใน array")
                    
    for AVG in range(len(arrayGame1)):
        AVG_Score = '%.1f'%(sum(arrayGame1[AVG])/len(arrayGame1[AVG]))
        # print(AVG_Score)
        AVG_Array.append(AVG_Score)

    # การหาคนที่ 2
    for len_Score_Game2 in DataRefGame2.val():
        lenScoreGame2 = [len_Score_Game2]
        arrayGame2.append(lenScoreGame2)

    MemberSubject2 = db.child('Subject').child('Anatome').child('Member')
    for NameMem_Game2 in MemberSubject2.get().val():
        dataScore_Game2 = db.child('Subject').child('Anatome').child('Member').child(NameMem_Game2).child('TypeGame').child('Game2').get()

        for Score_Game2 in DataRefGame2.val():
            try:
                Score_G2 = dataScore_Game2.val()[Score_Game2]

            except :
                Score_G2 = 0

            # การเพิ่มค่าเข้าไปใน array
            for i_G2 in range(len(arrayGame2)):
                if Score_Game2 in arrayGame2[i_G2]:

                    arrayGame2[i_G2].append(Score_G2)

# remove Key Score in array
    for Re_Score_G2 in DataRefGame2.val():
        for ReKey_G2 in range(len(arrayGame2)):
            if Re_Score_G2 in arrayGame2[ReKey_G2]:
                arrayGame2[ReKey_G2].remove(Re_Score_G2)

    for AVG_G2 in range(len(arrayGame2)):
        AVG_Score_G2 = '%.1f'%(sum(arrayGame2[AVG_G2])/len(arrayGame2[AVG_G2]))
        AVG_Array2.append(AVG_Score_G2)

    # การหาคนที่ 3
    for len_Score_Game3 in DataRefGame3.val():
        lenScoreGame3 = [len_Score_Game3]
        arrayGame3.append(lenScoreGame3)

    MemberSubject3 = db.child('Subject').child('Anatome').child('Member')
    for NameMem_Game3 in MemberSubject3.get().val():
        dataScore_Game3 = db.child('Subject').child('Anatome').child('Member').child(NameMem_Game3).child('TypeGame').child('Game3').get()
        # print(dataScore_Game2.val())
        for Score_Game3 in DataRefGame3.val():
            try:
                Score_G3 = dataScore_Game3.val()[Score_Game3]
            except :
                Score_G3 = 0

            # การเพิ่มค่าเข้าไปใน array
            for i_G3 in range(len(arrayGame3)):
                if Score_Game3 in arrayGame3[i_G3]:

                    arrayGame3[i_G3].append(Score_G3)

# remove Key Score in array
    for Re_Score_G3 in DataRefGame3.val():
        for ReKey_G3 in range(len(arrayGame3)):
            if Re_Score_G3 in arrayGame3[ReKey_G3]:
                arrayGame3[ReKey_G3].remove(Re_Score_G3)

    for AVG_G3 in range(len(arrayGame3)):
        AVG_Score_G3 = '%.1f'%(sum(arrayGame3[AVG_G3])/len(arrayGame3[AVG_G3]))

        AVG_Array3.append(AVG_Score_G3)

    return jsonify({'ChartDataGame1':DatachartGame1,'ChartDataGame2':DatachartGame2,'ChartDataGame3':DatachartGame3,'AVGGame1':AVG_Array,'AVGGame2':AVG_Array2,'AVGGame3':AVG_Array3,'NameMem':NameMember})


if __name__ == "__main__":
    app.run(debug=True)

