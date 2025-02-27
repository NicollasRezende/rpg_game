import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

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

    def update(self, events, obstacles):
        keys = pygame.key.get_pressed()
        speed = 5
        new_x, new_y = self.rect.x, self.rect.y

        if keys[pygame.K_w]:
            new_y -= speed
        if keys[pygame.K_s]:
            new_y += speed
        if keys[pygame.K_a]:
            new_x -= speed
        if keys[pygame.K_d]:
            new_x += speed

        # Criar um novo retângulo para testar a posição futura
        new_rect = self.rect.move(new_x - self.rect.x, new_y - self.rect.y)

        # Verificar se colide com algum obstáculo
        if not any(new_rect.colliderect(obst) for obst in obstacles):
            # Só move se não houver colisão
            if 0 <= new_x <= SCREEN_WIDTH - self.rect.width:
                self.rect.x = new_x
            if 0 <= new_y <= SCREEN_HEIGHT - self.rect.height:
                self.rect.y = new_y
