from django.urls import path
from .views import(
    LeadListView,
    LeadDetailView,
    LeadCreateView,
    LeadUpdateView,
    LeadDeleteView,
    LeadConvertView,
    ClientListView,
    ClientDetailView,
    ClientCreateView,
    ClientUpdateView,
    ClientDeleteView
)

urlpatterns = [
    # URLs для лидов
    path('', LeadListView.as_view(), name = 'lead-list'),
    path('lead/<int:pk>/', LeadDetailView.as_view(), name = 'lead-detail'),
    path('lead/add/', LeadCreateView.as_view(), name = 'lead-create'),
    path('lead/<int:pk>/edit/', LeadUpdateView.as_view(), name = 'lead-update'),
    path('lead/<int:pk>/delete/', LeadDeleteView.as_view(), name = 'lead-delete'),
    path('lead/<int:pk>/convert/', LeadConvertView.as_view(), name='lead-convert'),
    # URLs для клиентов
    path('clients/',ClientListView.as_view(),name='client-list'),
    path('client/<int:pk>/',ClientDetailView.as_view(),name='client-detail'),
    path('client/add/',ClientCreateView.as_view(),name='client-create'),
    path('client/<int:pk>/delete/',ClientDeleteView.as_view(),name='client-delete'),
    path('client/<int:pk>/edit/',ClientUpdateView.as_view(),name='client-update')
]

