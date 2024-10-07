from django.db import models

from users.services import NULLABLE


class Contacts(models.Model):
    """Модель контактной информации"""
    email = models.EmailField(max_length=100, verbose_name="Почта")
    country = models.CharField(max_length=200, verbose_name="Страна")
    city = models.CharField(max_length=200, verbose_name="Город")
    strit = models.CharField(max_length=200, verbose_name="Улица")
    house_number = models.CharField(max_length=10, verbose_name="Номер дома")

    class Meta:
        verbose_name = "Контактная информация"
        verbose_name_plural = "Контактные информации"




class Product(models.Model):
    """Модель продукта"""
    name = models.CharField(max_length=200, verbose_name="Название продукта")
    model = models.CharField(max_length=150, verbose_name="Модель")
    date_release = models.DateField(verbose_name="Дата выхода продукта")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name


class Factory(models.Model):
    """Модель фабрики"""
    name = models.CharField(max_length=200, verbose_name="Название")
    contacts = models.OneToOneField(Contacts, on_delete=models.CASCADE, verbose_name="Контакты", related_name="company")
    products = models.ForeignKey(Product, verbose_name="Продукты", related_name="seller", on_delete=models.SET_NULL, **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Фабрика"
        verbose_name_plural = "Фабрики"

    def __str__(self):
        return f'Завод "{self.name}"'


class Retail(Factory):
    """Модель розничной точки"""
    supplier = models.ForeignKey(Factory, on_delete=models.CASCADE, verbose_name="Поставщик", related_name="retails")
    arrears = models.FloatField(verbose_name="Задолженность перед поставщиком", default=0)

    class Meta:
        verbose_name = "Розничная точка"
        verbose_name_plural = "Розничные точки"

    def __str__(self):
        return f'Розничная точка "{self.name}"'


class IndEntrepr(Factory):
    """Модель индивидуального предпринимателя"""
    supplier = models.ForeignKey(Retail, on_delete=models.CASCADE, verbose_name="Поставщик", related_name="indentrepr")
    arrears = models.FloatField(verbose_name="Задолженность перед поставщиком", default=0)

    class Meta:
        verbose_name = "Индивидуальный предприниматель"
        verbose_name_plural = "Индивидуальные предприниматели"

    def __str__(self):
        return f'ИП "{self.name}"'


