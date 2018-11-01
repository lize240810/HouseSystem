
/**
 * 显示验证提示信息
 */
function showValidate(input) {
    var thisAlert = $(input).parent();
    $(thisAlert).addClass('alert-validate');
}
/**
 * 隐藏验证提示信息
 */
function hideValidate(input) {
    var thisAlert = $(input).parent();
    $(thisAlert).removeClass('alert-validate');
}
/**
 * 切换验证提示信息
 */
function toggleValidate(input) {
    if($(thisAlert).hasClass('alert-validate')){
        $(thisAlert).removeClass('alert-validate');       
    }else{
        $(thisAlert).addClass('alert-validate');       
    }
}
/**
 * 验证email
 */
function validate (input) {
    if($(input).attr('type') == 'email' || $(input).attr('name') == 'email') {
        if($(input).val().trim().match(/^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/) == null) {
            return false;
        }
    }
    else {
        if($(input).val().trim() == ''){
            return false;
        }
    }
}
/**
 * 使用ajax 异步请求登录
 */
function ajax_login(){
     var username = $('input[name = "username"]').val().trim(),
         pass = $('input[name = "pass"]').val().trim();
         $.ajax({
            url : GLOBAL.AJAX_LOGIN,
            type : 'GET',
            data :
                {
                    'username': username,
                    'pass': pass
                },
            dataType : 'json',
            success : function(resp){
                switch(resp.error)
                {
                case 0:
                    sweetAlert("欢迎登录", resp.desc,"success");
                    window.location.href = resp.url;
                    break;
                case 1:
                    sweetAlert("温馨提示", resp.desc,"error");
                    break;
                case 4:
                    sweetAlert("温馨提示", resp.desc,"info");
                    break;
                default :
                    sweetAlert("温馨提示", resp.desc,"info");
                    break;
                }
                
            },
            error: function(info) {
                console.log(arguments);
                // debugger;
                swal("温馨提示", info,"error");
            }
        });
}


(function ($) {
    "use strict";


    /*==================================================================
    [ Focus input ]*/
    $('.input100').each(function(){
        $(this).on('blur', function(){
            if($(this).val().trim() != "") {
                $(this).addClass('has-val');
            }
            else {
                $(this).removeClass('has-val');
            }
        })    
    })

  
    /*==================================================================
    [ Validate ]*/


    $('.validate-form').on('submit',function(event){
        // j禁止默认事件
        event.preventDefault();
        // this.submit();
        var check = true;

        var input = $('.validate-input .input100');

        for(var i=0; i<input.length; i++) {
            if(validate(input[i]) == false){
                showValidate(input[i]);
                check=false;
            }
        }
        if(check){
            ajax_login()
        }

        return check;
    });

})(jQuery);