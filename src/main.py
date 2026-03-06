import pygame
import sys
import random

def clamp(value, min_value, max_value):
    """Clamp a value between a minimum and maximum."""
    if value < min_value:
        return min_value

    if value > max_value:
        return max_value

    return value

# ===============
# Classes
# ===============

class Player:
    """Simple player using basic x/y movement."""

    def __init__(self, center_x, center_y, width=20, height=20, speed=5, color=(125, 0, 0)):
        self.x = center_x
        self.y = center_y
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color

        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = (self.x, self.y)

    def move(self, keys, boundary_width, boundary_height):

        # Move the player based on key input
        if keys[pygame.K_a]:
            self.x -= self.speed

        if keys[pygame.K_d]:
            self.x += self.speed

        if keys[pygame.K_w]:
            self.y -= self.speed

        if keys[pygame.K_s]:
            self.y += self.speed

        # Calculate half dimensions for boundary checking
        half_w = self.width // 2
        half_h = self.height // 2

        # Ensure the player doesn't go out of bounds by clamping the position
        self.x = clamp(self.x, half_w, (boundary_width - half_w))
        self.y = clamp(self.y, half_h, (boundary_height - half_h))

        # Update the rect position after moving
        self.rect.center = (self.x, self.y)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

class Enemy:
    def __init__(self, screen_width, screen_height, width = 20, height = 20, speed = 2, color = (255, 255, 255)):
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        self.x = random.randint(self.width // 2, screen_width - self.width // 2)
        self.y = random.randint(self.height // 2, screen_height - self.height // 2)

        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = (self.x, self.y)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

# ===============
# Main Game Loop
# ===============

def main():
    pygame.init() # Initialize Pygame

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

        pygame.display.flip() # Update the display
        clock.tick(90)

# Run the main function with error handling
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
        pygame.quit()
        sys.exit(1)