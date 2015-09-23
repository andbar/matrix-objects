class ShapeException(Exception):
    pass


class Vector():

    def __init__(self, vec):
        self.vec = vec
        self.shape = len(self.vec)

    def shape_checker(self, other):
        if self.shape != other.shape:
            raise ShapeException()

    def __add__(self, other):
        self.shape_checker(other)
        added_vector = []
        for index, value in enumerate(self.vec):
            added_vector.append(self.vec[index] + other.vec[index])
        return added_vector

    def __sub__(self, other):
        self.shape_checker(other)
        subtract_vector = []
        for index, value in enumerate(self.vec):
            subtract_vector.append(self.vec[index] - other.vec[index])
        return subtract_vector

    def __mul__(self, other):
        mult_vector = []
        for row in self.vec:
            mult_vector.append(row * other)
        return mult_vector

    def __eq__(self, other):
        if self.vec == other.vec:
            return True

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
