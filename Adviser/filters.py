from django_filters import filters, FilterSet
from .models import Attitude


class MyOrderingFilter(filters.OrderingFilter):
    descending_fmt = '%s (降順)'


class AttitudeFilter(FilterSet):
    declaration = filters.CharFilter(name='declaration', label='心がけ', lookup_expr='contains')
    situation = filters.CharFilter(name='situation', label='心がけるべき状況', lookup_expr='contains')
    wrong_action = filters.CharFilter(name='wrong_action', label='間違って取る行動例', lookup_expr='contains')
    reason = filters.CharFilter(name='reason', label='心がけて実践すべき端的な理由', lookup_expr='contains')

    order_by = MyOrderingFilter(
        # tuple_mapping retains-order
        fields=(
            ('adopted_date', 'adopted_date'),
            ('timing', 'timing'),
            ('frequency', 'frequency'),
            ('total_succeeded_point', 'total_succeeded_point'),
            ('practiced_rate', 'practiced_rate'),
        ),
        field_labels={
            'adopted_date': '心がけ採用日',
            'timing': '意識すべきだったタイミング数',
            'frequency': '要意識頻度',
            'total_succeeded_point': '累積成功ポイント',
            'practiced_rate': '実践成功率',
        },
        label='並べ替え'
    )

    class Meta:
        model = Attitude
        fields = ('declaration', 'situation', 'wrong_action', 'reason',)
