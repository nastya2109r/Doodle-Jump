from random import randint
import pygame
from scripts.functions import load_image
from scripts.sprite import Sprite
from scripts.constants import display_size, create_platform_event


class PlatformGenerator:
    def __init__(self, step):
        self.step = step

    def create_start_configuration(self):
        platform = Sprite(
            load_image("assets", "images", "platform.png"),
            [display_size[0] / 2, display_size[1] - 50],
        )

        event = pygame.Event(create_platform_event, {"platform": platform})
        pygame.event.post(event)

        for y in range(display_size[1], 0, -self.step):
            self.create_platform(y)

    def create_platform(self, center_y):
        image = load_image("assets", "images", "platform.png")
        width = image.get_width()
        center_x = randint(width // 2, display_size[0] - width // 2)
        platform = Sprite(image, [center_x, center_y])

        event = pygame.Event(create_platform_event, {"platform": platform})
        pygame.event.post(event)

    def update(self, offset_y, platforms):
        if platforms[-1].rect.centery - offset_y >= self.step:
            self.create_platform(offset_y)
            platforms.remove(platforms[0])
