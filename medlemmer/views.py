from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Member
from .forms import MemberEditForm


class MemberListView(LoginRequiredMixin, ListView):
    model = Member
    template_name = 'medlemmer/member_list.html'
    context_object_name = 'members'
    paginate_by = 10


class MemberDetailView(LoginRequiredMixin, DetailView):
    model = Member
    template_name = 'medlemmer/member_detail.html'
    context_object_name = 'member'


class MemberEditView(LoginRequiredMixin, UpdateView):
    model = Member
    form_class = MemberEditForm
    template_name = 'medlemmer/member_edit.html'
    success_url = reverse_lazy('medlemmer:member-list')

    def get_object(self, queryset=None):
        return get_object_or_404(Member, user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_own_profile'] = self.get_object().user == self.request.user
        return context
