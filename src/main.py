import pygame
import sys
import random

from player import *
from enemy import *

# ===============
# Main Game Loop
# ===============

def main():
    pygame.init()  # Initialize Pygame

    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Rogue-like Game")

    background_color = (10, 10, 10)

    player = Player(width // 2, height // 2)
    enemy = Enemy(width, height)
    print(player.x, player.y)
    print(enemy.x, enemy.y)

    clock = pygame.time.Clock()

    while True:

        screen.fill(background_color)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        player.move(keys, width, height)

        player.draw(screen)
        enemy.draw(screen)

        pygame.display.flip()  # Update the display
        clock.tick(90)


pygame.quit()

# Run the main function with error handling
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
        pygame.quit()
        sys.exit(1)
