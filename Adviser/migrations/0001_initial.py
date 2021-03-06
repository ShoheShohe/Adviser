# Generated by Django 2.0.7 on 2018-07-08 07:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attention',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('declaration', models.TextField(max_length=50, verbose_name='心がけ')),
                ('situation', models.TextField(max_length=200, verbose_name='心がけるべき状況')),
                ('wrong_action', models.TextField(max_length=200, verbose_name='間違って取る行動例')),
                ('reason', models.TextField(max_length=100, verbose_name='そうすべき端的な理由')),
                ('logic', models.TextField(max_length=300, verbose_name='理由の論証')),
                ('draft_logic', models.TextField(max_length=1000, verbose_name='論証の下書き')),
                ('adopted_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='心がけ採用日')),
                ('frequency', models.FloatField(default=0, verbose_name='意識すべき出来事が起こる頻度')),
                ('practiced_rate', models.FloatField(default=0, verbose_name='実践頻度')),
                ('maker', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作成者')),
            ],
        ),
    ]
