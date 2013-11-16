from slice_generator import SliceGenerator


class PyGamePixelDrawer(object):

    def __init__(self, screen):
        self.screen = screen

    def write_pixel(self, (x, y), fill):
        self.screen.set_at((x,y), fill)

    __setitem__ = write_pixel

    def clear(self):
        self.screen.fill((0,0,0))


class SceneDrawer(object):

    def __init__(self, pixel_drawer, arena):
        self.pixel_drawer = pixel_drawer
        self.arena = arena
        self.slice_generator = SliceGenerator(arena)

    def draw_scene(self, position, direction):
        for x, pixel_slice in enumerate(
            self.slice_generator.generate_slices(
                position,
                direction
            )
        ):
            for y, pixel in enumerate(pixel_slice):
                if pixel:
                    self.pixel_drawer.write_pixel((x, y), pixel)
