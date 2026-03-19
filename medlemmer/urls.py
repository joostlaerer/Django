from django.urls import path
from .views import MemberListView, MemberDetailView, MemberEditView

app_name = 'medlemmer'

urlpatterns = [
    path('', MemberListView.as_view(), name='member-list'),
    path('<int:pk>/', MemberDetailView.as_view(), name='member-detail'),
    path('edit/', MemberEditView.as_view(), name='member-edit'),
]
