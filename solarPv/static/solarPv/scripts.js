function validateRegistration(){
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    if(username.length > 8){
        alert("Username cannot be greater than 8 characters.");
    }
    if(password.length > 8){
        alert("Password cannot be greater than 8 characters.");
    }
    var pattern = new RegExp("^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[-+_!@#$%^&*.,?]).+$");
    if (!pattern.test(password)) {
        alert("Password must have a a digit, a lowercase letter,"
                +"an uppercase letter, and a special character")
    }

    return false;
}

