"""为应用程序users定义URL模式"""

from django.conf.urls import url
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    #登陆页面,1.0为login,2.0为LoginView
    url(r'^login/$',LoginView.as_view(template_name='users/login.html'),
        name='login'),

    #注销
    url(r'^logout/$',views.logout_view,name='logout'),

    #注册页面
    url(r'^register$',views.register,name='register'),
]
app_name = 'login'
