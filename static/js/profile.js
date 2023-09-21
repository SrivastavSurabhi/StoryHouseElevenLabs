$(document).ready(function() {
    $('div.editable, .update_buttons, .editable_user_name').addClass('d-none')
    $('.flex-title h1').text('Profile')


    $(document).on('click','.editicon',function(){
        $('.editicon, .user_name').addClass('d-none')
        $('div.editable, .update_buttons, .editable_user_name').removeClass('d-none')
        $('.flex-title h1').text('Edit Profile')
    })

    $(document).on('click','.cancel',function(){
        $('.editicon, .user_name').removeClass('d-none')
        $('div.editable, .update_buttons, .editable_user_name').addClass('d-none')
        $('.flex-title h1').text('Profile')
    })

    $(document).on('change','#addprofile',function(){
       img = this
        const file = img.files[0];
        uploadImg(file, "relativebox")
    })

    $(document).on('click','.update_buttons .save',function(){
        name = $('#fname').val()
        file = $('.editable input')[0].files[0]
        if (name && name != $('.base_user_name').text() || file){
            data = new FormData()
            data.append('name', name)
            data.append('file', file)
            token = document.getElementsByName("csrfmiddlewaretoken")[0].value
            $.ajax({
                method: "POST",
                headers: {'X-CSRFToken': token},
                url: '/auth/profile',
                data: data,
                processData: false,
                contentType: false,
                dataType: "json",
                beforeSend: function(){
                    $('.parent-loader').fadeIn()
                },
                complete: function(){
                    $('.parent-loader').fadeOut()
                },
                success: function(data){
                    $('.editicon, .user_name').removeClass('d-none')
                    $('div.editable, .update_buttons, .editable_user_name').addClass('d-none')
                    $('.flex-title h1').text('Profile')
                    $('.base_user_name, .user_name').text(name)
                    uploadImg(file, "profiles")
                },
                error: function(){
                    console.log('hi')
                }
            })
        }
        else{
            oneNotificationAtOnce('Please update fields to save changes.')
        }
    })

    function uploadImg(file, className){
        const reader = new FileReader();
        reader.addEventListener("load", () => {
           $("."+ className + " img").attr("src", reader.result)
        }, false);

        if (file) {
          reader.readAsDataURL(file);
        }
    }


    function oneNotificationAtOnce(message, status='error'){
        $('.notifyjs-corner').empty();
        $.notify(message, status);
    }

})


