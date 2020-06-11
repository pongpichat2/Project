
function CheckDatanull() {
    var Password = document.forms["AddMember"]["Password"].value;
    var fname = document.forms["AddMember"]["Fname"].value;
    var lname = document.forms["AddMember"]["Lname"].value;
    var Compass = document.forms["AddMember"]["ComPass"].value;
    var email = document.forms["AddMember"]["Email"].value;
    var tel = document.forms["AddMember"]["Tel"].value;
    if (fname == "" || fname == null) {
        alert("กรุณากรอก First ด้วยครับ!! ");
        document.getElementById("Fname").focus();
        return false;
    }
    if (lname == "" || lname == null) {
        alert("กรุณากรอก Lastname ด้วยครับ!! ");
        document.getElementById("Lname").focus();
        return false;
    }

    if (Password == "" || Password == null) {
        alert("กรุณากรอก Password ด้วยครับ!! ");
        document.getElementById("Password").focus();
        return false;
    }
    
    if (Compass == "" || Compass == null) {
        alert("กรุณากรอก Co-Password ด้วยครับ!! ");
        document.getElementById("ComPass").focus();
        return false;
    }
    if (email == "" || email == null) {
        alert("กรุณากรอก E-mail ด้วยครับ!! ");
        document.getElementById("Email").focus();
        return false;
    }
    if (tel == "" || tel == null) {
        alert("กรุณากรอก Tel ด้วยครับ!! ");
        document.getElementById("Tel").focus();
        return false;
    }

    if(Password != Compass) {
        alert("Password และ ConfirmPassword ไม่ตรงกันครับ");
        document.getElementById("ComPass").focus();
        return false;
    }
}
