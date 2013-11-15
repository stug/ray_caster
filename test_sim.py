import math

from arena import Arena
from arena import Block
from slice_generator import SliceGenerator
from vector import Vector

def generate_test_scene():
    test_arena = Arena(10, 10)
    for i in range(10):
        test_arena[0, i].contents = Block('#0000FF')
        test_arena[9, i].contents = Block('#FF0000')
        test_arena[i, 0].contents = Block('#FFFF00')
        test_arena[i, 9].contents = Block('#00FF00')
    test_arena[9, 5].contents = Block('#FFFFFF')
    test_arena[5, 0].contents = Block('#FFFFFF')
    test_arena[0, 5].contents = Block('#FFFFFF')
    test_arena[5, 9].contents = Block('#FFFFFF')

    test_arena[7, 6].contents = Block('#00FFFF')
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

