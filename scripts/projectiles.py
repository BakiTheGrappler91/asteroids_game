import pygame

class Projectile(object):
    def __init__(self, x, y, radius, angle, time):
        self.x = x
        self.y = y
        self.radius = radius
        self.angle = angle
        self.time = time
        self.vel = [7, 7]
        self.img = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.img, (255, 255, 255), (radius, radius), self.radius)
        self.mask = pygame.mask.from_surface(self.img)



    def render(self, surf):
        surf.blit(self.img, (self.x, self.y))
