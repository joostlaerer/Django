from datetime import date
from decimal import Decimal

from django.db import models

from medlemmer.models import Member


def current_year():
	return date.today().year


def default_due_date():
	today = date.today()
	return date(today.year, 3, 31)


class AnnualFee(models.Model):
	STATUS_PENDING = 'pending'
	STATUS_PAID = 'paid'
	STATUS_EXEMPT = 'exempt'

	STATUS_CHOICES = [
		(STATUS_PENDING, 'Pending'),
		(STATUS_PAID, 'Paid'),
		(STATUS_EXEMPT, 'Exempt'),
	]

	member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='annual_fees')
	year = models.PositiveIntegerField(default=current_year)
	amount = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal('500.00'))
	due_date = models.DateField(default=default_due_date)
	status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)
	paid_at = models.DateField(blank=True, null=True)
	notes = models.TextField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-year', 'member__user__username']
		unique_together = ('member', 'year')

	def __str__(self):
		return f'{self.member} - {self.year}'

	@property
	def is_paid(self):
		return self.status in {self.STATUS_PAID, self.STATUS_EXEMPT}

	def save(self, *args, **kwargs):
		if self.status != self.STATUS_PAID:
			self.paid_at = None if self.status == self.STATUS_PENDING else self.paid_at
		super().save(*args, **kwargs)
