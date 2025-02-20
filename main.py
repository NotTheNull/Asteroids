import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *

group_updatable = None
group_drawable = None
group_asteroids = None

field = None
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
    global field
    global group_updatable
    global group_drawable
    global group_asteroids

    pygame.init()
    group_asteroids = pygame.sprite.Group()
    group_updatable = pygame.sprite.Group()
    group_drawable = pygame.sprite.Group()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    Player.containers = (group_drawable, group_updatable)
    Asteroid.containers = (group_asteroids, group_drawable, group_updatable)
    AsteroidField.containers = (group_updatable)

    field = AsteroidField()
    ship = Player(start_x, start_y)
    

def game_loop():
    dt = 0.0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))

        # weirdly, updateables can be called all at once ...
        group_updatable.update(dt)
        
        # iterate through the asteroids to see if the ship has collided
        for ast in group_asteroids:
            if ship.check_collision(ast):
                print("-- GAME OVER --")
                return

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

