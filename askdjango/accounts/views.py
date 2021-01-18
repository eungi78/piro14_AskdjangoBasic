from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login


# 로그아웃 상황일 때는 login url로 이동시켜 준다. 그래서 로그아웃 상태에서 /accounts/profile/ 접속해도 로그인 페이지로 redirect된다.
@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # 이 시점이 db 저장
            # 이 시점에서 회원가입하면 자동 로그인 처리하기
            # django/contrib/auth/LoginView에 form_valid가 있음.
            # 이는 form.is_valid일 때 호출되는 함수
            # import하고, form_valid인자로 request와 user를 넘겨주면 로그인 시킴
            auth_login(request, user)
            # return redirect('login')
            return redirect('profile')  # 회원가입하면 profile로 바로 이동
    else:
        form = UserCreationForm()
    return render(request, "accounts/signup.html/", {'form': form, })

# CBV
# from django.views.generic import CreateView
# from django.contrib.auth.models import User
# from django.conf import settings


# signup = CreateView.as_view(model=User, form_class=UserCreationForm, success_url='settings.LOGIN_URL', template_name='accounts/signup.html')


# 회원가입하면 자동 로그인
# class SignupView(CreateView):
#     model=User
#     form_class=SignupForm
#     template_name="accounts/signup.html"

#     def get_success_url(self):
#         return resolve_url('profile') # import 해야함

#     def form_valid(self,form):
#         user=form.save()
#         auth_login(self.request,user)
#         return redirect('profile')

# signup=SignupView.as_view()
