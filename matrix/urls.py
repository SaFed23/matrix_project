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
    TranspositionMatrixView,
    MatrixRankView,
    TriangularMatrixView,
    RootSystemView,
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
    path('transposition/', TranspositionMatrixView.as_view(), name='transposition'),
    path('matrix_rank/', MatrixRankView.as_view(), name='matrix_rank'),
    path('triangular_matrix/', TriangularMatrixView.as_view(), name='triangular_matrix'),
    path('root_system/', RootSystemView.as_view(), name='root_system'),
]
