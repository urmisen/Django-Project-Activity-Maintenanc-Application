"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from .views import *

from django.conf import settings
from django.conf.urls.static import static
from teacher import views as t_views
from project import views as p_views
from student import views as s_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('about/',about),
    path('contact/',contact),

    path('login/', s_views.login_view, name='login'),
    path('register/', s_views.register_view, name='register'),
    path('logout/', s_views.logout_view, name='logout'),
    path('home/', s_views.home, name='home'),
    path('profile/', s_views.profile, name='profile'),
    path('update/', s_views.update, name='update'),
    path('ct_marks/', s_views.ct_marks, name='ct_marks'),
    path('s_about/', s_views.about, name='s_about'),
    path('s_contact/', s_views.contact, name='s_contact'),


    path('CHEM_1113/', s_views.CHEM_1113, name='CHEM_1113'),
    path('CSE_1101/', s_views.CSE_1101, name='CSE_1101'),
    path('EEE_1151/', s_views.EEE_1151, name='EEE_1151'),
    path('MATH_1113/', s_views.MATH_1113, name='MATH_1113'),
    path('HUM_1113/', s_views.HUM_1113, name='HUM_1113'),
    path('CSE_1201/', s_views.CSE_1201, name='CSE_1201'),
    path('CSE_1203/', s_views.CSE_1203, name='CSE_1203'),
    path('MATH_1213/', s_views.MATH_1213, name='MATH_1213'),
    path('HUM_1213/', s_views.HUM_1213, name='HUM_1213'),
    path('PHY_1213/', s_views.PHY_1213, name='PHY_1213'),
    path('CSE_2101/', s_views.CSE_2101, name='CSE_2101'),
    path('CSE_2103/', s_views.CSE_2103, name='CSE_2103'),
    path('EEE_2151/', s_views.EEE_2151, name='EEE_2151'),
    path('MATH_2113/', s_views.MATH_2113, name='MATH_2113'),
    path('HUM_2113/', s_views.HUM_2113, name='HUM_2113'),
    path('CSE_2201/', s_views.CSE_2201, name='CSE_2201'),
    path('CSE_2203/', s_views.CSE_2203, name='CSE_2203'),
    path('CSE_2205/', s_views.CSE_2205, name='CSE_2205'),
    path('EEE_2251/', s_views.EEE_2251, name='EEE_2251'),
    path('MATH_2213/', s_views.MATH_2213, name='MATH_2213'),
    path('CSE_3101/', s_views.CSE_3101, name='CSE_3101'),
    path('CSE_3103/', s_views.CSE_3103, name='CSE_3103'),
    path('CSE_3105/', s_views.CSE_3105, name='CSE_3105'),
    path('CSE_3107/', s_views.CSE_3107, name='CSE_3107'),
    path('CSE_3109/', s_views.CSE_3109, name='CSE_3109'),
    path('CSE_3201/', s_views.CSE_3201, name='CSE_3201'),
    path('CSE_3203/', s_views.CSE_3203, name='CSE_3203'),
    path('CSE_3205/', s_views.CSE_3205, name='CSE_3205'),
    path('CSE_3207/', s_views.CSE_3207, name='CSE_3207'),
    path('CSE_3209/', s_views.CSE_3209, name='CSE_3209'),
    path('CSE_4101/', s_views.CSE_4101, name='CSE_4101'),
    path('CSE_4103/', s_views.CSE_4103, name='CSE_4103'),
    path('CSE_4105/', s_views.CSE_4105, name='CSE_4105'),
    path('CSE_4107/', s_views.CSE_4107, name='CSE_4107'),
    path('CSE_4109/', s_views.CSE_4109, name='CSE_4109'),
    path('CSE_4201/', s_views.CSE_4201, name='CSE_4201'),
    path('CSE_4203/', s_views.CSE_4203, name='CSE_4203'),
    path('CSE_4205/', s_views.CSE_4205, name='CSE_4205'),
    path('CSE_4207/', s_views.CSE_4207, name='CSE_4207'),
    path('CSE_4209/', s_views.CSE_4209, name='CSE_4209'),

    path('t_home/', t_views.t_home, name='t_home'),
    path('t_login/', t_views.login_view, name='t_login'),
    path('t_register/', t_views.register_view, name='t_register'),
    path('t_logout/', t_views.logout_view, name='t_logout'),
    path('t_profile/', t_views.profile, name='t_profile'),
    path('t_update/', t_views.update, name='t_update'),
    path('t_ct_marks/', t_views.ct_marks, name='t_ct_marks'),
    path('edit_marks/(?P<pk>\d+)', t_views.edit_marks, name='edit_marks'),
    path('delete_marks/(?P<pk>\d+)', t_views.delete_marks, name='delete_marks'),
    path('add_marks/', t_views.add_marks, name='add_marks'),
    path('t_about/', t_views.about, name='t_about'),
    path('t_contact/', t_views.contact, name='t_contact'),

    path('tCHEM_1113/', t_views.CHEM_1113, name='tCHEM_1113'),
    path('tCSE_1101/', t_views.CSE_1101, name='tCSE_1101'),
    path('tEEE_1151/', t_views.EEE_1151, name='tEEE_1151'),
    path('tMATH_1113/', t_views.MATH_1113, name='tMATH_1113'),
    path('tHUM_1113/', t_views.HUM_1113, name='tHUM_1113'),
    path('tCSE_1201/', t_views.CSE_1201, name='tCSE_1201'),
    path('tCSE_1203/', t_views.CSE_1203, name='tCSE_1203'),
    path('tMATH_1213/', t_views.MATH_1213, name='tMATH_1213'),
    path('tHUM_1213/', t_views.HUM_1213, name='tHUM_1213'),
    path('tPHY_1213/', t_views.PHY_1213, name='tPHY_1213'),
    path('tCSE_2101/', t_views.CSE_2101, name='tCSE_2101'),
    path('tCSE_2103/', t_views.CSE_2103, name='tCSE_2103'),
    path('tEEE_2151/', t_views.EEE_2151, name='tEEE_2151'),
    path('tMATH_2113/', t_views.MATH_2113, name='tMATH_2113'),
    path('tHUM_2113/', t_views.HUM_2113, name='tHUM_2113'),
    path('tCSE_2201/', t_views.CSE_2201, name='tCSE_2201'),
    path('tCSE_2203/', t_views.CSE_2203, name='tCSE_2203'),
    path('tCSE_2205/', t_views.CSE_2205, name='tCSE_2205'),
    path('tEEE_2251/', t_views.EEE_2251, name='tEEE_2251'),
    path('tMATH_2213/', t_views.MATH_2213, name='tMATH_2213'),
    path('tCSE_3101/', t_views.CSE_3101, name='tCSE_3101'),
    path('tCSE_3103/', t_views.CSE_3103, name='tCSE_3103'),
    path('tCSE_3105/', t_views.CSE_3105, name='tCSE_3105'),
    path('tCSE_3107/', t_views.CSE_3107, name='tCSE_3107'),
    path('tCSE_3109/', t_views.CSE_3109, name='tCSE_3109'),
    path('tCSE_3201/', t_views.CSE_3201, name='tCSE_3201'),
    path('tCSE_3203/', t_views.CSE_3203, name='tCSE_3203'),
    path('tCSE_3205/', t_views.CSE_3205, name='tCSE_3205'),
    path('tCSE_3207/', t_views.CSE_3207, name='tCSE_3207'),
    path('tCSE_3209/', t_views.CSE_3209, name='tCSE_3209'),
    path('tCSE_4101/', t_views.CSE_4101, name='tCSE_4101'),
    path('tCSE_4103/', t_views.CSE_4103, name='tCSE_4103'),
    path('tCSE_4105/', t_views.CSE_4105, name='tCSE_4105'),
    path('tCSE_4107/', t_views.CSE_4107, name='tCSE_4107'),
    path('tCSE_4109/', t_views.CSE_4109, name='tCSE_4109'),
    path('tCSE_4201/', t_views.CSE_4201, name='tCSE_4201'),
    path('tCSE_4203/', t_views.CSE_4203, name='tCSE_4203'),
    path('tCSE_4205/', t_views.CSE_4205, name='tCSE_4205'),
    path('tCSE_4207/', t_views.CSE_4207, name='tCSE_4207'),
    path('tCSE_4209/', t_views.CSE_4209, name='tCSE_4209'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
