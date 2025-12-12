import pygame
import random

from logger import log_event
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")

            angle = random.uniform(20, 50)

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)

            vel_one = self.velocity.rotate(angle)
            vel_two = self.velocity.rotate(angle * -1)

            asteroid_one.velocity = vel_one * 1.2
            asteroid_two.velocity = vel_two * 1.2