let count = 1;
document.getElementById("radio1").checked = true;

setInterval(function(){
    nextimage();
}, 4000)

function nextimage(){
    count++;
    if(count>4){
        count = 1;
    }
    document.getElementById("radio"+count).checked = true;
}

var menu = document.querySelectorAll(".header-info> ul > li > a");

for(var i = 0; i < menu.length; i++){
	menu[i].addEventListener("click", configMenu);
}



