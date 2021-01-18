from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# 로그아웃 상황일 때는 login url로 이동시켜 준다. 그래서 로그아웃 상태에서 /accounts/profile/ 접속해도 로그인 페이지로 redirect된다.
@login_required
def profile(request):
    return render(request, 'accounts/profile.html')
