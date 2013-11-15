from collections import namedtuple
import math

import arena
import grid_iterator


FoundBlock = namedtuple('FoundBlock' ['black', 'intersection'])


class RayCaster(object):

    def __init__(self, arena, position):
        self.arena = arena
        self.position = position

    def cast_ray(self, direction):
        for potential_intersection in GridIterator(self.position, direction):
            square = arena[self._get_coordinates_to_check(potential_intersection, direction)]
            if square.is_occupied:
                return FoundBlock(square.contents, potential_intersection)

    @staticmethod
    def _get_coordinates_to_check(potential_intersection, direction):
        return (
            self._get_index_to_check(potential_intersection.x, direction.x)
            self._get_index_to_check(potential_intersection.y, direction.y)
        )

    @staticmethod
    def _get_index_to_check(coordinate, direction_in_coordinate):
        if coordinate.is_integer():
            if direction_in_coordinate < 0:
                return coordinate - 1
        return math.floor(coordinate)