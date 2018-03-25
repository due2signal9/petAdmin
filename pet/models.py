from django.db import models

# Create your models here.


class PetCategory(models.Model):
    class Meta:
        verbose_name = u'宠物类别'
        verbose_name_plural = u'宠物类别'
        db_table = 'pet_category'

    sort_id = models.IntegerField(u'排序id', default=0, null=False, blank=False)
    name = models.CharField(u'类别名', max_length=32, unique=True, default=u'未知', null=False, blank=False)
    cover = models.CharField(u'封面', max_length=256, default=None, null=True, blank=True)
    time_created = models.DateTimeField(u'创建时间', auto_now_add=True)

    def __str__(self):
        pass


class PetInfo(models.Model):
    class Meta:
        verbose_name = u'宠物信息'
        verbose_name_plural = u'宠物信息'
        db_table = 'pet_pet_info'

    title = models.CharField(u'标题', max_length=64, null=False, blank=False)
    # district = models.CharField(u'', max_length=64, null=False, blank=False)
    description = models.CharField(u'详情描述', max_length=256, null=True, blank=True)
    image1 = models.CharField(u'图片描述1', max_length=256, null=False, blank=False)
    image2 = models.CharField(u'图片描述2', max_length=256, null=False, blank=False)
    image3 = models.CharField(u'图片描述3', max_length=256, null=False, blank=False)
    comment_count = models.IntegerField(u'', default=0)
    # comments =
    is_blocked = models.SmallIntegerField(u'被禁状态', default=0)
    is_deleted = models.SmallIntegerField(u'删除状态', default=0)
    time_created = models.DateTimeField(u'创建时间', auto_now_add=True)

    def __str__(self):
        pass


class Comment(models.Model):
    class Meta:
        verbose_name = u'评论'
        verbose_name_plural = u'评论'
        db_table = 'pet_comment'

    #pet_info_id =
    #from_user_id =
    #parent_id =
    #to_comment_id =
    content = models.CharField(u'评论内容', max_length=140, null=False, blank=False)
    is_blocked = models.SmallIntegerField(u'被禁状态', default=0)
    is_deleted = models.SmallIntegerField(u'删除状态', default=0)
    time_created = models.DateTimeField(u'创建时间', auto_now_add=True)

    def __str__(self):
        pass


class Favorite(models.Model):
    class Meta:
        verbose_name = u'收藏'
        verbose_name_plural = u'收藏'
        db_table = 'pet_favorite'

    #pet_info_id =
    #from_user_id =
    time_created = models.DateTimeField(u'创建时间', auto_now_add=True)

    def __str__(self):
        pass

