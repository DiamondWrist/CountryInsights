from django.db import models

# Create your models here.


class City(models.Model):
    name = models.CharField(
        'Name',
        max_length=70,
        default='',
        unique=True
    )

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return "%s" % self.name


class Language(models.Model):

    name = models.CharField(
        'Name',
        max_length=70,
        default='',
        unique=True
    )

    nativeName = models.CharField(
        'Native Name',
        max_length=70,
        default='',
    )

    iso639_1 = models.CharField(
        "ISO-639 1",
        max_length=10,
        default='',
        null=True,
        blank=True
    )

    iso639_2 = models.CharField(
        "ISO-639 2",
        max_length=10,
        default='',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'

    def __str__(self):
        return '%s' % self.name


class Currency(models.Model):

    name = models.CharField(
        'Name',
        max_length=70,
        default='',
        null=True,
        blank=True
    )

    code = models.CharField(
        'Code',
        max_length=5,
        default='',
        null=True,
        blank=True
    )

    symbol = models.CharField(
        'Symbol',
        max_length=10,
        default='',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'

    def __str__(self):
        return '%s' % self.name


class Country(models.Model):

    name = models.CharField(
        'Name',
        max_length=150,
        default='',
        unique=True
    )

    capital = models.CharField(
        'Capital',
        max_length=150,
        default='',
    )

    cities = models.ManyToManyField(
        'City',
        verbose_name='City',
        related_name='country',
    )

    currencies = models.ManyToManyField(
        'Currency',
        verbose_name='Currency',
        related_name='country',
    )

    languages = models.ManyToManyField(
        'Language',
        verbose_name='Language',
        related_name='country',
    )

    population = models.PositiveBigIntegerField(
        'Population',
    )

    nativeName = models.CharField(
        'Native Name',
        max_length=150,
        default='',
        unique=True
    )

    numericCode = models.IntegerField(
        'Numeric Code',
        unique=True,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return '%s' % self.name
