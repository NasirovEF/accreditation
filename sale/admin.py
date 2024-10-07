from django.contrib import admin

from sale.models import Product, Factory, Retail, IndEntrepr, Contacts

admin.site.register(Product)
admin.site.register(Contacts)
# admin.site.register(Factory)
# admin.site.register(Retail)
# admin.site.register(IndEntrepr)
@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ("name", "contacts", "products", "created_at",)
    search_fields = ("name", "contacts", "products", "created_at")


@admin.register(Retail)
class RetailAdmin(admin.ModelAdmin):
    list_display = ("name", "contacts", "products", "created_at", "supplier", "arrears",)
    search_fields = ("name", "contacts", "products", "created_at")


@admin.register(IndEntrepr)
class IndEntreprAdmin(admin.ModelAdmin):
    list_display = ("name", "contacts", "products", "created_at", "supplier", "arrears",)
    search_fields = ("name", "contacts", "products", "created_at")

