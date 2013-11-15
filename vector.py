import math


class Vector(object):

    @classmethod
    def build_with_basis(
        cls,
        parallel_component,
        perpendicular_component,
        parallel_vector,
        perpendicular_vector
    ):
        return parallel_vector * parallel_component + perpendicular_vector * perpendicular_component

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, scale):
        return type(self)(scale*self.x, scale*self.y)

    def __add__(self, other_vector):
        return type(self)(self.x + other_vector.x, self.y + other_vector.y)

    def __sub__(self, other_vector):
        return type(self)(self.x - other_vector.x, self.y - other_vector.y)

    def dot(self, other_vector):
        return self.x*other_vector.x + self.y*other_vector.y

    def __repr__(self):
        return 'Vector({0}, {1})'.format(self.x, self.y)

    def __len__(self):
        return math.sqrt(self.dot(self))

    def find_distance_along_vector(self, point, direction):
        self_to_point = point - self
        return self_to_point.dot(direction)
