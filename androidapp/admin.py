from django.contrib import admin
from .models import TitleModel, DescModel
# Register your models here.
admin.site.register(TitleModel)
admin.site.register(DescModel)
