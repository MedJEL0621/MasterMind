

function playing(){
    alert('Seras redirigido')
    window.location='./game';
};

$(function() {
    var elemento = document.getElementById("header_color");
    $(window).scroll(function() {
      if ($(this).scrollTop() > 0) {
        elemento.classList.add('header_col');
      } else {
        elemento.classList.remove('header_col');
      }
    })
  });

function users() {
    
    arr = ["Juan", "Kevin", "Estefania", "Laura", "alberton", "camilo"];
    
    for(var i = 0; i < 6; i++){
        if(i == 4){
            arr[i] = "";
        }
        console.log(arr[i]);
    }
    arr[i] = null;
    console.log(arr[i]);
};

users();



