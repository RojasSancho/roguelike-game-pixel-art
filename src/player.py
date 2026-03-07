import pygame

def clamp(value, min_value, max_value):
    """Clamp a value between a minimum and maximum."""
    if value < min_value:
        return min_value

    if value > max_value:
        return max_value

    return value

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