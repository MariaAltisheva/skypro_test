from django.db import models


class Item(models.Model):
    name = models.CharField(verbose_name='Продукт', max_length=30)
    model = models.CharField(verbose_name='Модель', max_length=100)
    start_date = models.DateField(verbose_name='Дата выхода продукта на рынок', auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class Link(models.Model):
    LINKS = ((0, 'Завод'), (1, 'Розничная сеть'), (2, 'ИП'))
    hierarchy = models.SmallIntegerField(verbose_name='Звено сети', choices=LINKS)
    name = models.CharField(verbose_name='Компания', max_length=100, unique=True)
    email = models.EmailField(max_length=150, unique=True)
    country = models.CharField(verbose_name='Страна', max_length=50)
    city = models.CharField(verbose_name='Город', max_length=50)
    street = models.CharField(verbose_name='Улица', max_length=150)
    house = models.CharField(verbose_name='Дом', max_length=10)
    items = models.ManyToManyField(Item, related_name='network')
    provider = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='Поставщик', related_name='traders',
                                 null=True, blank=True)
    debt = models.DecimalField(max_digits=30, decimal_places=2, verbose_name='Задолженность', default=0)
    date_of_create = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Звено сети'
        verbose_name_plural = 'Звенья сети'

    def __str__(self):
        return self.name

