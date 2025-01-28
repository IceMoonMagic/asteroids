import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def update(self, delta):
        self.position += self.velocity * delta
        pass

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)
        rotate1 = self.velocity.rotate(angle)
        rotate2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        child1 = self.__class__(self.position.x, self.position.y, new_radius)
        child1.velocity = rotate1 * 1.2
        child2 = self.__class__(self.position.x, self.position.y, new_radius)
        child2.velocity = rotate2 * 1.2
