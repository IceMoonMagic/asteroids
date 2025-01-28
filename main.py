from typing import cast

import pygame

from asteroid import Asteroid
from astroidfield import AsteroidField
from circleshape import CircleShape
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
    shots = pygame.sprite.Group()
    do_frame_process = pygame.sprite.Group()
    do_frame_draw = pygame.sprite.Group()

    Player.containers = (do_frame_process, do_frame_draw)
    player = Player(pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

    Asteroid.containers = (asteroids, do_frame_process, do_frame_draw)
    AsteroidField.containers = (do_frame_process,)
    field = AsteroidField()

    Shot.containers = (do_frame_process, do_frame_draw, shots)

    # Main Loop
    while True:
        # Handle Input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Process
        for to_process in do_frame_process:
            to_process.frame_process(delta)

        for asteroid in asteroids:
            cast(asteroid, Asteroid)
            if asteroid.is_colliding(player):
                print("Game Over!")
                exit(0)
            for shot in shots:
                cast(shot, Shot)
                if asteroid.is_colliding(shot):
                    shot.kill()
                    asteroid.split()

        # Draw Frame
        screen.fill((0, 0, 0))
        for to_draw in do_frame_draw:
            cast(to_draw, CircleShape)
            to_draw.frame_draw(screen)

        pygame.display.flip()

        # Limit Frame Rate
        delta = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
