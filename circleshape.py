import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(
        self,
        position: pygame.Vector2,
        radius: float,
        velocity: pygame.Vector2 | None = None,
    ):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position: pygame.Vector2 = position
        self.velocity: pygame.Vector2 = velocity or pygame.Vector2(0, 0)
        self.radius: float = radius

    def frame_process(self, delta: float):
        # sub-classes must override
        pass

    def frame_draw(self, screen: pygame.Surface):
        # sub-classes must override
        pass

    def is_colliding(self, other: "CircleShape") -> bool:
        distance_apart = self.position.distance_to(other.position)
        radii = self.radius + other.radius
        return distance_apart < radii
