#!/usr/bin/python3
# Imports the three python packages.
import pygame
import time
import random

# Calls the init() function.
pygame.init()

# Set the width and height of the game frame.
dis_width = 600
dis_height = 600

# Display the interface with the setted size of width and height.
dis = pygame.display.set_mode((dis_width, dis_height))

# Sets the caption name of the game screen.
pygame.display.set_caption('Snake Game by Daniel')

# Define the colors which is used for the interface.
teal = (0, 128, 128)
red = (255, 0, 0)
yellow = (255, 255, 102)
white = (255,255,255)

# Call the pygame Clock function.
clock = pygame.time.Clock()

# Set snake block to 20 and snake speed to 10.
snake_block = 20
snake_speed = 10

# Define the font and score style.
font_style = pygame.font.SysFont("bahnschrift", 30)
score_font = pygame.font.SysFont("comicsansms", 35)

# Implements the pause functionality of the game.
def pause():
    paused = True

    # While the pause do quit() or paused() or continue() to play game.
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()           

# Implemens the score of the game
def our_score(score):
    value = score_font.render("Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

# Draws the snake that eats food.
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, white, [x[0], x[1], snake_block, snake_block])

# Implements the message function with msg and color parameter.
def message(msg, color):
    msgs = font_style.render(msg, True, color)
    dis.blit(msgs, [dis_width/6, dis_height/3])

# Implements the game loop function in order to stay connected
# the game interface.
def gameLoop():
    game_over = False
    game_close = False

    # Sets the (x, y) cordination of the frame and the snake.
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    # Draws the foods of the snake to eat it with (x, y) coordinate.
    foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0
    
    # If game close is true, send message for action.
    while not game_over:
        while game_close == True:
            dis.fill(teal)
            
            # Messages for action to continue or quit.
            message("Game Over! Press Q-Quit/C-Play/P-Pause Again", red)
            
            pygame.display.update()

            # Used to continue or quit the game.
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Used to move the snake with keyboard shortcut.
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
                elif event.key == pygame.K_p:
                    pause()
                        
        # Used to notify when the game is crashed with the frame.
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change # Sets the x coordination.
        y1 += y1_change # Sets the y coordination.
        dis.fill(teal)  # Fills the color with teal color.

        # Draws the snake with the append mode when it eats his food to grow.
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        
        # Delete the snake list of 0 if it greater than the snake length
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        
        # Game over when the snake eats itself
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        
        # Call to draw snake
        our_snake(snake_block, snake_List)

        # Calls to count the score of the game.
        our_score(Length_of_snake - 1)

        # Updates the frame for new action.
        pygame.display.update()
        
        # Test to know whether snake reach at food or not.
        # And then take it as food.
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0
            # Increase the snake by one food block.
            Length_of_snake += 1

        # Set the clock with the snake speed.
        clock.tick(snake_speed)

    # Call to exit from the frame.
    pygame.quit()
    quit()

# Calls the function to not exit but continue to play until
# exit from the game.
gameLoop()
