$(document).ready(() => {
    $('form').submit((event) => {
        event.preventDefault();
        form = $("form")

        $.ajax({
            'url' : '/ajax/newsletter/',
            'type' : 'POST',
            'data' : form.serialize(),
            'datatype': 'json',
            'success': (data) => {
                alert(data['success'])
            },
        })// END of AJAX method
        $('#id_your_name').val('')
        $('#id_email').val('')
    }) // end of submit event
}) // end of document ready function