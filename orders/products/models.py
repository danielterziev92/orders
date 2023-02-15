from django.db import models
from orders.common.models import AuditInfoMixin


class Town(AuditInfoMixin, models.Model):
    TITLE_MAX_LENGTH = 30

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        verbose_name='Име',
        null=False,
        blank=False,
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name='Активен',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Град"
        verbose_name_plural = "Градове"

    def __str__(self):
        return f'{self.title}'


class Product(AuditInfoMixin, models.Model):
    TITLE_MAX_LENGTH = 30
    IMAGE_MAX_LENGTH = 10

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        verbose_name='Име',
        null=False,
        blank=False,
    )

    quantity = models.PositiveIntegerField(
        verbose_name='Количество',
        null=False,
        blank=False,
    )

    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name='Цена',
        null=False,
        blank=False
    )

    multiple_amount = models.PositiveIntegerField(
        verbose_name='Кратно количество',
        null=False,
        blank=False,
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукти'
