import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()   #initialised Clock object
    dt = 0  #delta t variable

    updatable = pygame.sprite.Group()   #create empty updatable group
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)   #add all instances of player to both groups
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    asteroidfield = AsteroidField()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collision_detection(player):
                print("Game over!")
                sys.exit()

        screen.fill("black")

        for draw in drawable:
            draw.draw(screen)
        #player.draw(screen)     #player is drawn after filling the screen but before flipping it
        #player.update(dt)

        pygame.display.flip()
        #limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")




if __name__ == "__main__":
    main()
