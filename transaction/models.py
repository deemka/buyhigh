from django.db import models

from asset.models import Asset
from core.models import BaseModel
from portfolio.models import Portfolio


class Transaction(BaseModel):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name="transactions")
    asset = models.ForeignKey(Asset, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    count = models.PositiveIntegerField(default=0)
    type = models.CharField(max_length=4, choices=(("buy", "buy"), ("sell", "sell")))
    transaction_costs = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    executed_at = models.DateTimeField()

    def total_price(self):
        return self.price * self.count + self.transaction_costs

    def __str__(self):
        return f"{self.type}: {self.asset.title} @ {self.price} x {self.count}"
