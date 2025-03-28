import os
import pygame

def scale(val, src, dst):
    return ((val - src[0]) / (src[1]-src[0])) * (dst[1]-dst[0]) + dst[0]

def lerp(x1: float, x2: float, y1: float, y2: float, x: float):
    return ((y2 - y1) * x + x2 * y1 - x1 * y2) / (x2 - x1)

ASSETS_FOLDER = "assets"

# Screen dimensions
BASE_WIDTH = 400
BASE_HEIGHT = 700

#UI and PLANET
GAME_INFO_BAR_HEIGHT = 50
PLANET_RADIUS = 30
PLANET_TEXT_SIZE = 24

# Colors
PLAYER_COLOR = (0, 0x78, 0x48)
NO_OWNER_COLOR = (0x81, 0x83, 0x80)
BACKGROUND_COLOR = (40, 40, 60)
CONNECTION_COLOR = (0x81, 0x83, 0x80)

#Scaled dimensions
SCREEN_WIDTH = 400*2
SCREEN_HEIGHT = 700*2
GAME_INFO_BAR_HEIGHT = scale(GAME_INFO_BAR_HEIGHT, (0, BASE_HEIGHT), (0, SCREEN_HEIGHT))
PLANET_RADIUS = scale(PLANET_RADIUS, (0, BASE_HEIGHT), (0, SCREEN_HEIGHT))
PLANET_TEXT_SIZE = int(scale(PLANET_TEXT_SIZE, (0, BASE_HEIGHT), (0, SCREEN_HEIGHT)))

GAME_SCENE_WIDTH = SCREEN_WIDTH
GAME_SCENE_HEIGHT = SCREEN_HEIGHT - GAME_INFO_BAR_HEIGHT

background = pygame.image.load(os.path.join(ASSETS_FOLDER, "GSFC_20171208_Archive_e000012~medium.jpg"))
background = pygame.transform.scale(background, [SCREEN_WIDTH, SCREEN_HEIGHT])

planet_assets = dict()
rocket_assets = dict()

def load_assets():
    print("Loading assets...")
    for file in os.listdir(os.path.join(ASSETS_FOLDER, "PlanetParts")):
        if not file.endswith(".png"):
            continue
        filename = file.split(".")[0]
        planet_assets[filename] = pygame.image.load(os.path.join(ASSETS_FOLDER, "PlanetParts", file))

    for file in os.listdir(os.path.join(ASSETS_FOLDER, "Rockets")):
        if not file.endswith(".png"):
            continue
        filename = file.split(".")[0]
        rocket_assets[filename] = pygame.image.load(os.path.join(ASSETS_FOLDER, "Rockets", file))
