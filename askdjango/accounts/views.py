from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


# 로그아웃 상황일 때는 login url로 이동시켜 준다. 그래서 로그아웃 상태에서 /accounts/profile/ 접속해도 로그인 페이지로 redirect된다.
@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, "accounts/signup.html/", {'form': form, })

# CBV
# from django.views.generic import CreateView
# from django.contrib.auth.models import User
# from django.conf import settings

# signup = CreateView.as_view(model=User, form_class=UserCreationForm, success_url='settings.LOGIN_URL', template_name='accounts/signup.html')
