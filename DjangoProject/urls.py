"""
URL configuration for DjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.urls import path
from . import views #导入views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path（route:‘路由名称/’，‘试图/试图函数’，name="路由说明")
    path("hello/", views.hello, name='first'),
    path("",views.index,name="first view"),#不写任何路由时，表示默认访问地址127.0.0.1:8000
    path("red_balls_top10/",views.red_balls_top10,name="red_balls"),
    path("blue_ball_top8/",views.blue_ball_top8,name="blue_ball_top8"),
    path("every_red_ball_top1/",views.every_red_ball_top1,name="every_blue_balltop1"),
    path("cold_hot_ball/",views.cold_hot_ball,name="cold_hot_ball_analysis"),
    path("red_ball_event/",views.red_ball_event,name="红球奇偶比分布"),
    path("first_and_second_prizes/",views.first_and_second_prizes,name="first_and_second_prizes"),
    path('sales_trend/', views.sales_trend, name="sales_trend"),
    path("red1_all_freq/", views.red1_all_freq, name="红1球整体出现频次分布"),
]
"""
访问路由，启动django服务，用127.0.0.1:8000/路由?参数（有则写）
"""
