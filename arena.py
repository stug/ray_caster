class Block(object):

    height = 1

    def __init__(self, color=None):
        self.color = color

    def build_slice(self, screen_height, distance, face, position_on_face):
        """Eventually we'll want to have texture and will need face, and position_on_face.
        For now we're ignoring them.
        """
        # TODO: this is gross but fine for now.
        num_filled_pixels = screen_height/(2*distance)
        pixel_fill_start = int((screen_height - num_filled_pixels)/2)
        pixel_slice = [0]*screen_height
        for i in range(int(num_filled_pixels)):
            pixel_slice[pixel_fill_start + i] = 1
        return pixel_slice


class Square(object):

    def __init__(self, contents=None):
        self.contents = contents

    @property
    def is_occupied(self):
        return self.contents is not None


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
