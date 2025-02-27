import pygame

class SceneManager:
    def __init__(self):
        self.scenes = {}
        self.current_scene = None

    def add_scene(self, name, scene):
        self.scenes[name] = scene

    def set_scene(self, name):
        if name in self.scenes:
            self.current_scene = self.scenes[name]

    def update(self, events):
        if self.current_scene:
            self.current_scene.update(events)

    def render(self, screen):
        if self.current_scene:
            self.current_scene.render(screen)
