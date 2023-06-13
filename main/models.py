from django.db import models
from django.contrib.auth.models import Group, User


class Station(models.Model):
    station_no = models.IntegerField('Номер станции')
    location = models.CharField('Расположение станции', max_length=255)
    well_count = models.IntegerField('Количество вышек')
    director_id = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'groups__name': "director"})
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.station_no)

    class Meta:
        verbose_name = 'Станция'
        verbose_name_plural = 'Станции'


class Wells(models.Model):
    name = models.CharField('Имя скважины', max_length=50)
    st = models.BooleanField('Признак бокового ствола', default=0)
    oil_count = models.FloatField('Накоплено нефти')
    days = models.IntegerField('Дней в работе')
    in_prod = models.BooleanField('Скважина в добыче', default=0)
    wct = models.FloatField('Обводненность', max_length=11, null=True)
    bottom_perf = models.FloatField('Верх перфорации', max_length=11)
    top_perf = models.FloatField('Низ перфорации', max_length=11)
    x = models.FloatField('X')
    y = models.FloatField('Y')
    station_id = models.ForeignKey(Station, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Скважина'
        verbose_name_plural = 'Скважины'


class Well_data(models.Model):
    q_oil = models.FloatField('Дебит нефти')
    wct = models.FloatField('Обводненность', max_length=11, null=True)
    created_date = models.DateTimeField()
    well = models.ForeignKey(Wells, on_delete=models.CASCADE)

    def __str__(self):
        return self.well.name

    class Meta:
        verbose_name = 'Дебит нефти'
        verbose_name_plural = 'Дебит нефти'