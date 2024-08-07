"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from reservation.views import (
    begin_test_view,
    success
)

from personal.views import (
    home_screen_view,
    introduce_snt_view,
    curriculum_snt_view,
    schedule_snt_view,
    opinion_view,
    announce_view,

    # subpages
    c_lit_essay,
    c_cur_issue,
    c_debate,
    g6,
    g5,
    g4,
    g3,

)

from account.views import (
    registration_view,
    logout_view,
    login_view,
    account_view,
    must_authenticate_view,

)

urlpatterns = [
    path('', home_screen_view, name="home"),
    path('admin/', admin.site.urls),
   
    path('register/', registration_view, name="register"),
    path('logout/', logout_view, name="logout"),
    path('login/', login_view, name="login"),
    path('must_authenticate/', must_authenticate_view, name="must_authenticate"),
    path('account/', account_view, name="account"),
    
    path('introduce/', introduce_snt_view, name="introduce"),
    
    path('announce/', announce_view, name="announce"),
    path('announce/', include('announce.urls'), name="announce"),

    path('opinion/', opinion_view, name="opinion"),
    path('opinion/', include('blog.urls'), name="blog"),


    path('curriculum/', curriculum_snt_view, name="curriculum"),
    path('curriculum/curl', c_lit_essay, name="curl"),
    path('curriculum/curc', c_cur_issue, name="curc"),
    path('curriculum/curd', c_debate, name="curd"),

    path('schedule/', schedule_snt_view, name="schedule"),
    path('schedule/g6', g6, name="g6"),
    path('schedule/g5', g5, name="g5"),
    path('schedule/g4', g4, name="g4"),
    path('schedule/g3', g3, name="g3"),

    path('leveltest/', begin_test_view, name="leveltest"),
    path('leveltest/success', success, name="success"),


    # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
        name='password_change_done'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), 
        name='password_change'),
    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
     name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
     name='password_reset_complete'),   
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)