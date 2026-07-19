import pygame
import math
import sys

pygame.init()

# -----------------------------
# WINDOW & COLORS
# -----------------------------
WIDTH, HEIGHT = 1000, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RAIED Dome - 3D Engineering Isometric")

BLACK = (0, 0, 0)
GRAY = (180, 180, 180)
ORANGE = (255, 140, 0)
BLUE = (0, 150, 255)
WHITE = (230, 230, 230)

font = pygame.font.SysFont(None, 30)

# -----------------------------
# 3D PROJECTION SETTINGS
# -----------------------------
CENTER_X = WIDTH // 2
GROUND_Y = HEIGHT - 120

TANK_RADIUS = 140
SHUTTER_LENGTH = 160
SHUTTER_WIDTH = 30
NUM_SHUTTERS = 8
DEPLOY_SPEED = 4

FRAME_RADIUS = 260
MAX_HEIGHT = 180  # how high shutters rise in 3D

# -----------------------------
# SHUTTERS INITIALIZATION
# -----------------------------
shutters = []
for i in range(NUM_SHUTTERS):
    angle = math.radians(i * (360 / NUM_SHUTTERS))
    shutters.append({
        "angle": angle,
        "progress": 0,   # inward slide
        "height": 0,     # upward rise
        "tilt": 0        # inward tilt
    })

deploying = False
retracting = False

# -----------------------------
# 3D PROJECTION FUNCTION
# -----------------------------
def project_point(x, y, z):
    """
    Converts 3D coordinates (x, y, z) into 2D screen coordinates.
    Simple isometric projection.
    """
    iso_x = CENTER_X + x - y
    iso_y = GROUND_Y - z - (x + y) * 0.3
    return int(iso_x), int(iso_y)

# -----------------------------
# DRAW TANK (3D CYLINDER)
# -----------------------------
def draw_tank():
    # Top ellipse
    top_points = []
    for i in range(40):
        ang = math.radians(i * 9)
        x = TANK_RADIUS * math.cos(ang)
        y = TANK_RADIUS * math.sin(ang)
        px, py = project_point(x, y, 0)
        top_points.append((px, py))

    pygame.draw.polygon(WIN, GRAY, top_points)

    # Side walls
    for i in range(40):
        ang = math.radians(i * 9)
        x = TANK_RADIUS * math.cos(ang)
        y = TANK_RADIUS * math.sin(ang)
        px1, py1 = project_point(x, y, 0)
        px2, py2 = project_point(x, y, -80)
        pygame.draw.line(WIN, GRAY, (px1, py1), (px2, py2), 2)

# -----------------------------
# DRAW SHUTTERS IN 3D
# -----------------------------
def draw_shutter(s):
    angle = s["angle"]
    progress = s["progress"]
    height = s["height"]
    tilt = s["tilt"]

    # Radial direction
    dx = math.cos(angle)
    dy = math.sin(angle)

    # Base position on frame
    base_x = dx * FRAME_RADIUS
    base_y = dy * FRAME_RADIUS

    # Slide inward
    inner_x = base_x - dx * progress
    inner_y = base_y - dy * progress

    # Shutter endpoints in 3D
    # Back edge (farther from center)
    x1 = inner_x
    y1 = inner_y
    z1 = height

    # Front edge (tilted inward)
    x2 = inner_x - dx * SHUTTER_LENGTH * math.cos(tilt)
    y2 = inner_y - dy * SHUTTER_LENGTH * math.cos(tilt)
    z2 = height + SHUTTER_LENGTH * math.sin(tilt)

    # Project to 2D
    p1 = project_point(x1, y1, z1)
    p2 = project_point(x2, y2, z2)

    pygame.draw.line(WIN, ORANGE, p1, p2, SHUTTER_WIDTH)

# -----------------------------
# MAIN LOOP
# -----------------------------
clock = pygame.time.Clock()

while True:
    WIN.fill(BLACK)

    # UI
    text = font.render("SPACE: Deploy   R: Retract   ESC: Quit", True, BLUE)
    WIN.blit(text, (20, 20))

    # Draw tank
    draw_tank()

    # Draw shutters
    for s in shutters:
        draw_shutter(s)

    # Animation logic
    for s in shutters:
        if deploying:
            if s["progress"] < FRAME_RADIUS:
                s["progress"] += DEPLOY_SPEED
            if s["height"] < MAX_HEIGHT:
                s["height"] += DEPLOY_SPEED * 0.7
            if s["tilt"] < math.radians(55):
                s["tilt"] += 0.02

        if retracting:
            if s["progress"] > 0:
                s["progress"] -= DEPLOY_SPEED
            if s["height"] > 0:
                s["height"] -= DEPLOY_SPEED * 0.7
            if s["tilt"] > 0:
                s["tilt"] -= 0.02

    # Events
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

    pygame.display.update()
    clock.tick(60)
