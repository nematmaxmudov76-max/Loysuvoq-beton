from django.db.models import TextChoices


class EstateStatusChoices(TextChoices):
    SALE = "sale", "for sale"
    SOLD = "sold", "sold"
    RENT = "rent", "for rent"
    UNAVAILABLE = "unavailable", "unavailable"
