import pygame
from constants import *

class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)

    def draw(self, screen):
        pygame.draw.rect(screen, "White", self.rect)

    def update(self, dt, up_key, down_key):
        direction = 0
        if up_key:
            direction -= 1
        if down_key:
            direction += 1
        self.rect.y += direction * PADDLE_SPEED * dt
        self.rect.y = max(0, min(self.rect.y, SCREEN_HEIGHT - self.rect.height))

    def machine_update(self, dt, ball):
        ignorezone = 10
        direction = 0

        diff = ball.rect.centery - self.rect.centery

        if diff < -ignorezone:
            direction = -1
        elif diff > ignorezone:
            direction = 1
        else:
            direction = 0  

        self.rect.y += direction * PADDLE_SPEED * dt
        self.rect.y = max(0, min(self.rect.y, SCREEN_HEIGHT - self.rect.height))
