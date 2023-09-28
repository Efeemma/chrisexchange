from django.db import models

# Create your models here.

class Cryptocurrencies_Rate(models.Model):
    item_photo = models.ImageField(upload_to='crypto_coin', blank=True)
    buy_price = models.IntegerField()
    sell_price = models.IntegerField()
    
    
class Giftcard_Rate(models.Model):
    item_photo = models.ImageField(upload_to='crypto_coin', blank=True)
    buy_price = models.IntegerField()
    sell_price = models.IntegerField()
