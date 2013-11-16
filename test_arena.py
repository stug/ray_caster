from arena import Arena
from arena import Block


test_arena = Arena(10, 10)
for i in range(10):
    test_arena[0, i].contents = Block((0,0,255))
    test_arena[9, i].contents = Block((0,255,0))
    test_arena[i, 0].contents = Block((255,0,0))
    test_arena[i, 9].contents = Block((255,255,0))
test_arena[9, 5].contents = Block((255,255,255))
test_arena[5, 0].contents = Block((255,255,255))
test_arena[0, 5].contents = Block((255,255,255))
test_arena[5, 9].contents = Block((255,255,255))
test_arena[7, 6].contents = Block((0,255,255))
