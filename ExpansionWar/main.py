import asyncio

import pygame
import sys

import config
from game_scene import GameScene

import logging
logger = logging.getLogger(__name__)
from pygame_logger import PygameHandler


pygame.init()

screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption("Planet Conqueror")
clock = pygame.time.Clock()

async def main():
    config.current_scene = GameScene(1, 2100)

    running = True
    while running:
        screen.blit(config.background, (0, 0), (0, 0, config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    config.current_scene.handle_click(event.pos)
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    config.current_scene.handle_mouse_up(event.pos)
            elif event.type == pygame.MOUSEMOTION:
                config.current_scene.handle_mouse_motion(event.pos)

        config.current_scene.draw(screen)
        if config.ENABLE_PYGAME_LOG:
            pygame_handler.draw(screen)

        pygame.display.flip()
        clock.tick(60)
        await asyncio.sleep(0)

pygame_handler = None
def setup_logger():
    global pygame_handler
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    pygame_handler = PygameHandler(config.PYGAME_LOG_LIMIT)
    pygame_handler.setLevel(logging.DEBUG)
    pygame_handler.setFormatter(formatter)
    logger.addHandler(pygame_handler)

if __name__ == "__main__":
    setup_logger()
    config.load_assets()
    asyncio.run(main())
