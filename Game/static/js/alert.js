
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


