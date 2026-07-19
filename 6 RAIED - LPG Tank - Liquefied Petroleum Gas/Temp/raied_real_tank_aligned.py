import pygame
import math
import sys

pygame.init()

ORANGE = (255, 140, 0)
BLUE = (0, 150, 255)
WHITE = (240, 240, 240)

font = pygame.font.SysFont(None, 24)

# -----------------------------
# LOAD IMAGE SAFELY (NO convert_alpha YET)
# -----------------------------
try:
    raw_img = pygame.image.load("tank.png")   # <-- SAFE
except Exception as e:
    print("Could not load tank.png:", e)
    pygame.quit()
    sys.exit()

IMG_W, IMG_H = raw_img.get_width(), raw_img.get_height()

# NOW create the window
WIN = pygame.display.set_mode((IMG_W, IMG_H))
pygame.display.set_caption("RAIED - Shutters Aligned to Real Frame")

# NOW convert the image (AFTER window exists)
tank_img = raw_img.convert_alpha()

# -----------------------------
# GEOMETRY FROM YOUR MEASUREMENTS
# -----------------------------
CENTER_X = 175
CENTER_Y = 363

TOP_X = 190
TOP_Y = 130

dx = TOP_X - CENTER_X
dy = TOP_Y - CENTER_Y
RADIUS = math.hypot(dx, dy)

FIRST_ANGLE = math.atan2(dy, dx)

# -----------------------------
# SHUTTER PARAMETERS
# -----------------------------
NUM_SHUTTERS = 8
MAX_OFFSET = 160
DEPLOY_SPEED = 4

SHUTTER_WIDTH = 6  # approx. 25 mm visually

shutters = []
for i in range(NUM_SHUTTERS):
    angle = FIRST_ANGLE + i * (2 * math.pi / NUM_SHUTTERS)
    shutters.append({"angle": angle, "offset": 0})

deploying = False
retracting = False

# -----------------------------
# DRAW SHUTTER
# -----------------------------
def draw_shutter(s):
    angle = s["angle"]
    offset = s["offset"]

    ux = math.cos(angle)
    uy = math.sin(angle)

    base_x = CENTER_X + ux * RADIUS
    base_y = CENTER_Y + uy * RADIUS

    end_x = CENTER_X + ux * (RADIUS + offset)
    end_y = CENTER_Y + uy * (RADIUS + offset)

    pygame.draw.line(
        WIN,
        ORANGE,
        (int(base_x), int(base_y)),
        (int(end_x), int(end_y)),
        SHUTTER_WIDTH
    )

# -----------------------------
# MAIN LOOP
# -----------------------------
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_SPACE:
                deploying = True
                retracting = False
            if event.key == pygame.K_r:
                retracting = True
                deploying = False

    WIN.blit(tank_img, (0, 0))

    WIN.blit(font.render("SPACE: Deploy   R: Retract   ESC: Quit", True, BLUE), (10, 10))
    WIN.blit(font.render("RAIED: Shutters aligned to real frame", True, WHITE), (10, 35))

    for s in shutters:
        if deploying:
            s["offset"] = min(s["offset"] + DEPLOY_SPEED, MAX_OFFSET)
        if retracting:
            s["offset"] = max(s["offset"] - DEPLOY_SPEED, 0)

    for s in shutters:
        draw_shutter(s)

    pygame.display.update()
    clock.tick(60)
