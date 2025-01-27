import pygame

from constants import *
from player import Player


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

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Main Loop
    while True:
        # Handle Input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Process

        # Draw Frame
        screen.fill((0, 0, 0))
        player.draw(screen)

        pygame.display.flip()

        # Limit Frame Rate
        delta = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
