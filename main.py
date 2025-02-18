import pygame
from player import Player

from constants import *

group_updatable = None
group_drawable = None

ship = None
screen = None
clock = None
start_x = SCREEN_WIDTH / 2
start_y = SCREEN_HEIGHT / 2

def main():
    game_init()
    game_loop()

def game_init():
    global screen
    global clock
    global ship
    global group_updatable
    global group_drawable

    pygame.init()
    group_updatable = pygame.sprite.Group()
    group_drawable = pygame.sprite.Group()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    Player.containers = (group_drawable, group_updatable)
    ship = Player(start_x, start_y)
    
    #group_drawable.add(ship)
    #group_updatable.add(ship)


def game_loop():
    dt = 0.0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))

        # weirdly, updateables can be called all at once ...
        group_updatable.update(dt)
        
        # ... but drawables have to be called individually.  Is it a refresh rate thing?
        for entity in group_drawable:
            entity.draw(screen)
        
        pygame.display.flip() #refreshes the screen
        time = clock.tick(60)
        dt = time / 1000 



#NOTE: this check will make sure that the code will only run if the file is executed directly
#  it will not run if this file is imported into another file
if __name__ == "__main__":
    main()

