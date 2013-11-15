import Tkinter
#from painter import Painter
#from grid_iterator import Vector


class TkinterPixelDrawer(object):

    def __init__(self, canvas):
        self.canvas = canvas

    def write_pixel(self, (x, y), fill):
        x = x*4
        y = y*4
        return self.canvas.create_rectangle(x, y, x+3, y+3, fill=fill)

    __setitem__ = write_pixel


class SceneDrawer(object):

    def __init__(self, pixel_drawer, arena):
        self.pixel_drawer = pixel_drawer
        self.arena = arena
        self.slice_generator = Painter(arena)

    def draw_scene(self):
        for y, pixel_slice in enumerate(
            slice_generator.generate_slices(
                Vector(1, 1),
                Vector(2, 1)
            )
        ):
            for x, pixel in enumerate(pixel_slice):
                if pixel:
                    self.pixel_drawer.write_pixel((x, y), '#FFFFFF')


if __name__ == '__main__':
    top = Tkinter.Tk()
    pd = TkinterPixelDrawer(
        Tkinter.Canvas(top, height=500, width=500, background='black')
    )
    import ipdb; ipdb.set_trace()
    print 2
