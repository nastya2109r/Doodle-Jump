import pygame
from scripts.game import Game
from scripts.functions import load_image

class App:
    def __init__(self):
        self.running = True
        self.FPS = 60
        self.scene = pygame.display.set_mode((480, 720))
        self.clock = pygame.time.Clock() 
        self.game = Game()
        pygame.display.set_caption("Doodle Jump")
        pygame.display.set_icon(load_image("assets", "icons", "icon.ico"))
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.game.process_key_down_event(event.key)
            elif event.type == pygame.KEYUP:
                self.game.process_key_up_event(event.key)

    def update(self):
        self.game.update_objects()

    def render(self):
        self.scene.fill((0, 0, 0))
        self.game.render_objects(self.scene)
        pygame.display.update()

    
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()

            self.clock.tick(self.FPS)