from django.db import models


# Create your models here.
class Main(models.Model):
    """
    img: 图片
    name: 分类名称
    track_id: 通用 id
    """
    img = models.CharField(max_length=256)
    name = models.CharField(max_length=128)
    track_id = models.CharField(max_length=16)

    class Meta:
        """
        抽象类：用于继承
        """
        abstract = True


class MainWheel(Main):
    """
    轮播 banner
    """

    class Meta:
        db_table = "axf_wheel"


class MainNav(Main):
    """
    导航
    """

    class Meta:
        db_table = 'axf_nav'


class MainMustBuy(Main):
    """
    必购
    """

    class Meta:
        db_table = 'axf_must_buy'


class MainShop(Main):
    """
    商店
    """

    class Meta:
        db_table = 'axf_shop'


class MainShow(Main):
    """
    主要展示商品
    img : 图片
    long_name: 图片名称
    price: 优惠价格
    market_price: 原始价格
    """
    category_id = models.CharField(max_length=16, null=True)
    brand_name = models.CharField(max_length=128, null=True)

    img1 = models.CharField(max_length=256)
    child_cid1 = models.CharField(max_length=16, null=True)
    product_id1 = models.CharField(max_length=16, null=True)
    long_name1 = models.CharField(max_length=128)
    price1 = models.FloatField(default=0)
    market_price1 = models.FloatField(default=1)

    img2 = models.CharField(max_length=256)
    child_cid2 = models.CharField(max_length=16, null=True)
    product_id2 = models.CharField(max_length=16, null=True)
    long_name2 = models.CharField(max_length=128)
    price2 = models.FloatField(default=0)
    market_price2 = models.FloatField(default=1)

    img3 = models.CharField(max_length=256)
    child_cid3 = models.CharField(max_length=16, null=True)
    product_id3 = models.CharField(max_length=16, null=True)
    long_name3 = models.CharField(max_length=128)
    price3 = models.FloatField(default=0)
    market_price3 = models.FloatField(default=1)

    class Meta:
        db_table = 'axf_mainshow'


class FoodType(models.Model):
    """
    闪购-左侧类型表
    """
    type_id = models.CharField(max_length=16)
    type_name = models.CharField(max_length=128)
    child_type_names = models.CharField(max_length=256)
    type_sort = models.IntegerField(default=1)

    class Meta:
        db_table = 'axf_foodtypes'


class Goods(models.Model):
    """
    商品
    product_id：商品编号
    product_img：商品图片
    product_name：商品名称
    product_long_name：商品规格
    specifics：规格
    price: 折后价格
    market_price: 原价
    category_id: 分类id
    child_cid: 子分类id
    child_cid_name:子分类名称
    store_nums: 名称排序
    product_num: 销量排序
    """
    product_id = models.CharField(max_length=16)
    product_img = models.CharField(max_length=256)
    product_name = models.CharField(max_length=128)
    product_long_name = models.CharField(max_length=256)
    is_xf = models.IntegerField(default=1)
    pmd_esc = models.CharField(max_length=128)
    specifics = models.CharField(max_length=128)
    price = models.FloatField(default=0)
    market_price = models.FloatField(default=1)
    # category_id = models.CharField(max_length=16)
    child_cid = models.CharField(max_length=16)
    child_cid_name = models.CharField(max_length=128)
    dealer_id = models.CharField(max_length=16)
    store_nums = models.IntegerField(default=1)
    product_num = models.IntegerField(default=1)
    category = models.ForeignKey(FoodType, null=True)

    class Meta:
        db_table = 'axf_goods'


class UserModel(models.Model):
    """
    用户信息
    username：名称
    password: 密码
    email: 邮箱
    sex: 性别 (False 代表女)
    icon: 头像
    is_delete: 是否删除
    """
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=256)
    email = models.CharField(max_length=64, unique=True)
    sex = models.BooleanField(default=False)
    icon = models.ImageField(upload_to='icons')
    is_delete = models.BooleanField(default=False)
    user_ticket = models.CharField(max_length=256, null=True)

    class Meta:
        db_table = 'axf_users'


class CarModel(models.Model):
    """
    购物车
    user: 关联用户
    goods: 关联商品
    c_num: 商品的个数
    is_select: 是否选择商品
    """
    user = models.ForeignKey(UserModel)
    goods = models.ForeignKey(Goods)
    c_num = models.IntegerField(default=1)
    is_select = models.BooleanField(default=True)

    class Meta:
        db_table = 'axf_cart'


class OrderModel(models.Model):
    """
    订单
    user: 关联用户
    o_num: 数量
    o_status: 订单状态 0代表已下单，但是未付款；1代表已付款未发货；2代表已发货已付款
    o_create: 创建时间
    """
    user = models.ForeignKey(UserModel)
    o_num = models.CharField(max_length=64)
    o_status = models.IntegerField(default=0)
    o_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'axf_order'


class OrderGoodsModel(models.Model):
    """
    订单的详细表
    goods: 关联的商品
    order： 关联的订单
    goods_num: 商品的个数
    """
    goods = models.ForeignKey(Goods)
    order = models.ForeignKey(OrderModel)
    goods_num = models.IntegerField(default=1)

    class Meta:
        db_table = 'axf_order_goods'
