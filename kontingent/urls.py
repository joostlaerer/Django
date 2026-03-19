from django.urls import path

from .views import MyAnnualFeeListView, mark_fee_paid

app_name = 'kontingent'

urlpatterns = [
    path('mine/', MyAnnualFeeListView.as_view(), name='my-fees'),
    path('mark-paid/<int:member_id>/', mark_fee_paid, name='mark-paid'),
]
