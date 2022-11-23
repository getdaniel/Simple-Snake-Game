#!/usr/bin/python3
import pygame
import time

pygame.init()

dis_width = 600
dis_height = 600

dis=pygame.display.set_mode((dis_width, dis_height))

pygame.display.set_caption('Snake Game by Daniel')

game_over = False

black = (0, 0, 0)
red = (255, 0, 0)
white = (255,  255, 255)
blue = (0, 0, 255)

clock = pygame.time.Clock()

snake_block = 20
snake_speed = 30

font_style = pygame.font.SysFont(None, 30)

def message(msg, color):
    msgs = font_style.render(msg, True, color)
    dis.blit(msgs, [dis_width/3, dis_height/3])

def gameLoop():
    game_over = False

    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0

    foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0

while not game_over:
    while game_close == True:
        dis_fill(white)
        message("You Lost! Press Q-Quit or C-Play Again", red)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_over = True
                    game_close = False
                if event.key == pygame.K_c:
                     gameLoop()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -snake_block
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = snake_block
    
    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        game_over = True

    x1 += x1_change
    y1 += y1_change
    dis.fill(white)
    pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
    pygame.display.update()
    clock.tick(snake_speed)

message("You Lost!!!", red)
pygame.display.update()
time.sleep(5)

pygame.quit()
quit()
