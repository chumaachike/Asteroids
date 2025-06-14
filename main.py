# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")
    print (f"Asteroid min raduis: {ASTEROID_MIN_RADIUS} ")
    print (f"ASTEROID_KINDS: {ASTEROID_KINDS}")
    print(f"ASTEROID_SPAWN_RATE: {ASTEROID_SPAWN_RATE}")
    print (f"ASTEROID_MAX_RADIUS: {ASTEROID_MAX_RADIUS}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Fill screen with black
        pygame.display.flip()
        clock.tick(60)  # Limit to 60 frames per second

    pygame.quit()


if __name__ == "__main__":
    main()