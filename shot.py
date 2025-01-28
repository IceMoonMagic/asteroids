import pygame

from circleshape import CircleShape
from constants import SHOT_RADIUS


class Shot(CircleShape):
    def __init__(self, position: pygame.Vector2):
        super().__init__(position, SHOT_RADIUS)

    def frame_process(self, delta):
        self.position += self.velocity * delta

    def frame_draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
