from django.urls import path

from .views import MyAnnualFeeListView

app_name = 'kontingent'

urlpatterns = [
    path('mine/', MyAnnualFeeListView.as_view(), name='my-fees'),
]
