import pygame
import random
from constants import *

class Ball:
    def __init__(self, x, y, vx, vy, radius):
        width = radius * 2
        height = radius * 2
        self.vx = vx
        self.vy = vy
        self.rect = pygame.Rect(x, y, width, height)
        
    def reset(self, direction):
        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT // 2
        self.vx = BALL_SPEED * direction
        self.vy = BALL_SPEED * random.uniform(-0.5, 0.5)

    def draw(self, screen):
        pygame.draw.ellipse(screen, "White", self.rect)

    def update(self, dt, paddle, machine):
        self.rect.x += self.vx * dt
        self.rect.y += self.vy * dt
        if self.rect.top <= 0:
            self.rect.top = 0
            self.vy *= -1
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.vy *= -1
        if self.rect.colliderect(paddle.rect):
            self.vx = abs(self.vx)
            self.vy += random.uniform(-60, 60)

        elif self.rect.colliderect(machine.rect):
            self.vx = -self.vx
            self.vy += random.uniform(-60, 60)

            