
$(document).ready(function () {


    // shutdown function
    $('#shutdown-btn').on('click', function () {

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

    // add task
    $('#add_task-btn').on('click', function () {

        const taskName = $('#task_input').val()

        $.ajax({
            type: "POST",
            url: "/add_task",
            data: JSON.stringify({ name: taskName }),   //send as JSON
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function (response) {
                if (response.status == 200) {
                    location.reload()

                } else {
                    alert("Server error")
                }
                
            }
        });

    });


    // mark task as 'Done' using event delegation
    $(document).on('click', '.finalize-task', function (e) {
        e.preventDefault();
        const taskID = $(this).data('id');  // Get the task ID from the data-id attribute
        
        $.ajax({
            type: "POST",
            url: "/finalize_task",
            data: JSON.stringify({ id: taskID }),  // Send the task ID as JSON
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function (response) {
                if (response.status == 200) {
                    location.reload();  

                } else {
                    alert("Server error");
                }
            }
        });
        
    });


    // delete a task
    $(document).on('click', '.rm-task', function (e) {
        e.preventDefault();

        const taskID = $(this).data('id');  // Get the task ID from the data-id attribute
        
        $.ajax({
            type: "POST",
            url: "/delete_task",
            data: JSON.stringify({ id: taskID }),  // Send the task ID as JSON
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function (response) {
                if (response.status == 200) {
                    location.reload();  
                    
                } else {
                    alert("Server error");
                }
            }
        });
    });


    // restart a task
    $(document).on('click', '.restart-task', function (e) {
        e.preventDefault();

        const taskID = $(this).data('id');  // Get the task ID from the data-id attribute
        
        $.ajax({
            type: "POST",
            url: "/restart_task",
            data: JSON.stringify({ id: taskID }),  // Send the task ID as JSON
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function (response) {
                if (response.status == 200) {
                    location.reload();  
                    
                } else {
                    alert("Server error");
                }
            }
        });
    });

});



