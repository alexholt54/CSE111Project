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
    window.location.href = "http://127.0.0.1:5000/newUser"
})

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
    window.location.href = "http://127.0.0.1:5000/";
}

function goHome(){
    window.location.href = "http://127.0.0.1:5000/home";
}

// When delete user is clicked...
$("#deleteUser").on("click", function(){
    let username = $("#deleteUsername").val();
    if (username !== "") {
        $.ajax({
            url: "http://127.0.0.1:5000/admin",
            type: "DELETE",
            data: JSON.stringify({"username" : username, "type" : "user"}),
            contentType: "application/JSON",
            success: function(response){
                alert("Account Deleted!")
            }, 
            error: function(status, error){
                alert(error)
            }
        });
    }
});

// When admin adds data...
$("#addData").on("click", function(){
    let artist = $("#artistName").val();
    let song = $("#songName").val();
    let album = $("#albumName").val();
    let genre = $("#genreName").val();
    let year = $("#albumYear").val()
    $.ajax({
        url: "http://127.0.0.1:5000/admin",
        type: "POST",
        data: JSON.stringify({"artist" : artist, "song" : song, "album" : album, "genre" : genre, "year" : year, "type" : "data"}),
        contentType: "application/JSON",
        success: function(response){
            alert("Data Added!")
        }, 
        error: function(status, error){
            alert(error)
        }
    });
});

// When admin deletes data...
$("#deleteData").on("click", function(){
    let artist = $("#artistName").val();
    let song = $("#songName").val();
    let album = $("#albumName").val();
    let genre = $("#genreName").val();
    $.ajax({
        url: "http://127.0.0.1:5000/admin",
        type: "DELETE",
        data: JSON.stringify({"artist" : artist, "song" : song, "album" : album, "genre" : genre, "type" : "data"}),
        contentType: "application/JSON",
        success: function(response){
            alert("Data Deleted!")
        }, 
        error: function(status, error){
            alert(error)
        }
    });
});