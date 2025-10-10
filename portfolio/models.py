import re

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum, Case, When, F, DecimalField

from core.models import BaseModel


class Portfolio(BaseModel):
    name = models.CharField(max_length=32, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def current_positions(self) -> models.QuerySet:
        return self.transactions.values("asset").annotate(
            buy_count=Sum(Case(When(type="buy", then=F("count")), default=0, output_field=DecimalField())),
            sell_count=Sum(Case(When(type="sell", then=F("count")), default=0, output_field=DecimalField()))
        ).annotate(
            current_count=F("buy_count")-F("sell_count")
        ).filter(
            current_count__gt=0
        )

    def save(self, *args, **kwargs):
        if self._state.adding and not self.name:
            auto_names = Portfolio.objects.filter(user=self.user, name__regex=".*'s Portfolio \d+$")
            last = sorted(auto_names.values_list("name", flat=True))[-1]
            seq = int(re.search(r"\d+$", last).group()) + 1
            self.name = f"{self.user.username}'s Portfolio {seq}"
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name
