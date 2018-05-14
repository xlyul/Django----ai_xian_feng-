from django.conf.urls import url
from home import views

urlpatterns = [
    url(r'^home/', views.home, name='home'),
    url(r'^login/', views.login, name='login'),
    url(r'^regist/', views.regist, name='regist'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^mine/', views.mine, name='mine'),
    url(r'^cart/', views.cart, name='cart'),
    url(r'^market/$', views.market, name='market'),
    url(r'^market/(\d+)/(\S+)/(\d+)/', views.market_show, name='market_show'),
    url(r'^check/',views.check),
    # 订单相关
    url(r'^order/(\d+)/', views.order, name='order'),
    # # 修改订单状态
    url(r'^order_pay/(\d+)/', views.order_pay, name='order_pay'),
    url(r'^orderlist/', views.order_list, name='order_list'),
    url(r'^orderlistwaitpay/', views.order_wait_pay),
    # 添加商品到购物车及购物车内商品数量增减
    url(r'^add_goods/', views.add_goods),
    url(r'^sub_goods/', views.sub_goods),
    # 购物车内商品是否勾选
    url(r'^user_select/',views.user_select),
    url(r'^allchange1/',views.all_change1),
    url(r'^allchange2/',views.all_change2),
    url(r'^generateOrder/', views.user_generate_order, name='user_order'),
    url(r'^result/', views.result)
]
