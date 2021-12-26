import pygame
from pygame.constants import MOUSEBUTTONDOWN, SCRAP_SELECTION, K_a, K_d
from pygame.display import update

from pygame.time import Clock, delay
pygame.init()
pygame.display.init()
pygame.font.init()
FPSLOCK = 60
display = pygame.display.set_mode((800,400))
clock = pygame.time.Clock()
pygame.display.set_caption("SantaStealer")
presentIMG = pygame.image.load("./_sprites/logo.png")
pygame.display.set_icon(presentIMG)
plrX = 100
plrY = 100
level = 1
velocity = 3
presents = 0
start_button = pygame.image.load("./_sprites/start button.png")
floorimg = pygame.image.load("./_sprites/floor.png")
backgroundIMG = pygame.image.load("./_sprites/sky_backrop_with_snow.png")
jump = pygame.mixer.Sound("./_sounds/jump.wav")
select = pygame.mixer.Sound("./_sounds/select_button.wav")
deselect = pygame.mixer.Sound("./_sounds/deselect_button.wav")
collect = pygame.mixer.Sound("./_sounds/collect.wav")
space_pressed = False
font = pygame.font.SysFont("Alien Encounters", 23)
titleFont = pygame.font.SysFont("Almonte Snow", 60)
plrimage = pygame.image.load("./_sprites/player.png")
current_collide = False
class StartButton:
    def __init__(self):
        self.rect = pygame.draw.rect(display, (186, 201, 219), (352, 184, 64, 32), 0)
game_loop = False
menu_loop = True
winloop = False
hovering_over_play = False
drawA = True
drawB = True
while menu_loop:
    display.fill((186,201,219))
    display.blit(backgroundIMG,(0,0))
    Button = StartButton()
    display.blit(pygame.transform.scale(start_button, (64,32)), (352,184))
    text=titleFont.render("SantaStealer", True, (0,0,0))
    textrect=text.get_rect(center=(800//2, 100))
    display.blit(text,textrect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
            menu_loop = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Button.rect.collidepoint(pygame.mouse.get_pos()):
                menu_loop = False
                game_loop = True
    if Button.rect.collidepoint(pygame.mouse.get_pos()) and not hovering_over_play:
        pygame.mixer.Sound.play(select)
        hovering_over_play = True
    if not Button.rect.collidepoint(pygame.mouse.get_pos()) and hovering_over_play:
        pygame.mixer.Sound.play(deselect)
        hovering_over_play = False
    pygame.display.update()
    clock.tick(FPSLOCK)
while game_loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and plrY > 30:
                pygame.mixer.Sound.play(jump)
                velocity = -3
                plrY -= 4
                current_collide = False
    keysDown = pygame.key.get_pressed()
    if keysDown[K_a] and plrX > 0:
        plrX -= 1
    if keysDown[K_d] and plrX < 784:
        plrX += 1
    display.fill((186, 201, 219))
    display.blit(backgroundIMG,(0,0))
    display.blit(presentIMG, (10,10))
    text = font.render(str(presents), False, (0,0,0))
    display.blit(text, (28,10))
    class Floor:
        def __init__(self):
            self.rect = pygame.draw.rect(display, (186,201,219), (0, 380, 800, 20))
    FloorOBJ = Floor()
    class player:
        def __init__(self):
            new_surf = pygame.Surface((800,600), pygame.SRCALPHA)
            self.rect = pygame.draw.rect(new_surf, (186,201,219), (plrX, plrY, 16, 16), 0)
    plrOBJ = player()
    class PRESENT:
        def __init__(self,x,y):
            self.rect = pygame.draw.rect(display, (186, 201, 219), (x,y,16,16))
    if FloorOBJ.rect.colliderect(plrOBJ.rect) and current_collide == False:
        current_collide = True
        velocity = 0
    if velocity < 3 and current_collide == False:
        velocity += 0.1
    display.blit(floorimg, (0, 380))
    presentA = PRESENT(16,364)
    if drawA:
        display.blit(presentIMG, (16, 364))
    presentB = PRESENT(764,364)
    if drawB:
        display.blit(presentIMG, (764, 364))
    if presentA.rect.colliderect(plrOBJ.rect) and drawA:
        drawA = False
        presents+=1
    if presentB.rect.colliderect(plrOBJ.rect) and drawB:
        drawB = False
        presents+=1
    plrY += velocity
    display.blit(plrimage, (plrX, plrY))
    pygame.display.update()
    clock.tick(FPSLOCK)
    if drawA == False and drawB == False:
        winloop = True
        game_loop = False
while winloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            winloop = False
    display.fill((186, 201, 219))
    display.blit(backgroundIMG,(0,0))
    textA = font.render("You Won!", False, (0,0,0))
    textrect=textA.get_rect(center=(800//2, 100))
    display.blit(textA,textrect)
    textB = font.render("Scripts by: yodahe#2639", False, (0,0,0))
    textrect=textB.get_rect(center=(800//2, 200))
    display.blit(textB,textrect)
    textC = font.render("Backdrop by: RT Crazy_M#9514", False, (0,0,0))
    textrect=textC.get_rect(center=(800//2, 300))
    display.blit(textC,textrect)
    pygame.display.update()
pygame.quit()
quit()