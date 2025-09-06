from circleshape import *
import random

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            velocity_angle1 = self.velocity.rotate(random_angle)
            velocity_angle2 = self.velocity.rotate(-random_angle)
            new_radius= self.radius - ASTEROID_MIN_RADIUS
            new_Asteroid1 = Asteroid(self.position[0], self.position[1],new_radius)
            new_Asteroid2 = Asteroid(self.position[0], self.position[1],new_radius)
            new_Asteroid1.velocity = velocity_angle1 * 1.2
            new_Asteroid2.velocity = velocity_angle2 * 1.2


    