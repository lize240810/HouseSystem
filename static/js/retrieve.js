/**
 *  加载验证码图片
 */
function load_captcha($img) {
    $.ajax({
        url:'/captcha',
        type:'GET',
        data:{},
        dataType:'text',
        success: function(resp){
            $img.attr('src', resp);
        },
        error: function(xhr){
            swal('error','失败','error');
        }
    });
}

/**
 * 验证
 */
function verify_captcha($img){
    var captcha = $('input[name=captcha]').val()
    
     $.ajax({
        url : GLOBAL.AJAX_VERIFY,
        type : 'GET',
        data :{
            'captcha': captcha
        },
        dataType : 'json',
        success : function(resp){
            // 成功的画就更换一张图片
            var reload = function() {
                load_captcha($img);
            }
            if (resp.error == 0) {
                swal('验证成功', resp.desc ,'success')
                return true;
            }
            else if (resp.error == 1) {
                swal('提示', resp.desc ,'warning')
            }
            else if (resp.error == 3) {
                swal('提示', resp.desc ,'warning')
            }
            else{
                swal('验证失败', resp.desc ,'error')
            }
        },
        error: function(xhr){
            swal('提示','失败','error')
        }
     });
}

/**
 * 加载事件
 */
$(function(){
    var $img = $("#img-captcha");
    
    load_captcha($img)

    $img.on('click', function(){
        load_captcha($img)
    })

    $("button").on('click', function(){
        verify_captcha($img)
    });
})