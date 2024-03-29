from django.db import models
from django.urls import reverse
import numpy as np
import pandas as pd


def make_array(string):
    lines = string.splitlines()
    array = list(map(lambda x: list(map(int, x.split())), lines))
    return array


def show_matrix(array):
    bof_array = []
    for line in array:
        line = list(map(str, line))
        bof_array.append(" ".join(line))
    return bof_array


class Matrix(models.Model):

    name = models.CharField(max_length=25, default="New matrix")
    rows = models.PositiveIntegerField(default=0)
    columns = models.PositiveIntegerField(default=0)
    values = models.TextField()
    file = models.FileField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", args=[str(self.id)])

    def matrix(self):
        array = make_array(self.values)
        return array

    def determinate(self):
        if self.rows == self.columns:
            array = np.array(make_array(self.values))
            array.shape = (int(self.rows), int(self.columns))
            return np.around(np.linalg.det(array), decimals=2)
        else:
            return "Ошибка. Матрица не квадратная. Невозможно найти определитель!"

    def det_in_file(self):
        with open(self.name + ".txt", "w+") as file:
            file.write(str(self.determinate()))
        return reverse("detail", args=[str(self.id)])

    def sum_elements(self):
        return np.sum(np.array(make_array(self.values)))

    def sum_in_file(self):
        with open(self.name + ".txt", "w+") as file:
            file.writelines(str(self.sum_elements()))
        return reverse("detail", args=[str(self.id)])

    def mean_element(self):
        return np.mean(np.array(make_array(self.values)))

    def mean_in_file(self):
        with open(self.name + ".txt", "w+") as file:
            file.writelines(str(self.mean_element()))
        return reverse("detail", args=[str(self.id)])

    def transposition(self):
        array = np.transpose(np.array(make_array(self.values)))
        return array

    def trans_in_file(self):
        array_string = ""
        for line in show_matrix(self.transposition()):
            array_string += line + "\n"
        with open(self.name + ".txt", "w+") as file:
            file.write(array_string)
        return reverse("detail", args=[str(self.id)])

    def matrix_rank(self):
        return np.linalg.matrix_rank(np.array(make_array(self.values)))

    def rank_in_file(self):
        with open(self.name + ".txt", "w+") as file:
            file.write(str(self.matrix_rank()))
        return reverse("detail", args=[str(self.id)])

    def triangular_matrix_bottom(self):
        array = np.tril(np.array(make_array(self.values)), k=0)
        return array

    def triangular_matrix_top(self):
        array = np.triu(np.array(make_array(self.values)), k=0)
        return array

    def triangular_in_file(self):
        array_string = ""
        for line in show_matrix(self.triangular_matrix_bottom()):
            array_string += line + "\n"
        array_string += "\n"
        for line in show_matrix(self.triangular_matrix_top()):
            array_string += line + "\n"
        with open(self.name + ".txt", "w+") as file:
            file.write(array_string)
        return reverse("detail", args=[str(self.id)])

    def root_system(self):
        if self.determinate():
            if self.rows == self.columns:
                answer = np.zeros(self.rows)
                array_x = []
                for x in range(self.rows):
                    array_x.append('x' + str(x + 1))
                roots = list(zip(array_x, np.linalg.solve(np.array(make_array(self.values)), answer)))
                return roots
            else:
                return "Ошибка. Матрица не квадратная. Один из аргументов равен бесконечности!"
        else:
            return "Сингулярная матрица. Определитель равен 0!"

    def root_in_file(self):
        array_string = ""
        if self.determinate():
            if self.rows == self.columns:
                for line in self.root_system():
                    array_string += str(line[0]) + " = " + str(line[1]) + "\n"
            else:
                array_string = self.root_system()
        else:
            array_string = self.root_system()
        with open(self.name + ".txt", "w+") as file:
            file.write(array_string)
        return reverse("detail", args=[str(self.id)])

    def det_minor_matrix(self):
        if self.rows == self.columns:
            bof_array = []
            array = np.array(make_array(self.values))
            for i in range(self.rows):
                for j in range(self.columns):
                    m_shape = array.shape[0] - 1
                    arrayM = np.eye(m_shape, dtype='int')
                    arrayM[:i, :j] = array[:i, :j]
                    arrayM[:i, j:] = array[:i, j + 1:]
                    arrayM[i:, :j] = array[i + 1:, :j]
                    arrayM[i:, j:] = array[i + 1:, j + 1:]
                    bof_array.append(str(np.around(np.linalg.det(arrayM))))

            return ", ".join(bof_array)
        else:
            return "Ошибка. Матрица не квадратная"

    def minor_in_file(self):
        with open(self.name + ".txt", "w+") as file:
            file.write(self.det_minor_matrix())
        return reverse("detail", args=[str(self.id)])

    def write_in_csv_file(self):
        df = pd.DataFrame(self.matrix())
        df.to_csv(self.name + ".csv", header=None, index=None)
        return reverse("detail", args=[str(self.id)])

    def create_with_file(self):
        return reverse("detail", args=[str(self.id)])
