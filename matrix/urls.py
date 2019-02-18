from django.urls import path
from .views import (
    HomePageView,
    AboutView,
    MatrixCreateView,
    MatrixDetailView,
    MatrixUpdateView,
    MatrixDeleteView,
    DeterminateView,
    SumElementsMatrixView,
    MeanElementMatrixView,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('create/', MatrixCreateView.as_view(), name='create'),
    path('matrix/<int:pk>/detail', MatrixDetailView.as_view(), name='detail'),
    path('matrix/<int:pk>/update', MatrixUpdateView.as_view(), name='update'),
    path('matrix/<int:pk>/delete', MatrixDeleteView.as_view(), name='delete'),
    path('determinate/', DeterminateView.as_view(), name='determinate'),
    path('sum_elements/', SumElementsMatrixView.as_view(), name='sum_elements'),
    path('mean_element/', MeanElementMatrixView.as_view(), name='mean_element'),
]
