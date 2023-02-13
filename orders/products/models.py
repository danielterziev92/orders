from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class AuditInfoMixin(models.Model):
    created_on = models.DateField(
        auto_now_add=True,
        verbose_name='Дата на създаване'
    )

    updated_on = models.DateTimeField(
        auto_now=True,
        verbose_name='Последна модификация'
    )

    class Meta:
        abstract = True


class Category(AuditInfoMixin, MPTTModel):
    TITLE_MAX_LENGTH = 30

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        null=False,
        blank=False,
    )

    parent = TreeForeignKey(
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
