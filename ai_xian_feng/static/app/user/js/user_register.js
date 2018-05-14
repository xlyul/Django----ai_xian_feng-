csrf = $('input[name="csrfmiddlewaretoken"]').val();
$(function () {


    $("#password_confirm").change(function () {
        var password = $("#password").val();
        var password_confirm = $('#password_confirm').val();
        console.log(password);
        console.log(password_confirm);
        if (password.length == 0 || password_confirm.length == 0) {
            console.log(password.length);
            $("#password_confirm_info").html("密码不能为空！").css("color", "red");
        }
        else {
            if (password == password_confirm) {
                $("#password_confirm_info").html("两次一致").css("color", "green");
            } else {
                $("#password_confirm_info").html("两次输入不一致").css("color", "red");
            }
        }

    });

    // $("#username").change(function () {
    //
    // //
    //     var username = $("#username").val();
    //     $.getJSON("/axf/checkuser/",{"username":username},function (data) {
    //
    //         console.log(data);
    //
    //         if(data["status"] == "200"){
    //             $("#username_info").html(data["desc"]).css("color","green");
    //         }else if(data["status"] == "900"){
    //             $("#username_info").html(data["desc"]).css("color","red");
    //         }
    //
    //
    //     })

    $("#username").change(function () {
        var username = $("#username").val();
        console.log(typeof username);
        $.ajax({
            url: '/axf/check/',
            type: 'POST',
            data: {},
            dataType: 'json',
            headers: {'X-CSRFToken': csrf},
            success: function (msg) {
                console.log(msg);
                if (username.length > 10) {
                    $("#username_info").html('用户名不能超过10位！').css('color', 'red')
                } else if (username.length == 0) {
                    $("#username_info").html('用户名不能为空！').css('color', 'red')
                }
                else {
                    var num = 0;
                    for (i = 0; i < msg.us.length; i++) {
                        console.log(typeof msg.us[i]);
                        if (username != msg.us[i]) {
                            num += 1
                        }
                    }
                    console.log(num);
                    if (num == msg.us.length) {
                        $("#username_info").html('用户名正确！').css('color', 'green')

                    }
                    else {
                        $("#username_info").html('用户名已存在！').css('color', 'red')

                    }
                }

            }
        });
    });

    $("#email").change(function () {
        var email = $("#email").val();
        $.ajax({
            url: '/axf/check/',
            type: 'POST',
            data: {},
            dataType: 'json',
            headers: {'X-CSRFToken': csrf},
            success: function (msg) {
                var num = 0;
                for (i = 0; i < msg.es.length; i++) {
                    if (email != msg.es[i]) {
                        num += 1
                    }
                }
                if (num != msg.es.length) {
                    $("#email_info").html('邮箱名已存在！').css('color', 'red')
                }
                else {
                    $("#email_info").html('邮箱名可用！').css('color', 'green')
                }
            }
        });
    });


});

function checkinput() {

    var color1 = $("#username_info").css("color");
    console.log(color1);
    if (color1 == "rgb(255, 0, 0)") {
        console.log("红色的");
        return false
    } else {
        console.log("绿色的");
        return true
    }

    var password = $("#password").val();
    if (password.length < 6) {
        alert('密码不能少于6位！');
        return false
    }
    else {
        return true
    }

    var password_confirm = $("#password_confirm").val();

    if (password == password_confirm) {
        return true
    }
    else {
        return false
    }
}