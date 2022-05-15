from django.db import models

class Contact(models.Model):
    email = models.EmailField(verbose_name='下单人邮箱地址')
    po_number = models.CharField(max_length=10, verbose_name="销售单号（'7'开头）")
    client=models.CharField(max_length=20, verbose_name='客户', blank=True)
    salesperson=models.CharField(max_length=10, verbose_name='销售人员', blank=True)

    offices=[
        ('bj', '北京'),
        ('sh', '上海'),
        ('gz', '广州'),
        ('cd', '成都')
    ]
    office=models.CharField(max_length=20, choices=offices, verbose_name='分公司', blank=True)

    def __str__(self):
        return self.email
