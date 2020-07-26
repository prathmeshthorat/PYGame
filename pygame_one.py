import pygame 

# Initialise the instance 
pygame.init()
# Surface dimentions
gameDisplay=pygame.display.set_mode((800,600))
# Name
pygame.display.set_caption('HA HA')
# Add clock
clock= pygame.time.Clock()
crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        
        print (event)
        
    # pygame.display.update() OR pygame.display.flip()
    pygame.display.update()
    # fps
    clock.tick(60)
    
pygame.quit()
quit()
