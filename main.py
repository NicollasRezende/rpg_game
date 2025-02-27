import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from scenes.scene_manager import SceneManager
from scenes.game_scene import GameScene

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("RPG 2D")
    clock = pygame.time.Clock()

    scene_manager = SceneManager()
    scene_manager.add_scene("game", GameScene())
    scene_manager.set_scene("game")

    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        scene_manager.update(events)
        scene_manager.render(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
