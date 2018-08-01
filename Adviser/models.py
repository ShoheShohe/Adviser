from django.db import models
from django.core import validators
from django.utils import timezone
from django.contrib.auth import get_user_model

from users.models import User

# Create your models here.


class Attitude(models.Model):

    declaration = models.TextField(
        verbose_name='心がけ',
        max_length=50,
    )

    situation = models.TextField(
        verbose_name='心がけるべき状況',
        max_length=200,
    )

    wrong_action = models.TextField(
        verbose_name='間違って取る行動例',
        max_length=200,
    )

    reason = models.TextField(
        verbose_name='心がけて実践すべき端的な理由',
        max_length=100,
    )

    logic = models.TextField(
        verbose_name='理由の論証',
        max_length=300,
    )

    draft_logic = models.TextField(
        verbose_name='論証の下書き',
        max_length=1000,
    )

    maker = models.ForeignKey(
        'users.User',
        verbose_name='作成者',
        on_delete=models.CASCADE,
        default=get_user_model(),
    )
    # CASCADEではなく、SET_DEFAULTにして「削除されたユーザー」をセットできるようにすべき

    adopted_date = models.DateTimeField(
        verbose_name='心がけ採用日',
        default=timezone.now,
    )

    timing = models.IntegerField(
        verbose_name='意識すべきだったタイミング数',
        default=0,
    )

    frequency = models.FloatField(
        verbose_name='要意識頻度',
        default=0,
    )

    total_succeeded_point =models.IntegerField(
        verbose_name='累積成功ポイント',
        default=0,
    )

    practiced_rate = models.FloatField(
        verbose_name='実践成功率',
        default=0,
    )

    def __str__(self):
        return self.declaration
