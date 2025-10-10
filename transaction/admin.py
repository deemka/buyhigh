from django.contrib import admin

from transaction.models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("asset", "type", "count", "price", "type", "executed_at")
    list_filter = ("type",)
    date_hierarchy = "executed_at"