from django.db import models


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
