csrf = $('input[name="csrfmiddlewaretoken"]').val();
$(function () {
    $.ajax({
        url: '/axf/result/',
        type: 'POST',
        data: {},
        dataType: 'json',
        headers: {'X-CSRFToken': csrf},
        success: function (msg) {
            //   for (i = 0; i < msg.cids.length; i++) {
            //     for(j = 0; j < msg.ids.length; j++){
            //         g_id = msg.ids[j];
            //         c_id = msg.cids[i];
            //         if(g_id == c_id){
            //             msg.ids.splice(j,1)
            //         }
            //         else {
            //             s = 0;
            //             $('#num_' + g_id).html(s);
            //             msg.ids.splice(j,1)
            //
            //         }
            //     }
            //
            // }


            if (msg.choose) {
                $('#one').show();
                $('#two').hide();
            }
            else {
                $('#one').hide();
                $('#two').show();
            }
        },
        error: function (msg) {
            alert('请求错误！')
        }
    })
});


function addShop(good_id) {
    $.ajax({
        url: '/axf/add_goods/',
        type: 'POST',
        data: {'good_id': good_id},
        dataType: 'json',
        headers: {'X-CSRFToken': csrf},
        success: function (msg) {
            $('#num_' + good_id).html(msg.c_num);
            $('#price').html(msg.price);
            cart_id = msg.cart_id;
            console.log(cart_id);
            s = '<span onclick="cartChange(' + cart_id + ' )">√</span>';
            $('#changeselect_' + cart_id).html(s);
            if (msg.choose) {
                $('#one').show();
                $('#two').hide();
            }
            else {
                $('#one').hide();
                $('#two').show();
            }

        },
        error: function (msg) {
            alert('请求错误！')
        }
    })
}

function subShop(good_id) {
    $.ajax({
        url: '/axf/sub_goods/',
        type: 'POST',
        data: {'good_id': good_id},
        dataType: 'json',
        headers: {'X-CSRFToken': csrf},
        success: function (msg) {
            $('#num_' + good_id).html(msg.c_num);
            $('#price').html(msg.price);
            cart_id = msg.cart_id;
            console.log(cart_id);
            s = '<span onclick="cartChange(' + cart_id + ' )">√</span>';
            $('#changeselect_' + cart_id).html(s);
            if (msg.choose) {
                $('#one').show();
                $('#two').hide();
            }
            else {
                $('#one').hide();
                $('#two').show();
            }
        },
        error: function (msg) {
            alert('请求错误！')
        }
    })
}

function cartChange(cart_id) {
    $.ajax({
        url: '/axf/user_select/',
        type: 'POST',
        data: {'cart_id': cart_id},
        dataType: 'json',
        headers: {'X-CSRFToken': csrf},
        success: function (msg) {
            if (msg.cart_is_select) {
                s = '<span onclick="cartChange(' + cart_id + ' )">√</span>';
                $('#price').html(msg.price)
            }
            else {
                s = '<span onclick="cartChange(' + cart_id + ' )">X</span>';
                $('#price').html(msg.price)
            }
            $('#changeselect_' + cart_id).html(s);
            if (msg.choose) {
                $('#one').show();
                $('#two').hide();
            }
            else {
                $('#one').hide();
                $('#two').show();
            }
        },
        error: function (msg) {
            alert('请求失败！')
        }
    })
}

// $(function () {
//     $('#one').on('click',function (msg) {
//         $('#one').hide();
//         $('#two').show();
//     })
// });
//
// $(function () {
//     $('#two').on('click',function (msg) {
//         $('#two').hide();
//         $('#one').show();
//     })
// });

function all_change1(ids) {
    $('#one').hide();
    $('#two').show();
    for (i = 0; i < ids.length; i++) {
        console.log(ids[i]);
        cart_id = ids[i];
        s = '<span onclick="cartChange(' + cart_id + ' )">X</span>';
        $('#changeselect_' + cart_id).html(s);
    }
    $.ajax({
        url: '/axf/allchange1/',
        type: 'POST',
        data: {'cart_id': cart_id},
        dataType: 'json',
        headers: {'X-CSRFToken': csrf},
        success: function (msg) {
            $('#price').html(msg.price)
        },
        error: function (msg) {
            alert('请求失败！')
        }
    });

}

function all_change2(ids) {
    $('#one').show();
    $('#two').hide();
    for (i = 0; i < ids.length; i++) {
        cart_id = ids[i];
        s = '<span onclick="cartChange(' + cart_id + ' )">√</span>';
        $('#changeselect_' + cart_id).html(s);
    }
    $.ajax({
        url: '/axf/allchange2/',
        type: 'POST',
        data: {'cart_id': cart_id},
        dataType: 'json',
        headers: {'X-CSRFToken': csrf},
        success: function (msg) {
            $('#price').html(msg.price)
        },
        error: function (msg) {
            alert('请求失败！')
        }
    });

}

$(function () {
    $('#regist').on('click', function () {
        window.location.assign('/axf/regist/')
    });
    err_name = $('#error_name').val();
    err_password = $('#error_password').val();
    if (err_name) {
        alert(err_name)
    }
    else if (err_password) {
        alert(err_password)
    }

});

