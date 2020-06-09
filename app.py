from flask import *
# import pymysql.cursors

from firebase import firebase
import Calculat as Cal

# URL Project #
url = "https://project-e54fe.firebaseio.com/" 
# ตัวกำการเชื่อมกับ Firebase #
firebase = firebase.FirebaseApplication(url, authentication = None)


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

        if Answer == 'Answer1':
            Answer = choice1
        elif Answer == 'Answer2':
            Answer = choice2
        elif Answer == 'Answer3':
            Answer = choice3
        elif Answer == 'Answer4':
            Answer = choice4

        Avgtime = Cal.Calchoice(Answer)

        # countDataQuiz = str(len(firebase.get('/Quiz', None))+1)
        Insert = {'Subject':subject,'QuizName':Propo,'Ch1':choice1,'Ch2':choice2,'Ch3':choice3,'Ch4':choice4,'Answer':Answer,'Time':Avgtime}

        # result = firebase.post('Quiz/'+countDataQuiz,Insert)
        result = firebase.post('Quiz/',Insert)

        return render_template('Addchoice.html')

@app.route("/AddMember")
def PageAddMem():
    return render_template('AddMember.html')

@app.route("/insertMember", methods=['GET','POST'])
def insertMember():
    if request.method == "POST":
        fname = request.form['Fname']
        lname = request.form['Lname']
        ProSub = request.form['ProSubject']
        Username = request.form['Username']
        password = request.form['Password']
        Conpass = request.form['ComPass']
        email = request.form['Email']
        tel = request.form['Tel']

        Insert = {'Firstname':fname,'Lname':lname,'ProSubject':ProSub,'Username':Username,
        'Password':password,'ConfirmPass':Conpass,'Email':email,'Tel':tel}

        execute = firebase.post('Member/',Insert)

        return render_template('AddMember.html')

if __name__ == "__main__":
    app.run(debug=True)