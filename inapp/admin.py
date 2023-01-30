from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustUser, TopLid


# Register your models here.
admin.site.register(CustUser, UserAdmin)
admin.site.register(TopLid)