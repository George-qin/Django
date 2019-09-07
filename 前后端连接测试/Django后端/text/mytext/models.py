from django.db import models

# Create your models here.

class User(models.Model):
    UserName=models.CharField(max_length=20)#用户名
    PassWord=models.CharField(max_length=20)#密码
    Sex=models.CharField(max_length=5)#性别
    Age=models.IntegerField(default=18)#年龄
    Number=models.IntegerField(default=110)#电话号码
    Content=models.CharField(max_length=100)#个人描述

class LiuYan(models.Model):
    name=models.CharField(max_length=10)
    say=models.CharField(max_length=500)
