from django.contrib import admin
from .models import PetInfo, PetCategory, Comment, Favorite

# Register your models here.


@admin.register(PetCategory)
class PetCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(PetInfo)
class PetInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    pass

