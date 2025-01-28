import pygame

from asteroid import Asteroid
from astroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen: pygame.Surface = pygame.display.set_mode(
        (SCREEN_WIDTH, SCREEN_HEIGHT)
    )
    clock = pygame.time.Clock()
    delta: float = 0

    asteroids = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    field = AsteroidField()

    Shot.containers = (updatable, drawable, shots)

    # Main Loop
    while True:
        # Handle Input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Process
        for _updatable in updatable:
            _updatable.update(delta)

        for astroid in asteroids:
            if astroid.is_colliding(player):
                print("Game Over!")
                exit(0)
            for shot in shots:
                if astroid.is_colliding(shot):
                    shot.kill()
                    astroid.split()

        # Draw Frame
        screen.fill((0, 0, 0))
        for _drawable in drawable:
            _drawable.draw(screen)

        pygame.display.flip()

        # Limit Frame Rate
        delta = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
