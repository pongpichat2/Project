function checkdata(){
    var Quiz = document.forms["AddChoice"]["Proposition"].value;
    var C1 = document.forms["AddChoice"]["Ch1"].value;
    var C2 = document.forms["AddChoice"]["Ch2"].value;
    var C3 = document.forms["AddChoice"]["Ch3"].value;
    var C4 = document.forms["AddChoice"]["Ch4"].value;

    if (Quiz == "" || Quiz == null) {
        alert("กรุณากรอกโจทย์ด้วยครับ!! ");
        document.getElementById("Proposition").focus();
        return false;
    }
    if (C1 == "" || C1 == null) {
        alert("กรุณากรอก Choice1 ด้วยครับ!! ");
        document.getElementById("Ch1").focus();
        return false;
    }
    if (C2 == "" || C2 == null) {
        alert("กรุณากรอก Choice2 ด้วยครับ!! ");
        document.getElementById("Ch2").focus();
        return false;
    }
    if (C3 == "" || C3 == null) {
        alert("กรุณากรอก Choice1 ด้วยครับ!! ");
        document.getElementById("Ch3").focus();
        return false;
    }
    if (C4 == "" || C4 == null) {
        alert("กรุณากรอก Choice4 ด้วยครับ!! ");
        document.getElementById("Ch4").focus();
        return false;
    }
}