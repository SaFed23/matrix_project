from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView)
from .models import Matrix
from django.urls import reverse_lazy


class HomePageView(ListView):
    model = Matrix
    template_name = 'home.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class HowWorkingView(TemplateView):
    template_name = 'how_working.html'


class MatrixCreateView(CreateView):
    model = Matrix
    template_name = 'create.html'
    fields = ['rows', 'columns', 'values']


class MatrixDetailView(DetailView):
    model = Matrix
    template_name = 'detail.html'


class MatrixUpdateView(UpdateView):
    model = Matrix
    template_name = 'update.html'
    fields = ['rows', 'columns', 'values']


class MatrixDeleteView(DeleteView):
    model = Matrix
    template_name = 'delete.html'
    success_url = reverse_lazy('home')


class DeterminateView(ListView):
    model = Matrix
    template_name = 'determinate.html'


class SumElementsMatrixView(ListView):
    model = Matrix
    template_name = 'sum_elements.html'


class MeanElementMatrixView(ListView):
    model = Matrix
    template_name = 'mean_element.html'


class TranspositionMatrixView(ListView):
    model = Matrix
    template_name = 'transposition.html'


class MatrixRankView(ListView):
    model = Matrix
    template_name = 'matrix_rank.html'


class TriangularMatrixView(ListView):
    model = Matrix
    template_name = 'triangular_matrix_bottom.html'


class RootSystemView(ListView):
    model = Matrix
    template_name = 'root_system.html'


class DetMinorMatrixView(ListView):
    model = Matrix
    template_name = 'det_minor_matrix.html'
