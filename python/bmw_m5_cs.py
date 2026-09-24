import pygame
import math

pygame.init()

WIDTH, HEIGHT = 1200, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Realistic Sports Sedan")

clock = pygame.time.Clock()

# Colors
BLACK = (10, 10, 12)
ROAD = (35, 35, 38)
WHITE = (245, 245, 245)
SILVER = (170, 175, 180)
DARK = (20, 22, 25)
RED = (120, 0, 0)
BLUE = (25, 80, 120)
LIGHT = (210, 230, 255)
YELLOW = (255, 220, 120)


def ellipse(x, y, w, h, color):
    pygame.draw.ellipse(screen, color, (x, y, w, h))


def polygon(points, color):
    pygame.draw.polygon(screen, color, points)


# ------------------------------------------------
# MAIN CAR BODY
# ------------------------------------------------

# Shadow
ellipse(170, 530, 850, 80, (10, 10, 10))

# Main body
body = [
    (130, 480),
    (155, 420),
    (220, 390),
    (300, 375),
    (390, 285),
    (470, 245),
    (680, 245),
    (775, 290),
    (850, 365),
    (1010, 395),
    (1060, 445),
    (1050, 500),
    (990, 520),
    (190, 520)
]

polygon(body, (55, 58, 62))

# Lower body
lower_body = [
    (135, 470),
    (220, 460),
    (350, 475),
    (520, 480),
    (700, 470),
    (850, 460),
    (1030, 450),
    (1050, 500),
    (990, 520),
    (190, 520)
]

polygon(lower_body, (35, 37, 40))


# ------------------------------------------------
# ROOF
# ------------------------------------------------

roof = [
    (300, 375),
    (390, 285),
    (470, 245),
    (680, 245),
    (775, 290),
    (850, 365)
]

polygon(roof, (45, 47, 50))


# ------------------------------------------------
# WINDOWS
# ------------------------------------------------

# Front window
front_window = [
    (485, 265),
    (665, 265),
    (750, 300),
    (800, 350),
    (670, 350)
]

polygon(front_window, (20, 32, 40))

# Rear window
rear_window = [
    (470, 265),
    (395, 300),
    (340, 355),
    (465, 350)
]

polygon(rear_window, (18, 30, 38))

# Window reflections
polygon([
    (500, 270),
    (545, 270),
    (495, 340),
    (460, 340)
], (65, 90, 105))

polygon([
    (685, 270),
    (720, 300),
    (755, 340),
    (720, 340)
], (60, 85, 100))


# ------------------------------------------------
# WINDOW DIVIDER
# ------------------------------------------------

pygame.draw.line(
    screen,
    (5, 5, 5),
    (470, 260),
    (465, 355),
    7
)


# ------------------------------------------------
# FRONT GRILLE
# ------------------------------------------------

# Kidney-style grille
pygame.draw.ellipse(
    screen,
    (5, 5, 6),
    (940, 410, 45, 65)
)

pygame.draw.ellipse(
    screen,
    (5, 5, 6),
    (985, 410, 45, 65)
)

# Grille highlights
pygame.draw.arc(
    screen,
    (100, 100, 100),
    (940, 410, 45, 65),
    0,
    math.pi,
    2
)

pygame.draw.arc(
    screen,
    (100, 100, 100),
    (985, 410, 45, 65),
    0,
    math.pi,
    2
)


# ------------------------------------------------
# HEADLIGHTS
# ------------------------------------------------

# Headlight housing
polygon([
    (850, 375),
    (940, 385),
    (970, 415),
    (875, 410)
], (30, 35, 40))

# Headlight
polygon([
    (865, 382),
    (930, 390),
    (950, 408),
    (880, 405)
], LIGHT)

# LED strips
pygame.draw.line(
    screen,
    WHITE,
    (880, 390),
    (930, 400),
    4
)


# ------------------------------------------------
# TAIL LIGHT
# ------------------------------------------------

polygon([
    (145, 400),
    (220, 400),
    (205, 430),
    (145, 440)
], (80, 10, 12))

pygame.draw.line(
    screen,
    RED,
    (155, 410),
    (205, 415),
    5
)


# ------------------------------------------------
# FRONT BUMPER
# ------------------------------------------------

polygon([
    (980, 450),
    (1060, 445),
    (1050, 500),
    (995, 510)
], (25, 26, 28))

# Air intake
polygon([
    (990, 465),
    (1040, 460),
    (1035, 485),
    (995, 490)
], BLACK)


# ------------------------------------------------
# DOORS
# ------------------------------------------------

pygame.draw.line(
    screen,
    (15, 15, 15),
    (465, 355),
    (465, 470),
    3
)

pygame.draw.line(
    screen,
    (15, 15, 15),
    (680, 350),
    (680, 470),
    3
)

# Door handles
pygame.draw.rect(
    screen,
    (100, 100, 105),
    (510, 370, 35, 5)
)

pygame.draw.rect(
    screen,
    (100, 100, 105),
    (720, 370, 35, 5)
)


# ------------------------------------------------
# SIDE SKIRT
# ------------------------------------------------

polygon([
    (300, 470),
    (820, 470),
    (850, 500),
    (270, 500)
], (25, 27, 30))


# ------------------------------------------------
# WHEELS
# ------------------------------------------------

def draw_wheel(cx, cy):

    # Tire
    pygame.draw.circle(
        screen,
        (5, 5, 6),
        (cx, cy),
        75
    )

    # Tire highlight
    pygame.draw.circle(
        screen,
        (45, 45, 48),
        (cx, cy),
        60,
        5
    )

    # Rim
    pygame.draw.circle(
        screen,
        (145, 148, 152),
        (cx, cy),
        48
    )

    # Rim center
    pygame.draw.circle(
        screen,
        (35, 35, 38),
        (cx, cy),
        15
    )

    # Spokes
    for angle in range(0, 360, 45):

        rad = math.radians(angle)

        x1 = cx + math.cos(rad) * 12
        y1 = cy + math.sin(rad) * 12

        x2 = cx + math.cos(rad) * 43
        y2 = cy + math.sin(rad) * 43

        pygame.draw.line(
            screen,
            (60, 62, 65),
            (x1, y1),
            (x2, y2),
            5
        )

    # Center cap
    pygame.draw.circle(
        screen,
        (20, 20, 22),
        (cx, cy),
        9
    )


draw_wheel(300, 485)
draw_wheel(870, 485)


# ------------------------------------------------
# MIRROR
# ------------------------------------------------

ellipse(805, 335, 45, 20, (20, 22, 25))


# ------------------------------------------------
# SIDE BODY REFLECTION
# ------------------------------------------------

pygame.draw.line(
    screen,
    (120, 123, 128),
    (240, 420),
    (850, 420),
    3
)

pygame.draw.line(
    screen,
    (75, 78, 82),
    (350, 440),
    (900, 440),
    2
)


# ------------------------------------------------
# M5 CS STYLE BADGE
# ------------------------------------------------

font = pygame.font.SysFont("Arial", 22, True)

badge = font.render(
    "M5 CS",
    True,
    WHITE
)

screen.blit(
    badge,
    (760, 425)
)


# ------------------------------------------------
# ROAD
# ------------------------------------------------

pygame.draw.rect(
    screen,
    ROAD,
    (0, 555, WIDTH, 145)
)

# Road line
pygame.draw.line(
    screen,
    (180, 180, 180),
    (0, 620),
    (1200, 620),
    3
)


# ------------------------------------------------
# TITLE
# ------------------------------------------------

title_font = pygame.font.SysFont(
    "Arial",
    35,
    True
)

title = title_font.render(
    "BMW M5 CS",
    True,
    WHITE
)

screen.blit(
    title,
    (470, 80)
)


# ------------------------------------------------
# MAIN LOOP
# ------------------------------------------------

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(60)


pygame.quit()