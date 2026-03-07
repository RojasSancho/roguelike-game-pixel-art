import pygame
import random

class Enemy:
    def __init__(self, screen_width, screen_height, width=20, height=20, speed=2, color=(255, 255, 255)):
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