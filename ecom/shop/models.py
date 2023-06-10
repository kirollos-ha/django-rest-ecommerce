from django.db import models
from authentication.models import ShopUser

# c'era un name clash e django consigliava di usare
# related_name, per non avere più product_set, o qualcosa del genere
# non mi ricordavo cosa fosse related_name, i doc mi spaventano, quindi stack
# https://stackoverflow.com/questions/2642613/what-is-related-name-used-for
class Product(models.Model):
    seller = models.ForeignKey(ShopUser, on_delete=models.CASCADE,
                               related_name='products')
    name = models.CharField(max_length=200)
    price_in_cents = models.IntegerField()
    description = models.TextField()
    quantity_in_stock = models.IntegerField()

class Order(models.Model):
    """ hic est carrellus """
    buyer = models.ForeignKey(ShopUser, on_delete=models.CASCADE,
                              related_name='orders_made')
    product = models.ForeignKey(ShopUser, on_delete=models.CASCADE,
                                related_name='orders_with_product')
    quantity = models.IntegerField()
