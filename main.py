import pygame

from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))
        pygame.display.flip() #refreshes the screen




#NOTE: this check will make sure that the code will only run if the file is executed directly
#  it will not run if this file is imported into another file
if __name__ == "__main__":
    main()

