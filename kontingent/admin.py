from django.contrib import admin

from .models import AnnualFee


@admin.register(AnnualFee)
class AnnualFeeAdmin(admin.ModelAdmin):
	list_display = ('member', 'year', 'amount', 'status', 'due_date', 'paid_at')
	list_filter = ('status', 'year', 'due_date')
	search_fields = ('member__user__username', 'member__user__first_name', 'member__user__last_name')
	ordering = ('-year', 'member__user__username')
