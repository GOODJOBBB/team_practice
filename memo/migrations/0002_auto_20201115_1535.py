# Generated by Django 3.1.2 on 2020-11-15 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='memo',
            name='URL',
            field=models.CharField(default=123, max_length=200, verbose_name='URL'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='memo',
            name='address',
            field=models.CharField(default=123, max_length=200, verbose_name='주소'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='memo',
            name='advantage',
            field=models.CharField(default=123, max_length=200, verbose_name='복리후생'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='memo',
            name='business',
            field=models.CharField(default=123, max_length=200, verbose_name='분야'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='memo',
            name='career',
            field=models.CharField(default=123, max_length=200, verbose_name='경력'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='memo',
            name='company',
            field=models.CharField(default=123, max_length=200, verbose_name='기업이름'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='memo',
            name='content',
            field=models.CharField(default=123, max_length=200, verbose_name='직무내용'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='memo',
            name='diversification',
            field=models.CharField(default=123, max_length=200, verbose_name='고용형태'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='memo',
            name='etc',
            field=models.TextField(blank=True, verbose_name='기타사항'),
        ),
        migrations.AddField(
            model_name='memo',
            name='grade',
            field=models.CharField(default=123, max_length=200, verbose_name='학력'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='memo',
            name='money',
            field=models.CharField(default=123, max_length=200, verbose_name='급여'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='memo',
            name='representative',
            field=models.CharField(default=123, max_length=200, verbose_name='대표자명'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='memo',
            name='telephone',
            field=models.CharField(default=123, max_length=200, verbose_name='전화번호'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='memo',
            name='time',
            field=models.CharField(default=123, max_length=200, verbose_name='근무시간'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='memo',
            name='type',
            field=models.CharField(default=123, max_length=200, verbose_name='직종'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='memo',
            name='volume',
            field=models.CharField(default=123, max_length=200, verbose_name='모집인원'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='memo',
            name='pic',
            field=models.ImageField(blank=True, upload_to='', verbose_name='기업로고'),
        ),
    ]
