from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Volunteer
from .forms import VolunteerSignupForm


def home(request):
    """Homepage with signup button"""
    volunteer_count = Volunteer.objects.filter(is_active=True).count()
    context = {
        'volunteer_count': volunteer_count,
    }
    return render(request, 'frivillige/home.html', context)


class VolunteerListView(ListView):
    model = Volunteer
    template_name = 'frivillige/volunteer_list.html'
    context_object_name = 'volunteers'
    paginate_by = 12
    
    def get_queryset(self):
        return Volunteer.objects.filter(is_active=True).order_by('-created_at')


class VolunteerDetailView(DetailView):
    model = Volunteer
    template_name = 'frivillige/volunteer_detail.html'
    context_object_name = 'volunteer'


class VolunteerSignupView(CreateView):
    model = Volunteer
    form_class = VolunteerSignupForm
    template_name = 'frivillige/volunteer_signup.html'
    success_url = reverse_lazy('frivillige:volunteer-list')

    def form_valid(self, form):
        return super().form_valid(form)
