from django.shortcuts import render,HttpResponseRedirect,reverse
from django.contrib.auth.backends import ModelBackend
from apps.users.models import UserProfile
from django.db.models import Q
from django.views import View
from apps.users.forms import LoginForm
from django.contrib.auth import authenticate,login
# Create your views here.
class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            # 通过username或email查询用户
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            # 判断密码是否一致
            if user.check_password(password):
                return user
        except Exception as e:
            return None

class LoginView(View):
    def get(self, request):
        return render(request, "users/login.html", {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse("index"))
                else:
                    return render(request, "users/login.html", {"msg":"用户未激活！"})
            else:
                return render(request, "users/login.html", {"msg":"用户名或密码错误！"})
        else:
            return render(request, "users/login.html", {"login_form":login_form})