import pygame
from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        new_angle = random.uniform(20, 50)
        new_vec1 = self.velocity.rotate(new_angle)
        new_vec2 = self.velocity.rotate(new_angle * -1)
        new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        new_asteroid1.velocity = new_vec1 * 1.2
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        new_asteroid2.velocity = new_vec2 * 1.2

        self.kill()