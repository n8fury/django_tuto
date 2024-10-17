from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError


class AuctionPost(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    min_bid_amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[
                                         # Minimum bid must be >= 0
                                         MinValueValidator(0)])
    current_bid = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, validators=[
                                      # Minimum bid must be >= 0
                                      MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    image = models.ImageField(
        upload_to='auction_images/', blank=True, null=True)

    def clean(self):
        if self.current_bid < self.min_bid_amount:
            raise ValidationError(
                {'current_bid': 'Current bid must be greater than or equal to the minimum bid amount.'})

        if self.end_time <= self.created_at:
            raise ValidationError(
                {'end_time': 'End time must be in the future.'})

    def __str__(self):
        return f"{self.title} by {self.creator.username}"
