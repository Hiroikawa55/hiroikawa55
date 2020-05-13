from django.db import models
from django.utils import timezone

# Create your models here.
CHOICES = [
        ('建築物', '建築物'),
        ('土木構造物', '土木構造物'),
        ('その他工作物', 'その他工作物'),
    ]

CHOICES2 = [
        ('文化福祉', '文化福祉'),
        ('官公庁社', '官公庁社'),
        ('生活関連', '生活関連'),
        ('学校', '学校'),
        ('交通', '交通'),
        ('住宅', '住宅'),
        ('宗教', '宗教'),
        ('産業1次', '産業1次'),
        ('産業2次', '産業2次'),
        ('産業3次', '産業3次'),
        ('その他', 'その他'),
    ]


class BoardModel(models.Model):
    name = models.CharField(verbose_name='名称', max_length=100)
    structure = models.CharField(verbose_name='構造', max_length=40)
    age = models.CharField(verbose_name='和暦', max_length=20)
    age2 = models.CharField(verbose_name='西暦', max_length=20)
    pref = models.CharField(verbose_name='都道府県', max_length=100)
    town = models.CharField(verbose_name='市町村', max_length=100)
    address = models.CharField(verbose_name='住所', max_length=50)
    roof = models.CharField(verbose_name='屋根', max_length=50)
    type = models.CharField(verbose_name="種別",max_length=10,choices=CHOICES)
    type2 = models.CharField(verbose_name="分類",max_length=10,choices=CHOICES2)
    standard = models.CharField(verbose_name="基準",max_length=20,choices=CHOICES2)
    memo = models.TextField(verbose_name="説明")
    others = models.TextField(verbose_name="備考")
    architect = models.CharField(verbose_name="設計者",max_length=100)
    data = models.DateTimeField(verbose_name="登録年月日",default=timezone.now)
    editer  = models.CharField(verbose_name="編集",max_length=20)