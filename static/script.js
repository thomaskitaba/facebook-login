flask
 // document.addEventListener("DOMContentLoaded", function(){


function showdate(){
  diary_clock = settimeout ('currentdate();', 1000)
  
}

function currentdate(){
date_info = new date();
document.getElementById("clock").innerHTML = date_info;
showdate();

}




//});

