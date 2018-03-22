from django.contrib import admin
from .models import PetUser

# Register your models here.


@admin.register(PetUser)
class PetUserAdmin(admin.ModelAdmin):
    pass
