import pygame
from pygame.constants import MOUSEBUTTONDOWN, SCRAP_SELECTION, K_a, K_d
from pygame.time import Clock, delay

pygame.init()
pygame.display.init()
pygame.font.init()

FPSLOCK = 60
display = pygame.display.set_mode((800,400))
clock = pygame.time.Clock()
pygame.display.set_caption("SantaStealer")
present = pygame.image.load("./_sprites/logo.png")
pygame.display.set_icon(present)
plrX = 100
plrY = 100
level = 1
velocity = 3
presents = 0
start_button = pygame.image.load("./_sprites/start button.png")
jump = pygame.mixer.Sound("./_sounds/jump.wav")
space_pressed = False
font = pygame.font.SysFont("ALIEE13", 30)
plrimage = pygame.image.load("./_sprites/player.png")
current_collide = False
class StartButton:
    def __init__(self):
        self.rect = pygame.draw.rect(display, (186, 201, 219), (368, 184, 32, 16), 0)
class PRESENT:
    def __init__(self,x,y):
        self.rect = pygame.draw.rect(display, (186, 201, 219), (x,y,16,16))
game_loop = False
menu_loop = True
def updateLevel():
    if level == 1:
        #build level

        print()
while menu_loop:
    display.fill((186,201,219))
    Button = StartButton()
    display.blit(start_button, (368,184))
    text=font.render("SantaStealer", True, (0,0,0))
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
    clock.tick(FPSLOCK)

while game_loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.mixer.Sound.play(jump)
                velocity = -3
                plrY -= 4
                current_collide = False
    keysDown = pygame.key.get_pressed()
    if keysDown[K_a]:
        plrX -= 1
    if keysDown[K_d]:
        plrX += 1
    display.fill((186, 201, 219))
    display.blit(present, (10,10))
    text = font.render(str(presents), False, (0,0,0))
    display.blit(text, (28,10))
    class Floor:
        def __init__(self):
            self.rect = pygame.draw.rect(display, (255,0,0), (0, 380, 800, 20))
    FloorOBJ = Floor()
    class player:
        def __init__(self):
            self.rect = pygame.draw.rect(display, (186,201,219), (plrX, plrY, 16, 16), 0)
    plrOBJ = player()
    if FloorOBJ.rect.colliderect(plrOBJ.rect) and current_collide == False:
        current_collide = True
        velocity = 0
    if velocity < 3 and current_collide == False:
        velocity += 0.1

    plrY += velocity
    display.blit(plrimage, (plrX, plrY))
    #print("X: "+str(plrX)+", Y: "+str(plrY))
    pygame.display.update()
    clock.tick(FPSLOCK)
    

pygame.quit()
quit()