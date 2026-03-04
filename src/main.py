import pygame
import sys
import random

# ===============
# Classes
# ===============

class Player:
    """Simple player wrapper around a pygame.Rect with movement and draw helpers."""

    def __init__(self, center_x: int, center_y: int, width: int = 20, height: int = 20, speed: int = 5, color=(125, 0, 0)):
        # Create the rect and place it centered at the given coordinates
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = (center_x, center_y)
        self.speed = speed
        self.color = color

    def move(self, keys, boundary_width: int, boundary_height: int):
        """Move the player according to pressed keys while keeping it inside the screen bounds."""
        if keys[pygame.K_a] and self.rect.left > 0:  # Move left
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.right < boundary_width:  # Move right
            self.rect.x += self.speed
        if keys[pygame.K_w] and self.rect.top > 0:  # Move up
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.bottom < boundary_height:  # Move down
            self.rect.y += self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

class Enemy:

    def __init__(self, x, y, radius = 10, speed: int = 5, color=(255, 255, 255)):
        # Initialize the enemy's position, size, speed, and color
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

        # Random initial direction
        self.dx = random.choice([-1, 1]) * speed
        self.dy = random.choice([-1, 1]) * speed

    def move(self, boundary_width: int, boundary_height: int):
        """Move the enemy in its current direction and bounce off the walls."""
        # Update position
        self.x += self.dx
        self.y += self.dy

        # Bounce off the walls
        if self.x - self.radius <= 0 or self.x + self.radius >= boundary_width:
            self.dx *= -1
        if self.y - self.radius <= 0 or self.y + self.radius >= boundary_height:
            self.dy *= -1

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)

# ===============
# Main Game Loop
# ===============
def main():
    pygame.init()

    # Windows setup
    width, height = 800,600
    screen = pygame.display.set_mode((width, height)) # Create a window of specified width and height
    pygame.display.set_caption("Rogue-like Game")

    # Set a background color (RGB)
    background_color = (10, 10, 10)  # Dark gray background

    # Player setup
    # Use the Player class instead of a raw Rect
    player = Player(width // 2, height // 2)  # Start the player in the center of the screen

    # Enemy setup
    enemy = Enemy(random.randint(20, width-20), random.randint(20, height-20))  # Start the enemy at a random position

    clock = pygame.time.Clock() # Create a clock object to control the frame rate

    while True:
        # Fill the screen with background color
        screen.fill(background_color)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        # Detect key presses for movement and update the player
        keys = pygame.key.get_pressed()
        player.move(keys, width, height)

        # Draw the player
        player.draw(screen)

        # Draw the enemy
        enemy.move(width, height)
        enemy.draw(screen)

        # Update the display and control the frame rate
        pygame.display.flip()  # Update the display
        clock.tick(90)  # Limit to 90 frames per second

# Run the main function with error handling
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
        pygame.quit()
        sys.exit(1)