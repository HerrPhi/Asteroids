import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    game_clock = pygame.time.Clock()   #initialised Clock object
    dt = 0  #delta t variable

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")


        pygame.display.flip()
        dt = game_clock.tick(60)/1000


    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")




if __name__ == "__main__":
    main()
