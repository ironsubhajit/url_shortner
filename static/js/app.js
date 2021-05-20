$(document).on('submit', '#post-form', function(e){
    e.preventDefault(); // prevent default reloading page

    $.ajax({
        type: 'POST',
        url: '/create',
        data: {
            link: $('#link').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken').val(),
        },
        success: function(data){
            var newUrl = 'http://127.0.0.1:8000/go/'+data;
            $('#recent').attr("href", newUrl);
            $('#recent').html("localhost:8000/go/"+data);
        }
    });
});