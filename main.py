import Tkinter
from painter import Painter
from grid_iterator import Vector

from test_sim import generate_test_scene


class TkinterPixelDrawer(object):

    def __init__(self, canvas):
        self.canvas = canvas
        self.canvas.pack()

    def write_pixel(self, (x, y), fill):
        x = x*3
        y = y*3
        return self.canvas.create_rectangle(x, y, x+3, y+3, fill=fill)

    __setitem__ = write_pixel


class SceneDrawer(object):

    def __init__(self, pixel_drawer, arena):
        self.pixel_drawer = pixel_drawer
        self.arena = arena
        self.slice_generator = Painter(arena)

    def draw_scene(self):
        for x, pixel_slice in enumerate(
            self.slice_generator.generate_slices(
                Vector(1, 5),
                Vector(2, 1)
            )
        ):
            for y, pixel in enumerate(pixel_slice):
                if pixel:
                    self.pixel_drawer.write_pixel((x, y), '#FFFFFF')


if __name__ == '__main__':
    top = Tkinter.Tk()
    pd = TkinterPixelDrawer(
        Tkinter.Canvas(top, height=1000, width=1000, background='black')
    )
    SceneDrawer(pd, generate_test_scene()).draw_scene()
    import ipdb; ipdb.set_trace()
    print 4
    