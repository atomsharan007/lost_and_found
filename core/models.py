from django.db import models

class LostItem(models.Model):
    item_name = models.CharField(max_length=100)
    item_type = models.CharField(max_length=100, default="Lost")  # Default added
    location = models.CharField(max_length=100)
    date_lost = models.DateField()
    description = models.TextField()
    contact = models.CharField(max_length=15)  # Number field as text but length-limited
    image = models.ImageField(upload_to='lost_items/', blank=True, null=True, default='default.jpg')  # Allow blank/null & default

    def __str__(self):
        return f"{self.item_name} (Lost)"


class FoundItem(models.Model):
    item_name = models.CharField(max_length=100)
    item_type = models.CharField(max_length=100, default="Found")  # Default added
    location = models.CharField(max_length=100)
    date_found = models.DateField()
    description = models.TextField()
    contact = models.CharField(max_length=15)  # Number field as text but length-limited
    image = models.ImageField(upload_to='found_items/', blank=True, null=True, default='default.jpg')  # Allow blank/null & default

    def __str__(self):
        return f"{self.item_name} (Found)"
