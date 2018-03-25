from django.db import models

# Create your models here.


class HomeBanner(models.Model):
    class Meta:
        verbose_name = u'首页banner'
        verbose_name_plural = u'首页banner'
        db_table = 'pet_home_banner'

    title = models.CharField(u'标题', max_length=32, null=False, blank=False)
    cover = models.CharField(u'封面', max_length=256, null=False, blank=False)
    link_type = models.SmallIntegerField(u'跳转类型', null=False, blank=False)

    def __str__(self):
        pass


class BannerLinkType(models.Model):
    class Meta:
        verbose_name = u'banner跳转类型'
        verbose_name_plural = u'banner跳转类型'
        db_table = 'pet_banner_link_type'

    type_id = models.SmallIntegerField(u'', unique=True, null=False, blank=False)
    type_meta = models.CharField(u'', max_length=32, unique=True, null=False, blank=False)
    type_description = models.CharField(u'', max_length=256, null=True, blank=True)
    # time_created = models.DateTimeField(u'', )

    def __str__(self):
        pass


class HtmlCenter(models.Model):
    pass

