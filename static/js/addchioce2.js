function dataNull(){
    var subname = document.forms["Addsub"]["Subname"].value;
    var subid = document.forms["Addsub"]["Subid"].value;
    

    if (subname == "" || subname == null) {
    alert("กรุณากรอกข้อมูลให้ครบด้วย !! ");
    document.getElementById("Subname").focus();
    return false;
    }
    if (subid == "" || subid == null) {
        alert("กรุณากรอกข้อมูลให้ครบด้วย !! ");
        document.getElementById("Subid").focus();
        return false;
    }
    
}