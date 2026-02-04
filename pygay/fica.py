import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Test Pymunk - Fisica")
clock = pygame.time.Clock()

# Posizione e proprietà del cerchio
circle_x = 400
circle_y = 300
circle_radius = 30
circle_speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill((30, 30, 50))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()