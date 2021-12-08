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

function searching(){
    let search = $("#searchBar").val();
    if (search !== "") {
        $.ajax({
            url: "http://127.0.0.1:5000/home",
            type: "POST",
            data: JSON.stringify({"search" : search}),
            contentType: "application/JSON",
            success: function(response){
                window.location.href = response
            }, 
            error: function(status, error){
                alert(error)
            }
        });
    }

}

function makePub() {
    $.ajax({
        url: window.location.href,
        type: "PUT",
        data: JSON.stringify({"makePub" : "yes"}),
        contentType: "application/JSON",
        success: function(response){
            alert("Playlist Now Public!")
            window.location.href = window.location.href
        }, 
        error: function(status, error){
            alert(error)
        }
    });
}

function makePriv() {
    $.ajax({
        url: window.location.href,
        type: "PUT",
        data: JSON.stringify({"makePub" : "no"}),
        contentType: "application/JSON",
        success: function(response){
            alert("Playlist Now Private!")
            window.location.href = window.location.href
        }, 
        error: function(status, error){
            alert(error)
        }
    });
}

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

function newPlaylist(){
    let playlist = $("#newPlaylist").val();
    if (playlist !== "") {
        $.ajax({
            url: window.location.href,
            type: "POST",
            data: JSON.stringify({"playlist" : playlist, "type" : "playlist"}),
            contentType: "application/JSON",
            success: function(response){
                alert("Playlist Added!")
                window.location.href = window.location.href
            }, 
            error: function(status, error){
                alert(error)
            }
        });
    }
}

function followUser(){
    $.ajax({
        url: window.location.href,
        type: "POST",
        data: JSON.stringify({"type" : "follow"}),
        contentType: "application/JSON",
        success: function(response){
            alert("Now Following User!")
            window.location.href = window.location.href
        }, 
        error: function(status, error){
            alert(error)
        }
    });
}

function unfollowUser(){
    $.ajax({
        url: window.location.href,
        type: "DELETE",
        success: function(response){
            alert("Unfollowed User!")
            window.location.href = window.location.href
        }, 
        error: function(status, error){
            alert(error)
        }
    });
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

// When follow button is clicked...
function followArtist(){
    $.ajax({
        url: window.location.href,
        type: "POST",
        success: function(response){
            alert("Now Following Artist!")
            window.location.href = window.location.href
        }, 
        error: function(status, error){
            alert(error)
        }
    });
}

function deletePlaylist() {
    $.ajax({
        url: window.location.href,
        type: "DELETE",
        data: JSON.stringify({"type" : "playlist"}),
        contentType: "application/JSON",
        success: function(response){
            alert("Playlist Deleted!")
            goHome()
        }, 
        error: function(status, error){
            alert(error)
        }
    });
}

// When unfollow button is clicked...
function unfollowArtist() {
    $.ajax({
        url: window.location.href,
        type: "DELETE",
        success: function(response){
            alert("Unfollowed Artist!")
            window.location.href = window.location.href
        }, 
        error: function(status, error){
            alert(error)
        }
    });
}

// When add song is clicked...
$("#addSong").on("click", function(){
    let song = $("#newSong").val();
    if (song !== "") {
        $.ajax({
            url: window.location.href,
            type: "POST",
            data: JSON.stringify({"song" : song}),
            contentType: "application/JSON",
            success: function(response){
                alert("Song Added!")
                window.location.href = window.location.href
            }, 
            error: function(status, error){
                alert(error)
            }
        });
    }
});

// When delete song is clicked...
$("#deleteSong").on("click", function(){
    let song = $("#newSong").val();
    if (song !== "") {
        $.ajax({
            url: window.location.href,
            type: "DELETE",
            data: JSON.stringify({"song" : song, "type" : "song"}),
            contentType: "application/JSON",
            success: function(response){
                alert("Song Deleted!")
                window.location.href = window.location.href
            }, 
            error: function(status, error){
                alert(error)
            }
        });
    }
});