import pygame
import constants
import player
import asteroid

from asteroidfield import AsteroidField
from logger import log_state

def main():
    pygame.init()

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    clock_object = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    player.Player.containers = (updatable, drawable)
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()

    new_player = player.Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)


    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print (f"Screen width: {constants.SCREEN_WIDTH}")
    print (f"Screen height: {constants.SCREEN_HEIGHT}")

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # new_player.update(dt)
        updatable.update(dt)

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        dt = clock_object.tick(60) / 1000

if __name__ == "__main__":
    main()
