from django.db import models

# Create your models here.


class PetInfo(models.Model):
    class Meta:
        verbose_name = u'宠物信息'
        verbose_name_plural = u'宠物信息'
        db_table = 'pet_petInfo'

    is_blocked = models.SmallIntegerField(u'被禁状态', default=0)
    is_deleted = models.SmallIntegerField(u'删除状态', default=0)
    time_created = models.DateTimeField(u'创建时间', auto_now_add=True)

    def __str__(self):
        pass

