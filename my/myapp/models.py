from django.db import models

# Create your models here.
from datetime import *

class person(models.Model):
    pname=models.CharField(max_length=20)
    page=models.IntegerField()
    pcontend=models.CharField(max_length=50)

    #内置类排序
    # class Meta:
    #     ordering=['id','page']


class skill(models.Model):
    sname=models.CharField(max_length=20)
    sshnaghai=models.IntegerField()
    ssort=models.CharField(max_length=20)
    sperson=models.ForeignKey("person",on_delete=models.CASCADE)

class username(models.Model):
    UserName=models.CharField(max_length=40)

class password(models.Model):
    PassWord=models.CharField(max_length=20)
    puser=models.ForeignKey("username",on_delete=models.CASCADE)


"""
p1=person()
p1.pname="秦翼飞"
p1.page=19
p1.pcontend="临桂三中第一球王"
p1.save()


s1=skill()
s1.sname="旋球"
s1.sshnaghai=1000
s1.ssort="法术攻击"
s1=p1
s1.save()
"""

