from datetime import date

from django.contrib.auth.mixins import LoginRequiredMixin
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
