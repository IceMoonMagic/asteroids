import pygame

from circleshape import CircleShape
from constants import (
    InputMap,
    PLAYER_RADIUS,
    PLAYER_SHOOT_COOLDOWN,
    PLAYER_SHOOT_SPEED,
    PLAYER_SPEED,
    PLAYER_TURN_SPEED,
)
from shot import Shot


class Player(CircleShape):
    def __init__(self, position: pygame.Vector2):
        super().__init__(position, PLAYER_RADIUS)
        self.rotation: float = 0
        self.shoot_cooldown: float = 0

    def frame_process(self, delta: float):
        self.shoot_cooldown = max(self.shoot_cooldown - delta, 0)
        keys: pygame.key.ScancodeWrapper = pygame.key.get_pressed()

        if InputMap.is_forward(keys):
            self.move(delta)
        if InputMap.is_backward(keys):
            self.move(-delta)
        if InputMap.is_left(keys):
            self.rotate(-delta)
        if InputMap.is_right(keys):
            self.rotate(delta)
        if InputMap.is_shoot(keys) and self.shoot_cooldown <= 0:
            self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN
            self.shoot()

    def frame_draw(self, screen: pygame.Surface):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def move(self, delta: float):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * delta

    def rotate(self, delta: float):
        self.rotation += PLAYER_TURN_SPEED * delta

    def shoot(self):
        shot = Shot(self.position.copy())
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation)
        shot.velocity *= PLAYER_SHOOT_SPEED

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = (
            pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        )
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
