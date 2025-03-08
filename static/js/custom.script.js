
$(document).ready(function () {

    const textareas = $('.taskAdjustHeight');

    // adjust textarea height function
    function adjustHeight() {
        textareas.each(function () {
            $(this).css('height', 'auto');  
            $(this).css('height', this.scrollHeight + 'px');  
        });
    }

    // adjust when content changes
    textareas.on('input', adjustHeight);

    // adjust when content is loaded
    adjustHeight();


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

        const taskName = $('#task_name_input').val()
        const taskDesc = $('#task_desc_input').val()

        $.ajax({
            type: "POST",
            url: "/add_task",
            data: JSON.stringify({ name: taskName, desc: taskDesc }),   //send as JSON
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


    // update task
    $(document).on('click', '.update-task', function (e) {
        e.preventDefault();

        const taskID = $(this).data('id');  // Get the task ID from the data-id attribute
        
        const taskName = $(`textarea[data-id="Name${taskID}"]`).val()
        const taskDesc = $(`textarea[data-id="Desc${taskID}"]`).val()

        $.ajax({
            type: "POST",
            url: "/update_task",
            data: JSON.stringify({ id: taskID, name: taskName, desc: taskDesc}),  // Send the task ID as JSON
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



