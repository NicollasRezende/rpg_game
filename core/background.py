import pygame

class Background:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tile_size = 64  # Tamanho do tile do chão
        self.grass_texture = pygame.image.load("assets/grass.png").convert()

    def render(self, screen, camera):
        for x in range(0, self.width, self.tile_size):
            for y in range(0, self.height, self.tile_size):
                screen.blit(self.grass_texture, (x - camera.offset_x, y - camera.offset_y))
