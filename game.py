import math

import pygame

from slice_generator import SliceGenerator
from vector import Vector

from test_sim import generate_test_scene


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

    def draw_scene(self, direction):
        for x, pixel_slice in enumerate(
            self.slice_generator.generate_slices(
                Vector(5, 5),
                direction
            )
        ):
            for y, pixel in enumerate(pixel_slice):
                if pixel:
                    self.pixel_drawer.write_pixel((x, y), pixel)


if __name__ == '__main__':
    screen = pygame.display.set_mode((200, 200))
    clock = pygame.time.Clock()
    pd = PyGamePixelDrawer(screen)
    sd = SceneDrawer(pd, generate_test_scene())
    running = True
    t = 0
    while running:
        pd.clear()
        sd.draw_scene(Vector(math.sin(t), math.cos(t)))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
        clock.tick(1000)
        t += math.pi/100.0
