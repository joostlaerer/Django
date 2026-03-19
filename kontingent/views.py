from datetime import date

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView

from medlemmer.models import Member

from .models import AnnualFee


class MyAnnualFeeListView(LoginRequiredMixin, ListView):
	model = AnnualFee
	template_name = 'kontingent/my_fees.html'
	context_object_name = 'fees'

	def get_queryset(self):
		return AnnualFee.objects.filter(member__user=self.request.user).select_related('member', 'member__user')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['member'] = Member.objects.filter(user=self.request.user).first()
		context['current_year'] = date.today().year
		return context


@staff_member_required
def mark_fee_paid(request, member_id):
	if request.method != 'POST':
		return redirect('medlemmer:member-detail', pk=member_id)

	member = get_object_or_404(Member, pk=member_id)
	fee, _ = AnnualFee.objects.get_or_create(
		member=member,
		year=date.today().year,
	)
	fee.status = AnnualFee.STATUS_PAID
	fee.paid_at = date.today()
	fee.save()

	return redirect('medlemmer:member-detail', pk=member_id)
