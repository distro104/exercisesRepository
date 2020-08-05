'''
This game   have   the objective  that  to learn the basic
contents about Pygame.
'''

import pygame, random       # Import the libliry pygame and random
from pygame.locals import * # used in this project

# screen size:
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

# Keyboard variable
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# Speed in game
clock_time = 5

#Function that return a random position X,Y
def on_grid_random():
    x = random.randint(0,SCREEN_WIDTH)
    y = random.randint(0,SCREEN_HEIGHT)
    return (x // 10 * 10, y // 10 * 10)

def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1]) #Body of the snake



pygame.init() #All softwares taht are use pygame need this comand
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.display.set_caption('Snake Game')


snake = [(200, 200), (210, 200), (220, 200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((255,255,255))

apple_pos = on_grid_random()
apple  = pygame.Surface((10,10))
apple.fill((255,0,0))

my_direction = LEFT

clock = pygame.time.Clock()

while True:  # Main Loop
    clock.tick(clock_time)
    for event in pygame.event.get(): #Get events in game
        if event.type == QUIT: # When close the program quit
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_LEFT:
                my_direction = LEFT
            if event.key == K_RIGHT:
                my_direction = RIGHT

    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0,0))

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    screen.fill((0,0,0))
    screen.blit(apple, apple_pos)
    for pos in snake:
        screen.blit(snake_skin,pos)

    pygame.display.update() # Refresh elements in the screeen
