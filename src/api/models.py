from django.db import models


class Item(models.Model):
    CURRENCY_CHOICES = (
        ('USD', 'USD'),
        ('EUR', 'EUR'),
        ('RUB', 'RUB'),
    )
    name = models.CharField(max_length=300)
    description = models.TextField()
    price = models.PositiveIntegerField()
    currency = models.CharField(
        default='USD',
        choices=CURRENCY_CHOICES,
        max_length=3
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name
