// When login button is clicked...
$("#login").on("click", function(){
    let username = $("#username").val();
    let password = $("#password").val()
    if (username !== "" && password !== "") {
        $.ajax({
            url: "http://127.0.0.1:5000",
            type: "POST",
            data: JSON.stringify({"username" : username, "password" : password}),
            contentType: "application/JSON",
            success: function(response){
                response = "/" + response
                window.location.href = "http://127.0.0.1:5000" + response
            }, 
            error: function(status, error){
                alert(error)
            }
        });
    }
});