from collections import namedtuple
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
        return type(self)(other_vector.x + self.x, other_vector.y + self.y)

    def __repr__(self):
        return 'Vector({0}, {1})'.format(self.x, self.y)

    def find_distance_from_vector(self, other_vector):
        return math.sqrt((other_vector.x - self.x)**2 + (other_vector.y - self.y)**2)


class GridIterator(object):

    def __init__(self, position, direction):
        self.current_position = position
        self.direction = direction

    def __iter__(self):
        while True:
            yield self._get_next_grid_intersection()

    def _get_next_grid_intersection(self):
        import ipdb; ipdb.set_trace()
        vertical_intersection_dist = self._get_dist_to_next_whole_number(
            self.current_position.x
        )
        horizontal_intersection_dist = self._get_dist_to_next_whole_number(
            self.current_position.y
        )
        amount_to_advance = min(
            self._divide_safely(
                vertical_intersection_dist,
                self.direction.x
            ),
            self._divide_safely(
                horizontal_intersection_dist,
                self.direction.y
            )
        )
        self.current_position += self.direction * amount_to_advance
        return self.current_position

    @staticmethod
    def _get_dist_to_next_whole_number(current_coord):
        """Important that, if we're at a current whole number, we get the next
        whole number rather than just returning the current position.
        """
        return math.ceil(current_coord) - current_coord or 1.0

    @staticmethod
    def _divide_safely(numerator, denominator):
        if denominator == 0:
            return float('inf')
        return numerator/denominator
