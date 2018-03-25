from django.contrib import admin
from .models import HomeBanner, HtmlCenter, BannerLinkType

# Register your models here.


@admin.register(HomeBanner)
class HomeBannerAdmin(admin.ModelAdmin):
    pass


@admin.register(HtmlCenter)
class HtmlCenterAdmin(admin.ModelAdmin):
    pass


@admin.register(BannerLinkType)
class BannerLinkTypeAdmin(admin.ModelAdmin):
    pass
