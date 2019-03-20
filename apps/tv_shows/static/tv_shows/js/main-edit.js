$(document).ready(function() {

    $('#title').keyup(function() {

        data = $('#input').serialize();
        $.ajax({
            type: "POST",
            url: "/shows/edit-title-check",
            data: data,
            success: function (response) {
                $('#warn').html(response);
            }
        });

    });

});