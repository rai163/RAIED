import pygame
import math
import sys

pygame.init()

# -----------------------------
# WINDOW
# -----------------------------
WIDTH, HEIGHT = 1000, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RAIED - Real Tank Background")

ORANGE = (255, 140, 0)
BLUE = (0, 150, 255)
WHITE = (240, 240, 240)

font = pygame.font.SysFont(None, 28)

# -----------------------------
# LOAD TANK IMAGE
# -----------------------------
# Make sure "tank.png" is in the same folder
try:
    tank_img = pygame.image.load("tank.png").convert_alpha()
except pygame.error as e:
    print("Error loading tank.png:", e)
    pygame.quit()
    sys.exit()

# Scale image to fit nicely
img_ratio = tank_img.get_width() / tank_img.get_height()
target_height = 500
target_width = int(target_height * img_ratio)
tank_img = pygame.transform.smoothscale(tank_img, (target_width, target_height))

# Position image in the center
tank_x = (WIDTH - target_width) // 2
tank_y = (HEIGHT - target_height) // 2

# Approximate tank center and radius (relative to image)
# You can tweak these if needed
tank_center_x = WIDTH // 2
tank_center_y = tank_y + target_height // 2
tank_radius = target_height // 3  # approximate radius around the vessel

# -----------------------------
# SHUTTER PARAMETERS
# -----------------------------
NUM_SHUTTERS = 8
SHUTTER_LENGTH = 220
SHUTTER_WIDTH = 18

DEPLOY_SPEED = 4
MAX_OFFSET = 180  # how far up/out they move

shutters = []
for i in range(NUM_SHUTTERS):
    angle = math.radians(i * (360 / NUM_SHUTTERS))
    shutters.append({
        "angle": angle,
        "offset": 0  # 0 = retracted at tank edge, MAX_OFFSET = fully deployed
    })

deploying = False
retracting = False

# -----------------------------
# DRAW SHUTTERS
# -----------------------------
def draw_shutter(s):
    angle = s["angle"]
    offset = s["offset"]

    # Base point at tank edge
    base_x = tank_center_x + math.cos(angle) * tank_radius
    base_y = tank_center_y + math.sin(angle) * tank_radius

    # Move outward (deploy) along same angle
    base_x -= math.cos(angle) * offset
    base_y -= math.sin(angle) * offset

    # Shutter end point (further out)
    end_x = base_x + math.cos(angle) * SHUTTER_LENGTH
    end_y = base_y + math.sin(angle) * SHUTTER_LENGTH

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

    # Background: real tank image
    WIN.fill((0, 0, 0))
    WIN.blit(tank_img, (tank_x, tank_y))

    # UI text
    WIN.blit(font.render("SPACE: Deploy   R: Retract   ESC: Quit", True, BLUE), (20, 20))
    WIN.blit(font.render("RAIED: Shutters on REAL Tank Image", True, WHITE), (20, 50))

    # Update shutter states
    for s in shutters:
        if deploying:
            s["offset"] = min(s["offset"] + DEPLOY_SPEED, MAX_OFFSET)
        if retracting:
            s["offset"] = max(s["offset"] - DEPLOY_SPEED, 0)

    # Draw shutters on top of the real tank
    for s in shutters:
        draw_shutter(s)

    pygame.display.update()
    clock.tick(60)
