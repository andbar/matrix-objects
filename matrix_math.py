class ShapeException(Exception):
    pass


class Vector:

    def __init__(self, vec):
        self.vec = vec
        self.shape = len(self.vec)

    def __str__(self):
        return "{}".format(self.vec)

    def shape_checker(self, other):
        if self.shape != other.shape:
            raise ShapeException()

    def __add__(self, other):
        self.shape_checker(other)
        added_vector = []
        for index, value in enumerate(self.vec):
            added_vector.append(self.vec[index] + other.vec[index])
        return Vector(added_vector)

    def __sub__(self, other):
        self.shape_checker(other)
        subtract_vector = []
        for index, value in enumerate(self.vec):
            subtract_vector.append(self.vec[index] - other.vec[index])
        return Vector(subtract_vector)

    def __mul__(self, other):
        mult_vector = []
        for row in self.vec:
            mult_vector.append(row * other)
        return Vector(mult_vector)

    def __eq__(self, other):
        if self.vec == other.vec:
            return True
        else:
            return False

    def dot(self, other):
        self.shape_checker(other)
        values = []
        for index, value in enumerate(self.vec):
            values.append(value * other.vec[index])
        return sum(values)

    def magnitude(self):
        values = []
        for index, value in enumerate(self.vec):
            values.append(value ** 2)
        magn = sum(values)
        return magn ** 0.5


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix
        self.shape = (len(matrix), len(matrix[0]))

    def __str__(self):
        return "{}".format(self.matrix)

    def matrix_row(self, row):
        return self.matrix[row]

    def matrix_col(self, col):
        col_list = []
        for row in self.matrix:
            col_list.append(row[col])
        return col_list

    def __add__(self, other):
        self.shape_checker(other)
        added_matrix = []
        for index, row in enumerate(self.matrix):
            added_row = []
            for ind, val in enumerate(row):
                added_row.append(val + other.matrix[index][ind])
            added_matrix.append(added_vector)
        return Matrix(added_matrix)

    def __sub__(self, other):
        self.shape_checker(other)
        subtract_matrix = []
        for index, row in enumerate(self.matrix):
            subtract_row = []
            for ind, val in enumerate(row):
                subtract_row.append(val - other.matrix[index][ind])
            subtract_matrix.append(subtract_row)
        return Matrix(subtract_matrix)

    def matrix_scalar_multiply(self, other):
        output_matrix = []
        for row in self.matrix:
            output_row = []
            for col in row:
                output_row.append(col * other)
            output_matrix.append(output_row)
        return Matrix(output_matrix)

    def matrix_vector_multiply(self, other):
        if len(self.matrix[0]) != other.shape:
            raise ShapeException()
        output_vector = []
        for row in self.matrix:
            output_row = []
            for index, value in enumerate(row):
                output_row.append(value * other.vec[index])
            output_vector.append(sum(output_row))
        return Vector(output_vector)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.matrix_vector_multiply(other)
        elif isinstance(other, self.__class__):
            print("That's too hard for me!")
        else:
            return self.matrix_scalar_multiply(other)

    def __eq__(self, other):
        if self.matrix == other.matrix:
            return True
        else:
            return False
