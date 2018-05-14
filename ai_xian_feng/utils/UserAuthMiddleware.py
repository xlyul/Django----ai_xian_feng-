from datetime import datetime

from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin

from home.models import UserModel


class AuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # if request.path == '/axf/login/' or request.path == '/axf/regist/' or \
        #         request.path == '/axf/home/' or request.path == '/axf/mine/' or \
        #         request.path == '/axf/logout/':
        #     return None
        #
        # ticket = request.COOKIES.get('ticket')
        # if not ticket:
        #     return HttpResponseRedirect('/axf/login/')
        #
        # user = UserModel.objects.filter(user_ticket=ticket)
        # if not user:
        #     return HttpResponseRedirect('/axf/login/')
        #
        # request.user = user[0]
        ticket = request.COOKIES.get('ticket')
        user = UserModel.objects.filter(user_ticket=ticket).first()
        request.user = user

        if not ticket:
            return None

            # 判断令牌是否有效，无效则删除
            # out_time = user[0].out_time.replace(tzinfo=None) # replace 时区转换转换，减去8小时
            # now_time = datetime.utcnow()
            #
            # if out_time > now_time:
            #     # 没有失效
            # request.user = user[0].user
            # else:
            #     user.delete()