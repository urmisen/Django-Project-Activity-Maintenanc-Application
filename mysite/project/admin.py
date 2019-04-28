from django.contrib import admin
from .models import *
from .models import CT_Marks


admin.site.register(CT_Marks)
admin.site.register(Profile)
admin.site.register(Personal_data)

