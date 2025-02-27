import pygame
from entities.player import Player

class GameScene:
    def __init__(self):
        self.player = Player(400, 300)

        # Lista de obstáculos (x, y, largura, altura)
        self.obstacles = [
            pygame.Rect(200, 200, 100, 100),  # Exemplo: um bloco de parede
            pygame.Rect(500, 400, 80, 80),   # Outra parede
        ]

    def update(self, events):
        self.player.update(events, self.obstacles)

    def render(self, screen):
        screen.fill((30, 30, 30))  # Fundo
        
        # Desenha obstáculos
        for obstacle in self.obstacles:
            pygame.draw.rect(screen, (139, 69, 19), obstacle)  # Marrom para obstáculos

        self.player.render(screen)
