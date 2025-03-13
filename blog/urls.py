from django.urls import path
from .views import (
                    PublicationListView, 
                    PublicationDetailView,
                    PublicationCreateView,
                    PublicationUpdateView
                    )

urlpatterns = [
    path('', PublicationListView.as_view(), name='publications-list'),
    path('publication/<int:pk>/', PublicationDetailView.as_view(), name='publication-detail'),
    path('publication/new/', PublicationCreateView.as_view(), name='publication-create'),
    path('publication/<int:pk>/update', PublicationUpdateView.as_view(), name='publication-update'),
    
]