# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# -*- coding: utf-8 -*-


from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from decimal import Decimal
# Create your models here.


class PortfolioQuerySet(models.QuerySet):
    pass

class PortfolioManager(models.Manager):
    def getQueryset(self):
        return PortfolioQuerySet(self.model,using=self._db)


class Portfolio (models.Model):
    user          =models.ForeignKey(settings.AUTH_USER_MODEL)
    coin_quant = models.FloatField(null=True, blank=True)
    #coin_quant    =models.DecimalField(max_digits=10,decimal_places=4,default=Decimal('0.0000'))
    coin_name     =models.CharField(max_length = 15,null=True, blank=True)
    updated       =models.DateTimeField(auto_now=True)
    timestamp     =models.DateTimeField(auto_now_add=True)

    objects = PortfolioManager()

    def __str__(self):
        return str(self.coin_name)[:10]

    class Meta:
        verbose_name = 'Porfolio'
        verbose_name_plural = 'Portfolios'
