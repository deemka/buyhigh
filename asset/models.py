from django.db import models
from djmoney.models.fields import MoneyField

from core.models import BaseModel

SYMBOL_TYPES = (
    ("ISIN", "ISIN"),
    ("WKN", "WKN"),
    ("NYSE", "NYSE"),
    ("other", "Other"),
)

ASSET_TYPES = (
    ("STOCK", "Stock"),
    ("OPTION", "Option"),
    ("KO", "Knockout"),
    ("UNDEFINED", "Undefined"),
)


class Symbol(models.Model):
    identifier = models.CharField(max_length=16, unique=True)
    identifier_type = models.CharField(max_length=16, choices=SYMBOL_TYPES, default="ISIN")

    def __str__(self):
        return f"{self.identifier_type} : {self.identifier}"


class Asset(BaseModel):
    title = models.CharField(max_length=256, null=True, default=None)
    symbols = models.ManyToManyField(Symbol, blank=True)
    type = models.CharField(max_length=16, choices=ASSET_TYPES, default="UNDEFINED")

    def __str__(self):
        ret = self.title
        syms = []
        for symbol in self.symbols.all():
            syms.append(f"{symbol.identifier_type}: {symbol.identifier}")
        if syms:
            syms_s = ", ".join(syms)
            ret += f" ({syms_s})"
        return ret
