# Generated by Django 2.0.3 on 2018-03-21 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PetUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_phone', models.CharField(max_length=20, unique=True, verbose_name='手机号')),
                ('password', models.CharField(blank=True, max_length=256, verbose_name='密码')),
                ('gender', models.SmallIntegerField(default=0, verbose_name='性别')),
                ('signature', models.CharField(blank=True, max_length=32, verbose_name='个性签名')),
                ('last_login', models.DateTimeField(verbose_name='上次登录')),
                ('is_deleted', models.SmallIntegerField(default=0, verbose_name='删除状态')),
                ('is_blocked', models.SmallIntegerField(default=0, verbose_name='被禁状态')),
                ('time_created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': 'app用户',
                'db_table': 'pet_user',
                'verbose_name_plural': 'app用户',
            },
        ),
    ]
