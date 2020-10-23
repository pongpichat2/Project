function CheckLogin(){
    var email = document.forms["Login"]["Username"].value;
    var pass = document.forms["Login"]["password"].value;

    if (email == "" || email == null) {
        alert("กรุณากรอก Username ด้วยครับ!! ");
        document.getElementById("Username").focus();
        return false;
    }
    if (pass == "" || pass == null) {
        alert("กรุณากรอก Password ด้วยครับ!! ");
        document.getElementById("password").focus();
        return false;
    }
}
var i=1;
function add(){
i++;
var new_input="<input type='text' id='Sub_"+i+"' name='Sub[]'  required><button type='button' class='but-Delete' onclick='remove();' id='Subbut_"+i+"'>x</button><br id = 'br_"+i+"'>";
$('#new_chq').append(new_input);
$('#total_chq').val(i)
}
function remove(){
var last_chq_no = $('#total_chq').val();
if(last_chq_no>0){
  $('#Sub_'+last_chq_no).remove();
  $('#Subbut_'+last_chq_no).remove();
  $('#br_'+last_chq_no).remove();
  $('#total_chq').val(last_chq_no-1);
}
}