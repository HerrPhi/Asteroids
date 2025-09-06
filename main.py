import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()   #initialised Clock object
    dt = 0  #delta t variable

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        player.draw(screen)     #player is drawn after filling the screen but before flipping it

        player.update(dt)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")




if __name__ == "__main__":
    main()
