from django.db import models
import QuantLib as ql

# Create your models here.
class Bond(models.Model):

    ISIN = models.CharField(max_length=12)
    name = models.CharField(max_length=100)
    issue_price = models.DecimalField(max_digits=10, decimal_places=4)
    issue_date = models.DateField()
    maturity_date = models.DateField()
    coupon_rate = models.DecimalField(max_digits=5, decimal_places=3)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

class BondPrice(models.Model):

    calendar = ql.Poland()
    settlement_days = '2D'
    settlement_date = calendar.advance(ql.Date.todaysDate(), ql.Period(settlement_days))

    bond = models.ForeignKey(Bond, on_delete=models.CASCADE, related_name='prices')
    price = models.DecimalField(max_digits=10, decimal_places=4)
    date = models.DateField(default=settlement_date)

    def __str__(self):
        return self.bond.name

    class Meta:
        ordering = ['date']
        unique_together = ('price', 'date')