from django.contrib import admin
from .models import Member
from kontingent.models import AnnualFee


class AnnualFeeInline(admin.TabularInline):
    model = AnnualFee
    extra = 0
    fields = ('year', 'amount', 'status', 'due_date', 'paid_at', 'notes')
    ordering = ('-year',)


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'phone', 'city', 'joined_date')
    list_filter = ('joined_date', 'city', 'country')
    search_fields = ('user__first_name', 'user__last_name', 'user__email', 'phone')
    readonly_fields = ('joined_date', 'updated_date')
    inlines = [AnnualFeeInline]

    def get_full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}" or obj.user.username
    get_full_name.short_description = 'Name'
