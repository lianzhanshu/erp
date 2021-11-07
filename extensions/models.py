from django.db.models import CharField, DateField, DateTimeField, JSONField, FileField, ImageField
from django.db.models import BooleanField, IntegerField, FloatField, DecimalField
from django.db.models.deletion import CASCADE, SET_NULL, SET_DEFAULT, PROTECT
from django.db.models import OneToOneField, ForeignKey, ManyToManyField
from django.db.models import Model, IntegerChoices, TextChoices
from django.db.models import Sum, Count, Value, F, Q, Prefetch
from django.db.models.functions import Coalesce
from django.db import transaction, connection


class ModelMixin():

    def validate(self):
        """验证"""


class AmountField(DecimalField):
    """金额字段"""

    def __init__(self, verbose_name=None, name=None, **kwargs):
        kwargs['max_digits'], kwargs['decimal_places'] = 16, 2
        super().__init__(verbose_name, name, **kwargs)


__all__ = [
    'Model', 'ModelMixin', 'IntegerChoices', 'TextChoices',
    'CASCADE', 'SET_NULL', 'SET_DEFAULT', 'PROTECT',
    'OneToOneField', 'ForeignKey', 'ManyToManyField',
    'BooleanField', 'IntegerField', 'FloatField', 'DecimalField', 'AmountField',
    'CharField', 'DateField', 'DateTimeField', 'JSONField', 'FileField', 'ImageField',
    'Sum', 'Count', 'Value', 'F', 'Q', 'Prefetch', 'Coalesce', 'transaction', 'connection',
]