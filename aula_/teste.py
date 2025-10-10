import pygame
import sys

pygame.init()

w = 800
h = 600

screen = pygame.display.set_mode((w,h))
pygame.display.set_caption('ping e pong')

ball_x = 400 //2
ball_y = 300 //2

BV_X = 5
BV_Y = 5

largura_vareta = 20
altura_vareta = 150

white = 'white'
green = 'green'
black = 'black'

def draw_shapes():
    screen.fill('white')

    pygame.draw.rect(screen, )

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        pygame.display.flip()