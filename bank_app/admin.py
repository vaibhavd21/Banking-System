from django.contrib import admin
from .models import Customer
from .models import History

# Register your models here.
admin.site.register(Customer)
admin.site.register(History)