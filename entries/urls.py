from django.urls import path
from .views import (
    EntryListView,
    EntryDetailView,
    EntryCreateView,
    EntryUpdateView,
    EntryDeleteView,
    entry_search,
    home
)

urlpatterns = [
    path('', home, name='home'),
    path('entries/', EntryListView.as_view(), name='entry-list'),
    path('entries/<int:pk>/', EntryDetailView.as_view(), name='entry-detail'),
    path('entries/new/', EntryCreateView.as_view(), name='entry-create'),
    path('entries/<int:pk>/update/', EntryUpdateView.as_view(), name='entry-update'),
    path('entries/<int:pk>/delete/', EntryDeleteView.as_view(), name='entry-delete'),
    path('search/', entry_search, name='entry-search'),
]