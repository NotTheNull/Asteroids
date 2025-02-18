import pygame

from constants import *

def main():
    msg = f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}"
    print(msg)

#NOTE: this check will make sure that the code will only run if the file is executed directly
#  it will not run if this file is imported into another file
if __name__ == "__main__":
    main()

