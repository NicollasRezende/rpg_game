import pygame
from entities.player import Player
from core.camera import Camera
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from core.background import Background



class GameScene:
    def __init__(self):
        self.player = Player(450, 450)  # Spawn perto do primeiro obstáculo

        # Criar a câmera (supondo que o mapa seja maior que a tela)
        self.camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT, 2000, 2000, self.player)

        self.background = Background(2000, 2000)

        # Lista de obstáculos (x, y, largura, altura)
        self.obstacles = [
            pygame.Rect(200, 200, 100, 100),
            pygame.Rect(600, 500, 80, 80),
            pygame.Rect(1000, 400, 120, 100)
        ]

    def update(self, events):
        self.player.update(events, self.obstacles)
        self.camera.update(self.player)
        print(f"Camera Offset: {self.camera.offset_x}, {self.camera.offset_y}")  # Debug

    def render(self, screen):
        screen.fill((30, 30, 30))  # Fundo

        # Renderiza background
        self.background.render(screen, self.camera)
        
        # Debug para ver se o jogador está sendo desenhado
        print(f"Player Pos: {self.player.rect.x}, {self.player.rect.y}")

        for obstacle in self.obstacles:
            pygame.draw.rect(screen, (139, 69, 19), self.camera.apply(obstacle))

        # Renderiza o jogador
        player_rect = self.camera.apply(self.player.rect)
        pygame.draw.rect(screen, self.player.color, player_rect)


        # Renderizar o jogador ajustando pela câmera
        player_rect = self.camera.apply(self.player.rect)
        pygame.draw.rect(screen, self.player.color, player_rect)



