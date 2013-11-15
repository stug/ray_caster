from collections import namedtuple
import math

from grid_iterator import GridIterator


FoundBlock = namedtuple('FoundBlock', ['block', 'intersection'])


class RayCaster(object):

    def __init__(self, arena, position):
        self.arena = arena
        self.position = position

    def cast_ray(self, direction):
        for potential_intersection in GridIterator(self.position, direction):
            coords =  self._get_coordinates_to_check(potential_intersection, direction)
            square = self.arena[self._get_coordinates_to_check(potential_intersection, direction)]
            if square.is_occupied:
                return FoundBlock(square.contents, potential_intersection)

    @staticmethod
    def _get_coordinates_to_check(potential_intersection, direction):
        return (
            int(RayCaster._get_index_to_check(potential_intersection.x, direction.x)),
            int(RayCaster._get_index_to_check(potential_intersection.y, direction.y))
        )

    @staticmethod
    def _get_index_to_check(coordinate, direction_in_coordinate):
        if coordinate.is_integer():
            if direction_in_coordinate < 0:
                return coordinate - 1
        return math.floor(coordinate)
