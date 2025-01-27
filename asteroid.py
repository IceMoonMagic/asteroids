import pygame

from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def update(self, delta):
        self.position += self.velocity * delta
        pass

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
