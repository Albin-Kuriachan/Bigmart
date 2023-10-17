from django.contrib import admin

# Register your models here.
from backend.models import productdb, categorydb


admin.site.register(productdb)
admin.site.register(categorydb)