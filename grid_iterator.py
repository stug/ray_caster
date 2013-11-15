import math


class GridIterator(object):

    def __init__(self, position, direction):
        self.current_position = position
        self.direction = direction

    def __iter__(self):
        while True:
            yield self._get_next_grid_intersection()

    def _get_next_grid_intersection(self):
        vertical_intersection_dist = self._get_dist_to_next_whole_number(
            self.current_position.x,
            self.direction.x
        )
        horizontal_intersection_dist = self._get_dist_to_next_whole_number(
            self.current_position.y,
            self.direction.y
        )
        amount_to_advance = min(
            math.fabs(self._divide_safely(
                vertical_intersection_dist,
                self.direction.x
            )),
            math.fabs(self._divide_safely(
                horizontal_intersection_dist,
                self.direction.y
            ))
        )
        self.current_position += self.direction * amount_to_advance
        return self.current_position

    def _get_dist_to_next_whole_number(self, current_coord, magnitude_of_direction):
        """Important that, if we're at a current whole number, we get the next
        whole number rather than just returning the current position.
        """
        rounding_function = math.ceil if magnitude_of_direction > 0 else math.floor
        return rounding_function(current_coord) - current_coord or 1.0

    @staticmethod
    def _divide_safely(numerator, denominator):
        if denominator == 0:
            return float('inf')
        return numerator/denominator
