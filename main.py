import pygame
from pygame.constants import MOUSEBUTTONDOWN, SCRAP_SELECTION

pygame.init()
pygame.display.init()
pygame.font.init()

display = pygame.display.set_mode((800,400))
clock = pygame.time.Clock()
pygame.display.set_caption("ElfTheif")
present = pygame.image.load("./_sprites/logo.png")
pygame.display.set_icon(present)
plrX = 0
plrY = 0
presents = 0
start_button = pygame.image.load("./_sprites/start button.png")
jump = pygame.mixer.Sound("./_sounds/jump.wav")
space_pressed = False
font = pygame.font.SysFont("ALIEE13", 30)
class player:
    def __init__(self):
        self.image = pygame.image.load()
class StartButton:
    def __init__(self):
        self.rect = pygame.draw.rect(display, (186, 201, 219), (368, 184, 32, 16), 0)

game_loop = False
menu_loop = True

while menu_loop:
    display.fill((186,201,219))
    Button = StartButton()
    display.blit(start_button, (368,184))
    text=font.render("ElfTheif", True, (0,0,0))
    display.blit(text,(300, 170))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
            menu_loop = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Button.rect.collidepoint(pygame.mouse.get_pos()):
                menu_loop = False
                game_loop = True
    pygame.display.update()

while game_loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.mixer.Sound.play(jump)
    display.fill((186, 201, 219))
    display.blit(present, (10,10))
    text = font.render(str(presents), False, (0,0,0))
    display.blit(text, (28,10))
    pygame.display.update()
    

pygame.quit()
quit()