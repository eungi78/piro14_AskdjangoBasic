from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
]
# cbv에서는 template 연결을 이런 식으로 한다.
# 설정해주지 않으면 default로 class LoginView의 registration/login.html 로 설정이 되어 있는데,
# 이 경로에 만들어줘도 된다.

# accounts/login이라고 설정한 이유는 있다.
# 만약 blog 앱의 views.py에서
#
# from django.contrib.auth.decorators import login_required
# @login_required
# def post_new(request):
# pass

# 라고 했을 때, 로그인이 안 되어 있을 때는
# django/conf/global_settings.py에 있는
# LOGIN_URL = '/accounts/login/' 쪽으로 간다.
# 그렇기 때문에 앱이름도 accounts, projects url도 accounts라고 설정한 것.

# 여기서 superuser로 로그인 하면 page not found하면서 url이 /accounts/profile/이 뜨는데,
# 이는 디폴트로 아래와 같이 설정되어 있기 때문이다.
# LOGIN_REDIRECT_URL = '/accounts/profile/'

# reverse_lazy(): settings에 reverse가 있으면 초기화되는 과정에서 url reverse를 하기 때문에 실패하게 됨
# 그래서 이는 reverse_lazy는 실제 url을 참조하게 될 때 사용하게 됨. 게으르게.
# 그렇기에 global_settings에 reverse를 사용할 때는 reverse_lazy사용
# -->
# LOGIN_URL = '/accounts/login/'
# LOGIN_URL = reverse_lazy('login')

# LOGIN_REDIRECT_URL = '/accounts/profile/'
# LOGIN_REDIRECT_URL = reverse_lazy('profile')
