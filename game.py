import pygame
import sys
from scripts.entities import PhysicsEntity
from scripts.utils import load_image,load_images1
from scripts.tilemap import Tilemap

class game:
    def __init__(self):
    
        pygame.init() # Initializes pygame
        
        pygame.display.set_caption('Ninja Platformer')
        self.screen = pygame.display.set_mode((640,480)) #provides display screen
        self.clock = pygame.time.Clock()
        self.display = pygame.Surface((320,240))
        
        #okok
        
        
        self.movement = [False,False]
        
        self.assets = {
            'decor':load_images1('tiles/decor'),
            'grass':load_images1('tiles/grass'),
            'large_decor':load_images1('tiles/large_decor'),
            'stone':load_images1('tiles/stone'),
            'player':load_image('entities/player.png')
            }
        self.player = PhysicsEntity(self, 'player', (50,50), (8,15))#player render
        
        self.tilemap = Tilemap(self, tile_size=16)
        
    def run(self):
        while True:
            self.display.fill((14,219,248))     
            
            self.tilemap.render(self.display) 
            
            self.player.update((self.movement[1] - self.movement[0] ,0))
            self.player.render(self.display)
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.QUIT()
                    sys.exit()
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.movement[0] = True
                    if event.key == pygame.K_d:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.movement[0] = False
                    if event.key == pygame.K_d:
                        self.movement[1] = False
                    
            self.screen.blit(pygame.transform.scale(self.display,self.screen.get_size()), (0,0))
            
            pygame.display.update()
            self.clock.tick(60)
            
game().run()




