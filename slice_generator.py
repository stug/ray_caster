import math

from ray_caster import RayCaster
from vector import Vector


class RayGenerator(object):

    def __init__(self, number_of_steps, fov_angle):
        self.number_of_steps = number_of_steps
        self.fov_angle = fov_angle
        self.parallel_component = math.cos(fov_angle)
        self.perpendicular_step = math.sin(fov_angle)/(number_of_steps/2)

    def __iter__(self):
        for i in range(self.number_of_steps):
            yield (
                self.parallel_component,
                (float(i) - (self.number_of_steps/2)) * self.perpendicular_step
            )


class SliceGenerator(object):

    def __init__(self, arena, frame_width=200, frame_height=200, fov_angle=math.pi/3.0):
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.fov_angle = fov_angle
        self.arena = arena

    def generate_slices(self, position, direction):
        direction_perp = Vector(direction.y, -direction.x)
        ray_caster = RayCaster(self.arena, position)
        for parallel_component, perpendicular_component in RayGenerator(
            self.frame_width,
            self.fov_angle
        ):
            found_block = ray_caster.cast_ray(
                Vector.build_with_basis(
                    parallel_component,
                    perpendicular_component,
                    direction,
                    direction_perp
                )
            )
            yield found_block.block.build_slice(
                self.frame_height,
                position.find_distance_along_vector(found_block.intersection, direction),
                face=None,
                position_on_face=None
            )
