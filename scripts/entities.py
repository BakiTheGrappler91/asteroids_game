import math
import random

import pygame

class PhysicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos) # Position as [x, y]
        self.size = size
        self.velocity = [0, 0] # Velocity as [vx, vy]
        self.img = pygame.Surface((size, size), pygame.SRCALPHA)


    #def rect(self):
        #return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def update(self):
        for bullet in self.game.bullets[:]:
            offset_x = int(bullet.x - self.pos[0])
            offset_y = int(bullet.y - self.pos[1])
            if self.mask.overlap(bullet.mask, (offset_x, offset_y)):
                self.on_collision(bullet)

    def on_collision(self, bullet):
        if self.type == "asteroid":
            self.game.bullets.remove(bullet)  # Remove bullet
            self.divide()

    def render(self, surf):
        surf.blit(self.img, (self.pos[0], self.pos[1]))

class Ship(PhysicsEntity):
    def __init__(self, game, pos, size):
        super(). __init__(game, "ship", pos, size)
        self.acceleration = 0.1 # Acceleration rate
        self.max_speed = 6 # Max speed limit
        self.drag = 0.99 # Simulates space friction
        self.angle = 0 # Angle in degrees for rotating image
        self.angle_radians = 0 # Angle in radians for change in velocity
        #self.img = pygame.Surface((size, size), pygame.SRCALPHA)
        pygame.draw.polygon(
            self.img, (255, 255, 255),
            [(0, 20), (10, 0), (20, 20), (10, 12)], 2
        )
        self.mask = pygame.mask.from_surface(self.img)

    def update(self, movement=0, rotation=(0, 0)):
        # Update angle
        self.angle += (rotation[1] - rotation[0]) * 4
        self.angle %= 360
        self.angle_radians = math.radians(self.angle)

        # Apply thrust
        if movement:
            ax = self.acceleration * math.sin(self.angle_radians)
            ay = -self.acceleration * math.cos(self.angle_radians)
            self.velocity[0] += ax
            self.velocity[1] += ay

            # Clamp velocity to max speed
            speed = math.sqrt(self.velocity[0]**2 + self.velocity[1]**2)
            if speed > self.max_speed:
                scale = self.max_speed / speed
                self.velocity[0] *= scale
                self.velocity[1] *= scale

        else:
            # Apply drag to velocity when no thrust is applied
            self.velocity[0] *= self.drag
            self.velocity[1] *= self.drag

        # Update position
        self.pos[0] += self.velocity[0]
        self.pos[1] += self.velocity[1]

        # Screen wrap-around
        screen_width = self.game.screen.get_width()
        screen_height = self.game.screen.get_height()

        if self.pos[0] > screen_width:
            self.pos[0] -= screen_width
        if self.pos[0] < 0:
            self.pos[0] += screen_width
        if self.pos[1] > screen_height:
            self.pos[1] -= screen_height
        if self.pos[1] < 0:
            self.pos[1] += screen_height

        for asteroid in self.game.asteroids[:]:
            offset_x = int(asteroid.pos[0] - self.pos[0])
            offset_y = int(asteroid.pos[1] - self.pos[1])

            if self.mask.overlap(asteroid.mask, (offset_x, offset_y)):
                self.game.dead -= 1
                self.pos = [self.game.screen.get_width() // 2, self.game.screen.get_height() // 2]
                self.velocity = [0, 0]
                print("collision")


    def render(self, surf):
        rotated_surface = pygame.transform.rotate(self.img, -self.angle)
        rotated_rect = rotated_surface.get_rect(
            center=(self.pos[0] + self.size / 2, self.pos[1] + self.size / 2)
        )

        surf.blit(rotated_surface, rotated_rect)


class Asteroid(PhysicsEntity):
    def __init__(self, game, pos, size, scale):
        super().__init__(game, 'asteroid', pos, size)
        pygame.draw.circle(self.img, (255, 255, 255), (size // 2, size // 2), size // 2)
        self.mask = pygame.mask.from_surface(self.img)
        self.x_vel = random.uniform(-1, 1) * scale
        self.y_vel = random.uniform(-1, 1) * scale
        self.scale = scale

    def divide(self):
        for i in range(2):
            if self.size > 30:
                self.game.asteroids.append(Asteroid(self.game, (self.pos[0], self.pos[1]), self.size // 2, self.scale))
        self.game.asteroids.remove(self)
        self.game.score += self.game.score_increment


    def update(self):
        super().update()
        self.pos[0] += self.x_vel
        self.pos[1] += self.y_vel

        self.pos[0] %= self.game.screen.get_width()
        self.pos[1] %= self.game.screen.get_height()

    def render(self, surf):
        surf.blit(self.img, (self.pos[0], self.pos[1]))