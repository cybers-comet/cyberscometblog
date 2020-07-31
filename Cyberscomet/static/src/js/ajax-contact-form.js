jQuery(function ($) {
    "use strict";
    // Get the form.
    var form = $('#ajax-form');

    // Get the button.
    var sendbutton = $('#sendbutton');

    // Get the messages div.
    var formMessages = $('#form-messages');

    // Set up an event listener for the contact form.
    $(form).submit(function (e) {
        // Stop the browser from submitting the form.
        e.preventDefault();
        
        // Disable the button
        sendbutton.prop('disabled', true);

        // Serialize the form data.
        var formData = $(form).serialize();

        // Submit the form using AJAX.
        $.ajax({
            type: 'POST',
            url: $(form).attr('action'),
            data: formData
        }).done(function (response) {
            
            // Make sure that the formMessages div has the 'ajax-success' class.
            $(formMessages).removeClass('ajax-error');
            $(formMessages).addClass('ajax-success');

            // Set the message text.
            $(formMessages).text('留言成功！>o<');

            // Clear the form.
            $('#name').val('');
            $('#email').val('');
            $('#phone').val('');
            $('#content').val('');
            
            // Display the button
            sendbutton.prop('disabled', false);
            
        }).fail(function (data) {
            
            // Make sure that the formMessages div has the 'ajax-error' class.
            $(formMessages).removeClass('ajax-success');
            $(formMessages).addClass('ajax-error');

            // Set the message text.
            if (data.responseText !== '') {
                // Display the message
                $(formMessages).text('留言成功！>o<');
                // Display the button
                sendbutton.prop('disabled', false);
            } else {
                // Display the error message
                $(formMessages).text('啊! 有一个错误发生了');
                // Display the button
                sendbutton.prop('disabled', false);
            }
        });
    });
});