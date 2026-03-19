from datetime import date

from django.db.models.signals import post_save
from django.dispatch import receiver

from medlemmer.models import Member

from .models import AnnualFee


@receiver(post_save, sender=Member)
def create_current_year_fee(sender, instance, created, **kwargs):
    if created:
        AnnualFee.objects.get_or_create(
            member=instance,
            year=date.today().year,
        )
