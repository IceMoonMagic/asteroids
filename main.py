import pygame

from constants import *


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

    # Main Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))

        # End of Frame
        pygame.display.flip()
        delta = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
