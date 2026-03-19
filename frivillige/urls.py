from django.urls import path
from .views import home, VolunteerListView, VolunteerDetailView, VolunteerSignupView

app_name = 'frivillige'

urlpatterns = [
    path('', home, name='home'),
    path('volunteers/', VolunteerListView.as_view(), name='volunteer-list'),
    path('volunteers/<int:pk>/', VolunteerDetailView.as_view(), name='volunteer-detail'),
    path('signup/', VolunteerSignupView.as_view(), name='volunteer-signup'),
]
