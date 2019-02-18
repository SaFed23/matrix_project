from django.db import models
from django.urls import reverse
import numpy as np


def make_array(string):
    lines = string.splitlines()
    array = list(map(lambda x: list(map(lambda x1: int(x1), x.split())), lines))
    return array


class Matrix(models.Model):
    rows = models.IntegerField(default=0)
    columns = models.IntegerField(default=0)
    values = models.TextField()

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse("detail", args=[str(self.id)])

    def show_matrix(self):
        return np.array(make_array(self.values))

    def determinate(self):
        array = np.array(make_array(self.values))
        array.shape = (int(self.rows), int(self.columns))
        return np.around(np.linalg.det(array))

    def sum_elements(self):
        return np.sum(np.array(make_array(self.values)))

    def mean_element(self):
        return np.mean(np.array(make_array(self.values)))

    def transposition(self):
        return np.transpose(np.array(make_array(self.values)))

    def matrix_rank(self):
        return np.linalg.matrix_rank(np.array(make_array(self.values)))

    def triangular_matrix_bottom(self):
        return np.tril(np.array(make_array(self.values)), k=0)

    def triangular_matrix_top(self):
        return np.triu(np.array(make_array(self.values)), k=0)

    def root_system(self):
        answer = np.zeros(self.rows)
        array_x = []
        for x in range(self.rows):
            array_x.append('x' + str(x + 1))
        roots = list(zip(array_x, np.linalg.solve(np.array(make_array(self.values)), answer)))
        return roots


