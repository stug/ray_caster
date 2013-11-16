import math

import pygame

import scene_drawer
from test_arena import test_arena
from vector import Vector


class Player(object):

    def __init__(self, position=Vector(5,5), angle=0, step_size=0.1, rotation_step_size=math.pi/80):
        self.angle = angle
        self.position = position
        self.step_size = step_size
        self.rotation_step_size = rotation_step_size

    def forward(self):
        self._walk(self.step_size)

    def backward(self):
        self._walk(-self.step_size)

    def _walk(self, distance):
        self.position += self.direction * distance
        print self.position

    def rotate_left(self):
        self._rotate(self.rotation_step_size)

    def rotate_right(self):
        self._rotate(-self.rotation_step_size)

    def _rotate(self, amount):
        self.angle += amount

    @property
    def direction(self):
        return Vector(math.cos(self.angle), math.sin(self.angle))


class Game(object):

    def __init__(self, horizontal_resolution=200, vertical_resolution=200):
        screen = pygame.display.set_mode((horizontal_resolution, vertical_resolution))

        # TODO: scene drawer should probably entirely encapsulate pixel_drawer?
        self.pixel_drawer = scene_drawer.PyGamePixelDrawer(screen)
        self.scene_drawer = scene_drawer.SceneDrawer(self.pixel_drawer, test_arena)
        self.player = Player()

    def run(self):
        while self._should_continue():
            self.pixel_drawer.clear()
            self.scene_drawer.draw_scene(self.player.position, self.player.direction)
            pygame.display.flip()
            self._check_for_keys()

    def _check_for_keys(self):
        # TODO: add key to action map
        # also, should Dude handle his own movement?
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w]:
            self.player.forward()
        if keys_pressed[pygame.K_s]:
            self.player.backward()
        if keys_pressed[pygame.K_a]:
            self.player.rotate_left()
        if keys_pressed[pygame.K_d]:
            self.player.rotate_right()

    def _should_continue(self):
        should_continue = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                should_continue = False
        return should_continue


if __name__ == '__main__':
    Game().run()
