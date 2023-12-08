#Name: Kinz
#Date: 12/7/23
#Basic Basic Movement and Stamina Code
import pygame,sys
from Player import Character
from Stamina import Stamina_Bar
from background_testing import GIF

pygame.init()

# Game Setup
fps = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500


PLAYER_LOCATION_X=250
PLAYER_LOCATION_Y=50

#Setup of Starting objects

window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pygame.HWSURFACE)
pygame.display.set_caption("Title")

playersprite=Character(PLAYER_LOCATION_X,PLAYER_LOCATION_Y,30,30,'images/imgoated.png')
StaminaBar = Stamina_Bar(20,400,100,50, 'images/stamina_bar.png')


background = GIF(0,0,WINDOW_WIDTH,WINDOW_HEIGHT, 'images/grass_waving.gif')

Player = pygame.sprite.GroupSingle()
Player.add(playersprite)

Stamina = pygame.sprite.GroupSingle()
Stamina.add(StaminaBar)


def display():
    window.fill((255,255,255)) #White background
    background.draw(window)
    Player.draw(window)
    #Stamina.draw(window)

    #Player=pygame.draw.rect(window,(0,0,0),(250,50,50,50))
   

while True:
    display()   
    key_input = pygame.key.get_pressed()
    if key_input[pygame.K_LSHIFT]:
        
        playersprite.move(5)
        Stamina.draw(window)
    else:
        playersprite.move(3)
    for event in pygame.event.get():
        
      # if user  QUIT then the screen will close
          if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
  
    background.update(60)
    pygame.display.update() #update the display
    fpsClock.tick(fps) #speed of redraw
