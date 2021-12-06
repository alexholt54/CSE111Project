// When login button is clicked...
$("#login").on("click", function(){
    let username = $("#username").val();
    let password = $("#password").val();
    if (username !== "" && password !== "") {
        $.ajax({
            url: "http://127.0.0.1:5000/",
            type: "POST",
            data: JSON.stringify({"username" : username, "password" : password}),
            contentType: "application/JSON",
            success: function(response){
                window.location.href = "http://127.0.0.1:5000/" + response
            }, 
            error: function(status, error){
                alert(error)
            }
        });
    }
});

// When create user button on login page is clicked...
$("#create").on("click", function(){
    let username = $("#username").val();
    let password = $("#password").val();
    $.ajax({
        url: "http://127.0.0.1:5000/newUser",
        type: "GET",
        success: function(response){
            window.location.href = "http://127.0.0.1:5000/newUser"
        }, 
        error: function(status, error){
            alert(error)
        }
    });
});

// When create user button is clicked on create user page...
$("#createUser").on("click", function(){
    let username = $("#newUsername").val();
    let password = $("#newPassword").val();
    if (username !== "" && password !== "") {
        $.ajax({
            url: "http://127.0.0.1:5000/newUser",
            type: "POST",
            data: JSON.stringify({"username" : username, "password" : password}),
            contentType: "application/JSON",
            success: function(response){
                alert("New Account Created! You can now log in!")
                window.location.href = "http://127.0.0.1:5000/"
            }, 
            error: function(status, error){
                alert(error)
            }
        });
    }
});

function logout(){
    $.ajax({
        url: "http://127.0.0.1:5000/logout",
        type: "GET",
        success: function(response){
            window.location.href = "http://127.0.0.1:5000/" + response
        }, 
        error: function(status, error){
            alert(error)
        }
    });
}

function returnToLogin(){
    window.location.href = "http://127.0.0.1:5000/"
}