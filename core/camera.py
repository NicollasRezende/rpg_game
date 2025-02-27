import pygame

class Camera:
    def __init__(self, width, height, world_width, world_height, player):
        self.width = width
        self.height = height
        self.world_width = world_width
        self.world_height = world_height
        
        # Inicializa a câmera centralizada no jogador
        self.offset_x = max(0, min(player.rect.centerx - self.width // 2, world_width - self.width))
        self.offset_y = max(0, min(player.rect.centery - self.height // 2, world_height - self.height))


    def update(self, target):
        self.offset_x = max(0, min(target.rect.centerx - self.width // 2, 2000 - self.width))
        self.offset_y = max(0, min(target.rect.centery - self.height // 2, 2000 - self.height))


    def apply(self, rect):
        """ Ajusta a posição de um objeto de acordo com o deslocamento da câmera """
        return rect.move(-self.offset_x, -self.offset_y)
