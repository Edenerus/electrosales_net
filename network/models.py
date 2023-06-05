from django.db import models
from django.core.exceptions import ValidationError


class Product(models.Model):
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    title = models.CharField(max_length=50, verbose_name='Название')
    model = models.CharField(max_length=50, verbose_name='Модель')
    date_release = models.DateTimeField(blank=True, null=True, verbose_name='Дата выхода продукта на рынок')

    def __str__(self):
        return self.title


class Provider(models.Model):
    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    class Types(models.IntegerChoices):
        Factory = 0, 'Завод'
        RetailNetwork = 1, 'Розничная сеть'
        IE = 2, 'Индивидуальный предприниматель'  # IE - Individual Entrepreneur

    title = models.CharField(max_length=50, unique=True, verbose_name='Название')
    type = models.PositiveSmallIntegerField(choices=Types.choices, default=0, verbose_name='Тип звена')
    level = models.SmallIntegerField(verbose_name='Уровень звена сети', default=0)

    # contacts
    email = models.EmailField(unique=True, verbose_name='Email')
    country = models.CharField(max_length=50, verbose_name='Страна')
    city = models.CharField(max_length=50, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    # CharField т.к нам точно неизвестен Номер дома, на случай если указывается цифра с буквой, например, 2-а
    house = models.CharField(max_length=50, verbose_name='Номер дома')

    products = models.ManyToManyField(Product, blank=True, verbose_name='Продукты')
    provider = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name='Поставщик', related_name='supplier')
    debt = models.DecimalField(default=0, decimal_places=2, max_digits=10, verbose_name='Задолженность')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', editable=False)

    def save(self, *args, **kwargs):
        """Определение уровня звена сети"""
        if not self.provider:
            self.level = 0

        else:
            self.level = self.provider.level + 1

        return super().save(*args, **kwargs)

    def clean(self):
        """Проверка нужна для того, чтобы узнать, может ли объект иметь поставщика
            Т.к Завод всегда находится в уровне сети 0, то у него не может быть поставщиков
            Если потенциальный поставщик уже находится на уровне сети 2(т.е у него есть поставщик, у которого тоже свой
            поставщик), то он не может быть поставщиком для объекта
            В обоих случаях при неполадках выпадает сообщение"""
        if self.type == 0 and self.provider:
            raise ValidationError(f"{self} является заводом и не может иметь поставщиков")
        if self.provider.level == 2:
            raise ValidationError(f"{self.provider} не может быть поставщиком для {self}, т.к его уровень сети 2 ")

    def __str__(self):
        return self.title
