import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def frame_process(self, delta: float):
        self.position += self.velocity * delta

    def frame_draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return

        deflection_angle = random.uniform(20, 50)
        spawn_velocity = self.velocity.rotate(deflection_angle) * 1.2
        self.velocity = self.velocity.rotate(-deflection_angle) * 1.2
        self.radius = self.radius - ASTEROID_MIN_RADIUS

        self.__class__(self.position.copy(), self.radius, spawn_velocity)
