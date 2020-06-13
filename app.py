from flask import Flask, render_template, request, url_for,session, redirect


import pyrebase
import Calculat as Cal

config = {
    "apiKey": "AIzaSyAJ0CmanmUEWcn-Of-OdbdOERhXxOXsTB8",
    "authDomain": "project-e54fe.firebaseapp.com",
    "databaseURL": "https://project-e54fe.firebaseio.com",
    "projectId": "project-e54fe",
    "storageBucket": "project-e54fe.appspot.com",
    "messagingSenderId": "539702287057",
    "appId": "1:539702287057:web:969f76c2ab05a0051843f0",
    "measurementId": "G-X6XZJ3QC44"
}


fierbase = pyrebase.initialize_app(config)
db = fierbase.database()

nook = "sanook"
za = {'Firstname': 'asasdasd'}


# # check = nook in z

all_users = db.child("Member/sanook/").get()
for user in all_users.each():
    # x = za in user.val()
    # print(x)
    # print(user.key()) # Morty
    print(user.val())


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

        countDataQuiz = str(len(db.child("Quiz").get().val())+1)
        Insert = {'Subject':subject,'QuizName':Propo,'Ch1':choice1,'Ch2':choice2,'Ch3':choice3,'Ch4':choice4,'Answer':Answer,'Time':Avgtime,'NO':countDataQuiz}
        
        result = db.child("Quiz/").push(Insert)

        return redirect(url_for('hello'))


@app.route("/AddMember")
def PageAddMem():
    return render_template('AddMember.html')

@app.route("/insertMember", methods=['GET','POST'])
def insertMember():
    if request.method == "POST":
        fname = request.form['Fname']
        lname = request.form['Lname']
        ProSub = request.form['ProSubject']
        password = request.form['Password']
        Conpass = request.form['ComPass']
        email = request.form['Email']
        tel = request.form['Tel']
        username = request.form['Username']

        Insert = {'Firstname':fname,'Lname':lname,'ProSubject':ProSub,'Password':password,'ConfirmPass':Conpass,'Email':email,'Tel':tel, 'Username':username}
        execute = db.push('Member/'+username,Insert)
        return redirect(url_for('PageAddMem'))

@app.route("/Login")
def Login():
    return render_template('Login.html')

@app.route("/CheckLogin", methods=['GET','POST'])
def CheckLogin():

    email = request.form['Username']
    password = request.form['password']


 
  
if __name__ == "__main__":
    app.run(debug=True)