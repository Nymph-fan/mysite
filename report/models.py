

from django.db import models

class Performset(models.Model):
    perform_id=models.IntegerField(unique=True,blank=False)
    perform_name=models.CharField(max_length=20)

    def __str__(self):
        return str(self.perform_id)+''+self.perform_name


class build(models.Model):
    build_type_choice = (
        ('k12-campus', '卡搭校园'),
        ('k12-100', '网易100分'),
        ('k12-geek', '卡搭课程'),
        ('k12-geek-mobile', '卡搭课程app'),
        ('k12-100-app', '网易100分app'),

    )

    type=models.CharField(choices=build_type_choice,max_length=64,default='k12-campus',verbose_name="项目")
    name=models.CharField(max_length=20)
    passed=models.IntegerField('通过数')
    failed=models.IntegerField('失败数')
    memo = models.TextField(null=True, blank=True, verbose_name='备注')
    build_time=models.DateTimeField('触发时间')

    def __str__(self):
        return '<%s>  %s' % (self.get_build_type_display(), self.name)
