from django.db import models

# Create your models here.


class PetUser(models.Model):
    class Meta:
        verbose_name = u'app用户'
        verbose_name_plural = u'app用户'
        db_table = 'pet_user'

    login_phone = models.CharField(u'手机号', max_length=20, unique=True, null=False, blank=False)
    password = models.CharField(u'密码', max_length=256, null=True, blank=False)
    gender = models.SmallIntegerField(u'性别', default=0)
    signature = models.CharField(u'个性签名', max_length=32, blank=True, null=True)
    last_login = models.DateTimeField(u'上次登录', null=True)
    is_deleted = models.SmallIntegerField(u'删除状态', default=0)
    is_blocked = models.SmallIntegerField(u'被禁状态', default=0)
    time_created = models.DateTimeField(u'创建时间', auto_now_add=True)

    def __str__(self):
        pass



