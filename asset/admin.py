from django.contrib import admin

from asset.models import Asset, Symbol


@admin.register(Symbol)
class SymbolAdmin(admin.ModelAdmin):
    list_display = ("identifier", "identifier_type")


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ("title", "type")
    search_fields = ("title", "symbols__symbol")
    list_filter = ("type",)