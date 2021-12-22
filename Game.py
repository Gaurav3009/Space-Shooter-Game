import pygame
import random
import math
import numpy as np
from pygame import mixer


# Initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load("bg.png")

# Background Sound
mixer.music.load("DeathMatch.ogg")
mixer.music.play(-1)

# Title and the Icon of the game
pygame.display.set_caption("Space Shooter")
icon = pygame.image.load("ufoBlue.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("player.png")
X = 370
Y = 480
player_speed = 0
player_life = 3
clock = pygame.time.Clock()

# Enemy
enemyImg = []
enemyX = []
enemyY = []
num_of_enemies = 3
enemy_speed = 1

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("alien.png"))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(0, 20))

# Bullets
bullets = pygame.image.load("bullet_pl.png")
bulletX = 0
bulletY = 480
bullet_state = "ready"
bullet_x_change = 0
bullet_y_change = 8

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 0, 0))
    screen.blit(score, (x, y))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullets, (x+18.8, y-5))


def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt(math.pow((enemy_x - bullet_x), 2) + math.pow((enemy_y - bullet_y), 2))
    if distance < 27:
        return True
    else:
        return False


# Game Loop
def run_game():
    global playerImg
    global player_speed
    global bulletX
    global bulletY
    global score_value
    global bullet_state
    global X, Y
    global enemyX, enemyY
    global player_life
    left_move = False
    right_move = False
    blast = False
    action = True

    running = True
    while running:
        # RGB value
        screen.fill((0, 0, 0))
        # Background Image
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Left and Right movement of the player
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player_speed = 4
                if event.key == pygame.K_LEFT:
                    player_speed = -4
                if event.key == pygame.K_SPACE:
                    bullet_state = "fire"
                    bulletX = X
                    bulletY = Y

            if event.type == pygame.KEYUP:
                player_speed = 0

        # For updating the changes made
        X = X + player_speed
        # Setting Boundaries in our game window
        if X <= 0:
            X = 0
        elif X >= 736:
            X = 736
        player(X, Y)
        # Enemy Movement
        for i in range(num_of_enemies):
            enemyY[i] = enemyY[i] + enemy_speed
            if enemyY[i] >= 600:
                enemyX[i] = random.randint(0, 736)
                enemyY[i] = random.randint(0, 50)
                score_value -= 1

            enemy(enemyX[i], enemyY[i], i)

            # Collision
            collision = is_collision(enemyX[i], enemyY[i], bulletX, bulletY )
            if collision:
                bulletY = 480
                bullet_state = "ready"
                score_value += 1
                print(score_value)
                enemyX[i] = random.randint(0, 736)
                enemyY[i] = random.randint(0, 50)

        # BulletMovement
        if bulletY <= 0:
            bullet_state = "ready"
            bulletX = 0
            bulletY = 480
        if bullet_state is "fire":
            bullet(bulletX, bulletY)
            bulletY -= bullet_y_change
        show_score(textX, textY)
        pygame.display.update()
        clock.tick(90)


run_game()
'''************************************************************THANK YOU***********************************************************************************'''