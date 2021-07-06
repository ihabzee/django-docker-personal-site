from django.contrib.admin import AdminSite
from django.contrib.auth.forms import AuthenticationForm

# Register your models here.

class MyAdminSite(AdminSite):
    
    login_template = 'admin/login.html'

site = MyAdminSite()