# Generated by Django 2.1.3 on 2020-05-10 04:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoardModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('structure', models.CharField(max_length=40)),
                ('age', models.CharField(max_length=20)),
                ('pref', models.CharField(max_length=100)),
                ('town', models.CharField(max_length=100)),
                ('roof', models.CharField(max_length=50, verbose_name='住所')),
                ('address', models.CharField(max_length=50, verbose_name='住所')),
                ('age2', models.CharField(max_length=20)),
                ('type', models.CharField(choices=[('建築物', '建築物'), ('土木構造物', '土木構造物'), ('その他工作物', 'その他工作物')], max_length=10, verbose_name='種別')),
                ('type2', models.CharField(choices=[('文化福祉', '文化福祉'), ('官公庁社', '官公庁社'), ('生活関連', '生活関連'), ('学校', '学校'), ('交通', '交通'), ('住宅', '住宅'), ('宗教', '宗教'), ('産業1次', '産業1次'), ('産業2次', '産業2次'), ('産業3次', '産業3次'), ('その他', 'その他')], max_length=10, verbose_name='種別')),
                ('owner', models.CharField(max_length=100)),
                ('standard', models.CharField(choices=[('文化福祉', '文化福祉'), ('官公庁社', '官公庁社'), ('生活関連', '生活関連'), ('学校', '学校'), ('交通', '交通'), ('住宅', '住宅'), ('宗教', '宗教'), ('産業1次', '産業1次'), ('産業2次', '産業2次'), ('産業3次', '産業3次'), ('その他', 'その他')], max_length=20, verbose_name='基準')),
                ('memo', models.TextField()),
                ('others', models.TextField()),
                ('architect', models.CharField(max_length=100)),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
                ('editer', models.CharField(max_length=20, verbose_name='作成者')),
            ],
        ),
    ]
