from django.contrib import admin
from .models import PetInfo

# Register your models here.


@admin.register(PetInfo)
class PetInfoAdmin(admin.ModelAdmin):
    pass
