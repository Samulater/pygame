import pygame

from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit the game loop

        screen.fill((0, 0, 0))  # Fills the screen with black
        pygame.display.flip()   # Updates the entire screen

if __name__ == "__main__":
    main()