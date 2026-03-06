import pygame
import sys

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

        if keys[pygame.K_a]:
            self.x -= self.speed

        if keys[pygame.K_d]:
            self.x += self.speed

        if keys[pygame.K_w]:
            self.y -= self.speed

        if keys[pygame.K_s]:
            self.y += self.speed

        # Clamp inside window
        half_w = self.width // 2
        half_h = self.height // 2

        if self.x < half_w:
            self.x = half_w
        if self.x > boundary_width - half_w:
            self.x = boundary_width - half_w

        if self.y < half_h:
            self.y = half_h
        if self.y > boundary_height - half_h:
            self.y = boundary_height - half_h

        self.rect.center = (self.x, self.y)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)


# ===============
# Main Game Loop
# ===============

def main():
    pygame.init()

    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Rogue-like Game")

    background_color = (10, 10, 10)

    player = Player(width // 2, height // 2)

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

        pygame.display.flip()
        clock.tick(90)

# Run the main function with error handling
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
        pygame.quit()
        sys.exit(1)