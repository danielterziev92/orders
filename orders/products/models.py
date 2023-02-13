from django.db import models
from mptt import fields as mpttfields
from mptt import models as mpttmodel
from orders.common.models import AuditInfoMixin


class Category(AuditInfoMixin, mpttmodel.MPTTModel):
    TITLE_MAX_LENGTH = 30

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        null=False,
        blank=False,
    )

    parent = mpttfields.TreeForeignKey(
        'self',
        on_delete=models.RESTRICT,
        related_name='child',
        null=False,
        blank=False,
    )

    is_active = models.BooleanField(
        default=True,
        null=False,
        blank=False,
    )


class Product(models.Model):
    TITLE_MAX_LENGTH = 30

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

    multiple_amount = models.PositiveIntegerField(
        verbose_name='Кратно количество',
        null=False,
        blank=False,
    )

    image = models.ImageField(
        upload_to='product/',
        null=False,
        blank=False,
    )
