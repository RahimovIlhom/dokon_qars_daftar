from django.urls import path
from .views import (
    HomePageView,
    qarzdorlarView,
    qarzdorView,
    QarzdorCreateView,
    QarzCreateView,
    QarzdorUpdateView,
    QarzUpdateView,
    QarzdorDeleteView,
    QarzDeleteView,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('qarzdorlar/', qarzdorlarView, name='qarzdorlar'),
    path('qarzdor/<int:id>', qarzdorView, name='qarzdor'),
    path('new/', QarzdorCreateView.as_view(), name='qarzdor_new'),
    path('qarzdor/<int:id>/new', QarzCreateView.as_view(), name='qarz_new'),
    path('qarzdor/<int:pk>/edit', QarzdorUpdateView.as_view(), name='qarzdor_edit'),
    path('qarz/<int:pk>/edit', QarzUpdateView.as_view(), name='qarz_edit'),
    path('qarzdorlar/<int:pk>/delete', QarzdorDeleteView.as_view(), name='qarzdor_delete'),
    path('qarzdor/<int:pk>/delete', QarzDeleteView.as_view(), name='qarz_delete'),
]