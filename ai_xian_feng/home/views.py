import random
import time

from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.core.urlresolvers import reverse

from home.models import MainWheel, MainNav, MainMustBuy, MainShop, MainShow, UserModel, Goods, FoodType, \
    OrderModel, CarModel, OrderGoodsModel


def home(request):
    """
    主页显示
    whee: 轮播
    nav: 导航
    mustbuy: 必购
    shop: 商店
    mainshow: 主要商品展示
    """
    data = {
        'wheel': MainWheel.objects.all(),
        'nav': MainNav.objects.all(),
        'mustbuy': MainMustBuy.objects.all(),
        'shop': MainShop.objects.all(),
        'mainshow': MainShow.objects.all()
    }
    return render(request, 'home/home.html', data)


def regist(request):
    if request.method == 'GET':
        return render(request, 'user/user_register.html')
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        icon = request.FILES.get('icon')

        password = make_password(password)
        UserModel.objects.create(
            username=name,
            email=email,
            password=password,
            icon=icon
        )
        return HttpResponseRedirect('/axf/login/')


def login(request):
    if request.method == 'GET':
        return render(request, 'user/user_login.html')
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')
        if UserModel.objects.filter(username=name).exists():
            user = UserModel.objects.get(username=name)
            if check_password(password, user.password):
                s = 'abcdefghijklmnopqrstuvewxyz'
                ticket = ''
                for _ in range(15):
                    ticket += random.choice(s)
                now_time = int(time.time())
                ticket = 'TK' + ticket + str(now_time)
                response = HttpResponseRedirect('/axf/mine/')
                response.set_cookie('ticket', ticket, max_age=3000)
                user.user_ticket = ticket
                user.save()
                return response
            else:
                return render(request, 'user/user_login.html', {'password': '密码错误！'})
        else:
            return render(request, 'user/user_login.html', {'name': '用户名错误！'})


def logout(request):
    if request.method == 'GET':
        response = HttpResponseRedirect('/axf/mine/')
        response.delete_cookie('ticket')
        return response


def mine(request):
    user = UserModel.objects.filter(user_ticket=request.COOKIES.get('ticket')).first()
    # user = request.user
    if user and user.id:
        wait_pay = user.ordermodel_set.filter(o_status=0).count()
        payed = user.ordermodel_set.filter(o_status=1).count()
        data = {
            'user': user,
            'wait_pay': wait_pay,
            'payed': payed,
        }
        return render(request, 'mine/mine.html', data)
    else:
        return render(request, 'mine/mine.html', {'user': user})


def cart(request):
    if request.method == 'GET':
        user = request.user
        if user and user.id:
            cars = CarModel.objects.filter(user_id=user)
            price = 0
            ids = []

            for car in cars:
                id = car.id
                ids.append(id)
                if car.is_select:
                    price += car.goods.price * car.c_num
                    price = float('%.1f' % price)

            data = {
                'cars': cars,
                'price': price,
                'ids': ids,
            }

            return render(request, 'cart/cart.html', data)
        else:
            return HttpResponseRedirect('/axf/login/')


def result(request):
    if request.method == 'POST':
        data = {
            'code': '200',
            'msg': '请求成功'
        }
        user = request.user
        cars = CarModel.objects.filter(user_id=user)
        a = 0
        cids = []
        for car in cars:
            # cid = car.goods_id
            # cids.append(cid)
            if car.is_select:
                a += 1
        if a == len(cars):
            choose = True
        else:
            choose = False

        data['choose'] = choose
        # ids = []
        # goods = Goods.objects.all()
        # for good in goods:
        #     id = good.id
        #     ids.append(id)
        # data['ids'] = ids
        # data['cids'] = cids

        return JsonResponse(data)


def user_generate_order(request):
    if request.method == 'GET':
        user = request.user
        if user and user.id:
            # 先查询is_select为True的购物车数据
            carts = CarModel.objects.filter(is_select=True)

            # 创建订单
            order = OrderModel.objects.create(user=user, o_status=0, )

            # 创建订单详情信息
            for good in carts:
                OrderGoodsModel.objects.create(goods_id=good.goods_id,
                                               order_id=order.id,
                                               goods_num=good.c_num)
            carts.delete()
            return HttpResponseRedirect('/axf/order/' + str(order.id) + '/')


def all_change1(request):
    if request.method == 'POST':
        user = request.user
        data = {
            'code': '200',
            'msg': '请求成功'
        }
        if user and user.id:
            carts = CarModel.objects.filter(user_id=user)
            for cart in carts:
                cart.is_select = 0
                cart.save()
            price = 0
            data['price'] = price

        return JsonResponse(data)


def all_change2(request):
    if request.method == 'POST':
        user = request.user
        data = {
            'code': '200',
            'msg': '请求成功'
        }
        if user and user.id:
            carts = CarModel.objects.filter(user_id=user)
            for cart in carts:
                cart.is_select = 1
                cart.save()
            cars = CarModel.objects.filter(user_id=user)
            a = 0
            for ca in cars:
                if ca.is_select:
                    a += 1
            if a == len(cars):
                choose = True
            else:
                choose = False
            data['choose'] = choose
            price = 0
            for car in cars:
                if car.is_select:
                    price += car.goods.price * car.c_num
                    price = float('%.1f' % price)
            data['price'] = price
        return JsonResponse(data)


def user_select(request):
    if request.method == 'POST':
        cart_id = request.POST.get('cart_id')
        user = request.user
        data = {
            'code': '200',
            'msg': '请求成功'
        }
        if user and user.id:
            car = CarModel.objects.filter(pk=cart_id).first()
            if car.is_select:
                car.is_select = False
                car.save()
            else:
                car.is_select = True
                car.save()
            data['cart_is_select'] = car.is_select
            cars = CarModel.objects.filter(user_id=user)
            a = 0
            for ca in cars:
                if ca.is_select:
                    a += 1
            if a == len(cars):
                choose = True
            else:
                choose = False
            data['choose'] = choose
            price = 0
            for car in cars:
                if car.is_select:
                    price += car.goods.price * car.c_num
                    price = float('%.1f' % price)
            data['price'] = price
        return JsonResponse(data)


def add_goods(request):
    if request.method == 'POST':
        user = request.user
        data = {
            'code': '200',
            'msg': '请求成功'
        }
        if user and user.id:
            good_id = request.POST.get('good_id')
            # 获取购物车信息
            user_carts = CarModel.objects.filter(user=user, goods=good_id).first()
            # 如果购物车内有该商品就增加数量
            if user_carts:
                user_carts.c_num += 1
                user_carts.save()
                data['c_num'] = user_carts.c_num
                if not user_carts.is_select:
                    user_carts.is_select = 1
                    user_carts.save()
                    data['cart_id'] = user_carts.id
            else:
                # 如果购物车内没有该商品就创建
                CarModel.objects.create(
                    user=user,
                    goods_id=good_id,
                    c_num=1
                )
                data['c_num'] = 1
            cars = CarModel.objects.filter(user_id=user)
            price = 0
            for car in cars:
                if car.is_select:
                    price += car.goods.price * car.c_num
                    price = float('%.1f' % price)
            data['price'] = price
            a = 0
            for ca in cars:
                if ca.is_select:
                    a += 1
            if a == len(cars):
                choose = True
            else:
                choose = False
            data['choose'] = choose
        return JsonResponse(data)


def sub_goods(request):
    if request.method == 'POST':
        data = {
            'code': '200',
            'msg': '请求成功'
        }
        user = request.user
        goods_id = request.POST.get('good_id')
        if user and user.id:
            user_carts = CarModel.objects.filter(user=user, goods=goods_id).first()
            if user_carts:
                if user_carts.c_num == 1:
                    user_carts.delete()
                    data['c_num'] = 0
                else:
                    user_carts.c_num -= 1
                    user_carts.save()
                    data['c_num'] = user_carts.c_num
                    if not user_carts.is_select:
                        user_carts.is_select = 1
                        user_carts.save()
                        data['cart_id'] = user_carts.id
            cars = CarModel.objects.filter(user_id=user)
            price = 0
            for car in cars:
                if car.is_select:
                    price += car.goods.price * car.c_num
                    price = float('%.1f' % price)
            data['price'] = price
            a = 0
            for ca in cars:
                if ca.is_select:
                    a += 1
            if a == len(cars):
                choose = True
            else:
                choose = False
            data['choose'] = choose
        return JsonResponse(data)


def market(request):
    return HttpResponseRedirect(reverse('axf:market_show', args=('104749', '0', '0')))


def market_show(request, type_id, child_cid, new_id):
    if request.method == 'GET':
        user = request.user
        type_names = FoodType.objects.all()

        if child_cid == '0':
            goods = Goods.objects.filter(category=type_id)
        else:
            goods = Goods.objects.filter(category=type_id, child_cid_name=child_cid)

        child_names = Goods.objects.filter(category=type_id)
        child_names = child_names.values('child_cid_name').distinct()

        if new_id == '0':
            goods = goods.order_by('product_num')

        elif new_id == '1':
            goods = goods.order_by('store_nums')

        elif new_id == '2':
            goods = goods.order_by('-price')

        elif new_id == '3':
            goods = goods.order_by('price')

        data = {
            'type_names': type_names,
            'goods': goods,
            'child_names': child_names,
            'type_id': type_id,
            'child_cid': child_cid,
            'new_id': new_id,
            'user': user
        }
        # user = request.user
        # if user and user.id:
        #     carts = CarModel.objects.all()
        #     data['carts'] = carts
        return render(request, 'market/market.html', data)


def order(request, order_id):
    if request.method == 'GET':
        orders1 = OrderModel.objects.filter(pk=order_id).first()
        data = {
            'order_id': order_id,
            'orders1': orders1
        }
        return render(request, 'order/order_info.html', data)


def order_pay(request, order_id):
    # 修改订单状态
    if request.method == 'GET':
        OrderModel.objects.filter(pk=order_id).update(o_status=1)
        return HttpResponseRedirect(reverse('axf:mine'))


def order_list(request):
    user = request.user
    if user and user.id:
        orders1 = OrderModel.objects.filter(o_status=1, user_id=user)
        return render(request, 'order/order_list_payed.html', {'orders1': orders1})
    else:
        return render(request, 'order/order_list_payed.html')


def order_wait_pay(request):
    user = request.user
    if user and user.id:
        orders1 = OrderModel.objects.filter(o_status=0, user_id=user)
        return render(request, 'order/order_list_wait_pay.html', {'orders1': orders1})
    else:
        return render(request, 'order/order_list_payed.html')


def check(request):
    if request.method == 'POST':
        users = UserModel.objects.all()
        us = []
        es = []
        for user in users:
            u = user.username
            e = user.email
            us.append(u)
            es.append(e)
        data = {
            'us': us,
            'es': es
        }
        return JsonResponse(data)
