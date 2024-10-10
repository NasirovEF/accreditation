from django.contrib import admin
from django.urls import reverse
from sale.models import Product, Factory, Retail, IndEntrepr, Contacts

admin.site.register(Product)
admin.site.register(Contacts)


@admin.action(description="Очистить задолженность перед поставщиком у выбранных объектов")
def clear_arrears(modeladmin, request, queryset):
    queryset.update(arrears=0)


class CityFilter(admin.SimpleListFilter):
    title = "Город"
    parameter_name = "city_name"

    def lookups(self, request, model_admin):
        cities = set(obj.city_name for obj in model_admin.model.objects.all())
        return [(city, city) for city in cities]

    def queryset(self, request, queryset):
        city_name = self.value()
        if city_name:
            return queryset.filter(contacts__city=city_name)
        return queryset


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ("name", "contacts", "created_at", "city_name")
    search_fields = ("name", "contacts", "created_at", "city_name")
    list_filter = (CityFilter, "name")



@admin.register(Retail)
class RetailAdmin(admin.ModelAdmin):
    list_display = ("name", "contacts", "created_at", "supplier", "arrears",)
    search_fields = ("name", "contacts", "created_at", "city_name")
    list_filter = (CityFilter, "name")
    actions = [clear_arrears]

    def get_supplier_url(self, obj):
        return u''.format(reverse("admin:sale_factory_change", args=[obj.supplier.pk]), obj.supplier)
    get_supplier_url.short_description = "Поставщик"
    get_supplier_url.admin_order_field = "supplier"
    get_supplier_url.allow_tags = True



@admin.register(IndEntrepr)
class IndEntreprAdmin(admin.ModelAdmin):
    list_display = ("name", "contacts", "created_at", "supplier", "arrears")
    search_fields = ("name", "contacts", "created_at", "city_name")
    actions = [clear_arrears]
