import pygame
from player import Player

from constants import *

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    start_x = SCREEN_WIDTH / 2
    start_y = SCREEN_HEIGHT / 2
    ship = Player(start_x, start_y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))
        ship.update(dt)
        ship.draw(screen)
        pygame.display.flip() #refreshes the screen
        time = clock.tick(60)
        dt = time / 1000 




#NOTE: this check will make sure that the code will only run if the file is executed directly
#  it will not run if this file is imported into another file
if __name__ == "__main__":
    main()

