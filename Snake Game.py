# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 23:49:11 2020

@author: BHAVISHYA
"""

import pygame
import random

pygame.init()

clock= pygame.time.Clock()

orange=(255,123,7)
black = (0,0,0)
pink = (213, 50, 80)
red = (255,0, 0)
green = (0, 255, 0)
blue = (50, 153, 213)
white = (255, 255, 255)

display_width = 600
display_height = 400
dis = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Snake Game")
snake_block = 10
snake_speed=15
snake_list = []

def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, white, [x[0],x[1], 9, 9])
        

def snakegame():
    game_over = False
    game_end = False
    x1 = display_width/2
    y1 = display_height/2
    x1_change = 0
    y1_change = 0
    lastkey="none"
    
    snake_list = []
    Length_of_snake = 1
        
    foodx = round(random.randrange(0,display_width - snake_block)/ 10.0) * 10.0
    foody = round(random.randrange(0, display_height - snake_block)/10.0) * 10.0
        
    while not game_over:
        while game_end == True:
            dis.fill(blue)
            font_style = pygame.font.SysFont("comicsansms",25)
            mesg= font_style.render("You Lost! Wanna play again? Press P", True, pink)
            dis.blit(mesg, [display_width/6, display_height/3])
            
            score = Length_of_snake - 1
            score_font = pygame.font.SysFont("comicsansms",35)
            value= score_font.render("Your Score: " + str(score), True, green)
            dis.blit(value, [display_width/3, display_height/5])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key== pygame.K_p:
                        snakegame()
                if event.type == pygame.QUIT:
                    game_over=True
                    game_end=False
        
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                game_over=True
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_LEFT and lastkey!="right"):
                    x1_change = -snake_block
                    y1_change = 0
                    lastkey="left"
                if (event.key == pygame.K_RIGHT and lastkey!="left"):
                    x1_change = snake_block
                    y1_change = 0
                    lastkey="right"
                if (event.key == pygame.K_UP and lastkey!="down"):
                    y1_change = -snake_block
                    x1_change = 0
                    lastkey="up"
                if (event.key == pygame.K_DOWN and lastkey!="up"):
                    y1_change = snake_block
                    x1_change = 0
                    lastkey="down"
        if x1 >=display_width or x1<0 or y1>=display_height or y1< 0:
            game_end = True
        x1 += x1_change
        y1 += y1_change
        
        dis.fill(black)
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_list.append(snake_Head)
        
        if len(snake_list)>Length_of_snake:
            del snake_list[0]
            
        for x in snake_list[:-1]:
            if x == snake_Head:
                game_end = True
        snake(snake_block, snake_list)
        pygame.display.update()
        
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0,display_width - snake_block)/ 10.0) * 10.0
            foody = round(random.randrange(0, display_height - snake_block)/10.0) * 10.0
            Length_of_snake += 1
        clock.tick(snake_speed)
    pygame.quit()
    quit()
snakegame()