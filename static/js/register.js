
function ajax_register(){
    var username = $('input[name="username"]').val().trim(),
        pass = $('input[name="pass"]').val().trim(),
        email = $('input[name="email"]').val().trim(),
        phone = $('input[name="phone"]').val().trim()

    $.ajax({
        url : GLOBAL.AJAX_REGISTER,
        type:'GET',
        data:{
            'username' : username,
            'pass' : pass,
            'email' : email,
            'phone' : phone
        },
        dataType:'json',
        success : function(resp){
            console.log(resp)
            switch(resp.error){
                case 0:
                    swal({
                            title: '注册成功',
                            text: '快去登录吧',
                            icon: "/static/images/thumbs-up.jpg" 
                        });
                    window.location.href = resp.url;
                    break;
                case 1:
                    sweetAlert("温馨提示", resp.desc,"warning");
                    break;
                case 2:
                    sweetAlert("欢迎注册", resp.desc,"success");
                    break;
                case 3:
                    sweetAlert("欢迎注册", resp.desc,"info");
                    break;
            }
                
            },
        error: function(info){
            console.log(arguments);
            // debugger;
            swal("温馨提示", info, "error");
        }
    })
}

$(function(){
    $('.login100-form-btn').click(function(event){
        event.preventDefault();
        ajax_register()
    })
})