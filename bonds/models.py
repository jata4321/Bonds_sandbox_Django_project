from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
import QuantLib as ql
from datetime import date

# Create your models here.
class Bond(models.Model):

    ISIN = models.CharField(max_length=12)
    name = models.CharField(max_length=100)
    issue_price = models.DecimalField(max_digits=10, decimal_places=4, default=100)
    issue_date = models.DateField(default=date.today)
    maturity_date = models.DateField()
    coupon_rate = models.DecimalField(max_digits=5, decimal_places=3)
    coupon_frequency = models.SmallIntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(12)
        ]
    )
    redemption = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def clean(self):
        if self.issue_date >= self.maturity_date:
            raise ValidationError('Issue date must be earlier than maturity date.')

    def deactivate(self):
        if self.maturity_date < date.today():
            self.is_active = False
            self.save()


class BondPrice(models.Model):

    calendar = ql.Poland()
    settlement_days = '2D'
    settlement_date = calendar.advance(ql.Date.todaysDate(), ql.Period(settlement_days)).ISO()

    bond = models.ForeignKey(Bond, on_delete=models.CASCADE, related_name='prices')
    price = models.DecimalField(max_digits=10, decimal_places=4)
    date = models.DateField(default=settlement_date)

    def __str__(self):
        return self.bond.name

    class Meta:
        ordering = ['date']
        unique_together = ('price', 'date')