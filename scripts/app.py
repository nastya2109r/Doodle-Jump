import os 
import pygame
from scripts.game import Game

class App:
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        pass

    def render(self):
        self.scene.fill((0, 0, 0))
        self.game.render_objects(self.scene)
        pygame.display.update()

    def __init__(self):
        pygame.display.set_caption("Doodle Jump")
        image = pygame.image.load(os.path.join("assets", "icons", "icon.ico"))
        pygame.display.set_icon(image)
        self.running = True
        self.FPS = 60
        self.scene = pygame.display.set_mode((480, 720))
        self.clock = pygame.time.Clock() 
        self.game = Game()
    
    
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()

            self.clock.tick(self.FPS)