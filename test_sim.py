import math

from arena import Arena
from arena import Block
from grid_iterator import Vector
from painter import Painter

def generate_test_scene():
    test_arena = Arena(10, 10)
    for i in range(10):
        test_arena[0, i].contents = Block()
        test_arena[9, i].contents = Block()
        test_arena[i, 0].contents = Block()
        test_arena[i, 9].contents = Block()
    test_arena[8, 7].contents = 1
    return test_arena


    painter = Painter(test_arena, 200, 200, math.pi/3.0)
    test_scene = []
    for column in painter.generate_slices(
        Vector(4.5, 5.5),
        Vector(0.5, 0.5)
    ):
        test_scene.append(column)

    return test_scene


if __name__ == '__main__':
    print generate_test_scene()
    
