import math

from grid_iterator import Vector
from ray_caster import RayCaster


class RayGenerator(object):

    def __init__(self, number_of_steps, fov_angle):
        self.number_of_steps = number_of_steps
        self.fov_angle = fov_angle
        self.parallel_component = math.cos(fov_angle)
        self.perpendicular_step = math.sine(fov_angle)/(number_of_steps/2)

    def __iter__(self):
        for i in range(self.number_of_steps):
            yield (
                (float(i)-(number_of_steps/2)) * self.perpendicular_step,
                self.parallel_component
            )


class Painter(object):

    def __init__(self, frame_width, frame_height, fov_angle, arena):
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.fov_angle = fov_angle
        self.arena = arena

    def draw_scene(self, position, direction):
        direction_perp = Vector(direction.y, -direction.x)
        ray_caster = RayCaster(self.arena, position)
        for parallel_component, perpendicular_component in RayGenerator(self.frame_width, self.fov_angle):
            found_block = ray_caster.cast_ray(
                Vector.build_with_basis(
                    parallel_component,
                    perpendicular_component,
                    direction,
                    direction_perp
                )
            )