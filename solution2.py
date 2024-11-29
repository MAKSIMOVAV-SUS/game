import pygame # подключаем библиотеку
import sys # подключаем модуль для 
import time
from random import *

pygame.init()

WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player = pygame.Rect(400, 400, 50, 50)
player_img_orig = pygame.image.load('png-transparent-warcraft-thrall-character-art-heroes-of-the-storm-world-of-warcraft-battle-for-azeroth-the-lost-vikings-thrall-world-of-warcraft-game-fictional-characters-video-game.png')
player_img = pygame.transform.scale(player_img_orig, (player.width, player.height))
enemy = pygame.Rect(50, 50, 50, 50)
enemy_img_orig = pygame.image.load('a07705b9eda933dd7d4037fd72b3926a.png')
enemy_img = pygame.transform.scale(enemy_img_orig, (enemy.width, enemy.height))
enemy2 = pygame.Rect(150, 200, 70, 70)
enemy2_img_orig = pygame.image.load('a07705b9eda933dd7d4037fd72b3926a.png')
enemy2_img = pygame.transform.scale(enemy2_img_orig, (enemy2.width, enemy2.height))


direction = 'none'

while True:
    screen.fill((255, 255, 255))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RIGHT:
                direction = 'right'
            elif e.key == pygame.K_LEFT:
                direction = 'left'
            elif e.key == pygame.K_UP:
                direction = 'up'
            elif e.key == pygame.K_DOWN:
                direction = 'down'
        if e.type == pygame.KEYUP:
            direction = 'none'

    if direction == 'right':
        player.x += 5
    elif direction == 'left':
        player.x -= 5
    elif direction == 'up':
        player.y -= 5
    elif direction == 'down':
        player.y += 5


    if player.colliderect(enemy):
        enemy.x = randint(0, 550)
        enemy.y = randint(0, 550)
        player.width += 5
        player.height += 5
        player_img = pygame.transform.scale(player_img_orig, (player.width, player.height))
    if player.width == 500 and player.height == 500:
       enemy.x = (10000)
       enemy.y = (10000)
    if player.colliderect(enemy2):
        enemy2.x = randint(0, 550)
        enemy2.y = randint(0, 550)
        player.width += 5
        player.height += 5
        player_img = pygame.transform.scale(player_img_orig, (player.width, player.height))
    if player.width == 500 and player.height == 500:
       enemy2.x = (10000)
       enemy2.y = (10000)


    screen.blit(player_img, player)
    screen.blit(enemy_img, enemy)
    pygame.display.update()
    clock.tick(60)
    

