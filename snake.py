import pygame

pygame.init()

#window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("~Snake~")

FPS = 20
clock = pygame.time.Clock()

SNAKE_SIZE = 20

head_x = WINDOW_WIDTH//2
head_y = WINDOW_HEIGHT//2 + 100

snake_dx = 0
snake_dy = 0

score = 0

GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
RED = (150, 0, 0)
WHITE = (255, 255, 255)

font = pygame.font.SysFont('gabriola', 48)

title_text = font.render("~Snake~", True, GREEN, DARKRED)
title_react = title_text.get_rect()
title_react.center = d(WINDOW//2, WINDOW_HEIGHT//2)

score_text = font.render("Score: " + str(score), True, GREEN, DARKRED)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

game_over_text = font.render("GAMEOVER", True, GREEN, DARKRED)
game_over_rect = game_over_text.get_react()
game_over_react.center = (WINDOW_WIDHT//2, WINDOW_HIGHT//2)

continue_text = font.render("Press any key to play again", True, RED, DARKGREEN)
continue.rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 64)

pick_up_sound = pygame.mixer.Sound("pick_up_sound.wav")

#set image rectangles
apple_coord = (500, 500, SNAKE_SIZE, SNAKE_SIZE)
apple_rect = pygame.draw.rect(display_surface, RED, apple_coord)
head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
head_rect = pygame.draw.rect(display_surface, RED, head_coord)
body_coords = []

#main loop
running = True
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#end
pygame.quit()
