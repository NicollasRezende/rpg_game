import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
import math

class Entity:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def update(self, events):
        pass

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

class Player(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, 40, 40, (0, 255, 0))  # Verde
        self.speed = 5  # Velocidade do jogador

    def update(self, events, obstacles):
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0  # Delta X e Delta Y (para movimento)

        if keys[pygame.K_w]:
            dy -= self.speed
        if keys[pygame.K_s]:
            dy += self.speed
        if keys[pygame.K_a]:
            dx -= self.speed
        if keys[pygame.K_d]:
            dx += self.speed

        # 🔹 Ajuste para manter velocidade igual em diagonal
        if dx != 0 and dy != 0:
            diagonal_factor = 1 / math.sqrt(2)  # Normaliza o vetor diagonal
            dx *= diagonal_factor
            dy *= diagonal_factor

        # 🔹 Verifica se a nova posição do jogador não colide com obstáculos
        new_rect = self.rect.move(dx, dy)
        if not any(new_rect.colliderect(obst) for obst in obstacles):
            self.rect.x += dx
            self.rect.y += dy

        # 🔹 Evita sair da tela
        self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, SCREEN_HEIGHT - self.rect.height))
