class Block(object):

    def __init__(self, height, color=None):
        self.height = height
        self.color = color

    def build_slice(self, ):
        pass


class Square(object):

    def __init__(self, contents=None):
        self.contents = contents

    @property
    def is_occupied(self):
        self.contents is not None


class OutOfBoundsError(Exception): pass


class Arena(object):

    def __init__(self, x_size, y_size):
        self.x_size = x_size
        self.y_size = y_size
        self._stuff = tuple([Square() for _ in range(x_size*y_size)])

    def __getitem__(self, (x, y)):
        if x >= self.x_size: raise OutOfBoundsError()
        if y >= self.y_size: raise OutOfBoundsError()
        return self._stuff[self.y_size*y + x]