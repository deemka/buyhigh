from decimal import Decimal
from typing import Iterable
import statistics


def average(values: Iterable[Decimal]) -> Decimal:
    return statistics.mean(values)

