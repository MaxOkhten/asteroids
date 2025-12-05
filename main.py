import pygame
import constants
import player
from logger import log_state

def main():
    pygame.init()

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    clock_object = pygame.time.Clock()
    dt = 0

    new_player = player.Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print (f"Screen width: {constants.SCREEN_WIDTH}")
    print (f"Screen height: {constants.SCREEN_HEIGHT}")

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        new_player.draw(screen)

        pygame.display.flip()

        dt = clock_object.tick(60) / 1000

if __name__ == "__main__":
    main()
