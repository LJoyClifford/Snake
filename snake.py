import pygame

pygame.init()

#window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("~Snake~")

#main loop
running = True
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#end
pygame.quit()
