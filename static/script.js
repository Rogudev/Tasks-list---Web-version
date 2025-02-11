
$(document).ready(function () {


    // shutdown function
    document.getElementById('shutdown-btn').addEventListener('click', function () {

        $.ajax({
            type: "POST",
            url: "/shutdown",
            contentType: "application/json; charset=utf-8",
            dataType: "text",
            success: function (response) {
                alert(response);
                window.close();
            }
        });


    });

});



