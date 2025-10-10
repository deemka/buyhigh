from django.contrib import admin

from portfolio.models import Portfolio


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ("pk", "name",)

    def current_positions(self, obj):
        return obj.current_positions
