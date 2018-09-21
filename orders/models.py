from django.db import models
from carts.models import Cart

ORDER_STATUS_CHOICES = (
    ('created', 'Created'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('refunded', 'Refunded')
)

class Order(models.Model):

    order_id = models.CharField(max_length=120, blank=True)
    # billing profile = ?
    # shipping address
    # billing address
    cart = models.ForeignKey(Cart)
    status = models.CharField(max_length=128, default='created')
    shipping_total = models.DecimalField(default=5.99, max_digits=10, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)

    def __str__(self):
        return self.order_id