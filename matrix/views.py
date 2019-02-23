import pandas as pd
import numpy as np
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView)
from .models import Matrix, show_matrix
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect


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
    fields = ['name', 'rows', 'columns', 'values']


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
    template_name = 'triangular_matrix.html'


class RootSystemView(ListView):
    model = Matrix
    template_name = 'root_system.html'


class DetMinorMatrixView(ListView):
    model = Matrix
    template_name = 'det_minor_matrix.html'


class WriteMatrixInFileView(DetailView):
    model = Matrix
    template_name = 'for_work/add_file.html'


class CreateWithFileView(CreateView):
    model = Matrix
    template_name = 'for_work/create_with_file.html'
    fields = ['name', 'file']
    success_url = "home"

    def form_valid(self, form):
        name = form.cleaned_data['name']
        file = form.cleaned_data['file']
        df = pd.read_csv(file)
        array = []
        bof_array = []
        for el in df.columns.values:
            bof_array.append(int(el))
        array.append(bof_array)
        for row in df.values:
            bof_array = []
            for column in row:
                bof_array.append(int(column))
            array.append(bof_array)
        rows = len(array)
        columns = len(bof_array)
        array = show_matrix(array)
        array_string = ""
        for row in array:
            array_string += row + "\n"
        self.model.objects.create(
            name=name,
            rows=rows,
            columns=columns,
            values=array_string,
        )
        return HttpResponseRedirect("/")


class DetInFileView(ListView):
    model = Matrix

    def get(self, request, *args, **kwargs):
        all_matrix = self.model.objects.all()
        for matrix in all_matrix:
            matrix.det_in_file()
        return HttpResponseRedirect("/determinate/")


class SumInFileView(ListView):
    model = Matrix

    def get(self, request, *args, **kwargs):
        all_matrix = self.model.objects.all()
        for matrix in all_matrix:
            matrix.sum_in_file()
        return HttpResponseRedirect('/sum_elements/')


class MeanInFileView(ListView):
    model = Matrix

    def get(self, request, *args, **kwargs):
        all_matrix = self.model.objects.all()
        for matrix in all_matrix:
            matrix.mean_in_file()
        return HttpResponseRedirect('/mean_element/')


class TransInFileView(ListView):
    model = Matrix

    def get(self, request, *args, **kwargs):
        all_matrix = self.model.objects.all()
        for matrix in all_matrix:
            matrix.trans_in_file()
        return HttpResponseRedirect('/transposition/')


class RankInFileView(ListView):
    model = Matrix

    def get(self, request, *args, **kwargs):
        all_matrix = self.model.objects.all()
        for matrix in all_matrix:
            matrix.rank_in_file()
        return HttpResponseRedirect('/matrix_rank/')


class TriangularInFileView(ListView):
    model = Matrix

    def get(self, request, *args, **kwargs):
        all_matrix = self.model.objects.all()
        for matrix in all_matrix:
            matrix.triangular_in_file()
        return HttpResponseRedirect('/triangular_matrix/')


class RootInFileView(ListView):
    model = Matrix

    def get(self, request, *args, **kwargs):
        all_matrix = self.model.objects.all()
        for matrix in all_matrix:
            matrix.root_in_file()
        return HttpResponseRedirect('/root_system/')


class MinorInFileView(ListView):
    model = Matrix

    def get(self, request, *args, **kwargs):
        all_matrix = self.model.objects.all()
        for matrix in all_matrix:
            matrix.minor_in_file()
        return HttpResponseRedirect('/det_minor_matrix/')
