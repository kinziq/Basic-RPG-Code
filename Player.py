import pygame
import sys
#custom object for copys of walls        
class Character(pygame.sprite.Sprite):
    
    def __init__(self, startX,startY,width,height,path_images):
        super().__init__()
        plr_load= pygame.image.load('images/imgoated.png')
        self.image = pygame.transform.scale(plr_load, (width,height)).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(startX,startY))
    
    def move(self,speed):
        plrinput = pygame.key.get_pressed()
        
        self.movex = (plrinput[pygame.K_a] * -speed) + (plrinput[pygame.K_d] * speed)
        self.movey = (plrinput[pygame.K_w] * -speed) + (plrinput[pygame.K_s] * speed)
        
        self.rect.x+=self.movex
        self.rect.y+=self.movey
            
    def plr_check_hit(self,group):
        if pygame.sprite.spritecollide(self, group, False, collided=pygame.sprite.collide_mask):
            return True
        else:
            return
    
    def plr_collide(self):
        self.rect.x -= self.movex
