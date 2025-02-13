import os
import sys
import math
import random

import pygame

from scripts.entities import Ship, Asteroid
from scripts.projectiles import Projectile

class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()

        self.screen = pygame.display.set_mode((1000, 600))
        pygame.Surface.fill(self.screen,(255, 0, 0))
        self.clock = pygame.time.Clock()

        self.ship = Ship(self, (self.screen.get_width() / 2, self.screen.get_height() / 2), 20)
        self.bullets = []
        self.asteroids = []
        for i in range(5):
            self.asteroids.append(Asteroid(self, (random.randint(0, self.screen.get_width()), random.randint(0, self.screen.get_height())), random.randint(80, 100), 1))

        self.movement = False
        self.rotation = [False, False]
        self.dead = 3
        self.score = 0
        self.score_increment = 100
        self.font = pygame.font.SysFont('Monospace', 24)

    def main_menu(self):
        while True:
            self.screen.fill((0, 0, 0)) # Fill screen with black
            menu_text = self.font.render(f'Asteroids', True, (255, 255, 255)) # Have title of game rendered
            menu_rect = menu_text.get_rect(center=(self.screen.get_width() // 2, 100))  # Centered title
            self.screen.blit(menu_text, menu_rect.topleft) # Blit title of game to the screen

            mouse_pos = pygame.mouse.get_pos()

            play_button = self.font.render(f'Play', True, (255, 255, 255))
            play_rect = play_button.get_rect(center=(self.screen.get_width() // 2, 200))

            self.screen.blit(play_button, play_rect.topleft)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_rect.collidepoint(mouse_pos):
                        self.run()

            pygame.display.update()



    def run(self):
        while True:
            # Refresh screen
            self.screen.fill((0, 0, 0))

            # Update score and blit it onto the screen
            score_text = self.font.render(f'Score: {self.score}', True, (255, 255, 255))
            self.screen.blit(score_text, (10, 10))

            # Update the number of lives remaining and blit them onto the screen
            lives_text = self.font.render(f'Lives: {self.dead}', True, (255, 255, 255))
            self.screen.blit(lives_text, (10, 40))

            # Update and render ship every frame
            self.ship.update(self.movement, (self.rotation[0], self.rotation[1]))
            self.ship.render(self.screen)

            # Handle bullet behaviour
            for bullet in self.bullets:
                bullet.time += 1 # Bullet only exists for a certain amount of time
                if bullet.time < 100: # Whilst bullet is in list of bullets
                    bullet.x += bullet.vel[0] * math.sin(bullet.angle) # Velocity in x plane
                    bullet.y += bullet.vel[1] * -math.cos(bullet.angle) # Velocity in y plane

                    # Wrapping so that bullet stays on screen after reaching an edge
                    bullet.x %= self.screen.get_width()
                    bullet.y %= self.screen.get_height()
                else:
                    self.bullets.remove(bullet) # Removes bullet after set time

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.rotation[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.rotation[1] = True
                    if event.key == pygame.K_UP:
                        self.movement = True
                    if event.key == pygame.K_SPACE:
                        if len(self.bullets) < 5:
                            self.bullets.append(Projectile(self.ship.pos[0] + self.ship.size / 2, self.ship.pos[1] + self.ship.size / 2, 2, self.ship.angle_radians, 0))

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.rotation[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.rotation[1] = False
                    if event.key == pygame.K_UP:
                        self.movement = False

            # Render bullets every frame
            for bullet in self.bullets:
                bullet.render(self.screen)


            for asteroid in self.asteroids:
                asteroid.render(self.screen)
                asteroid.update()

            if len(self.asteroids) == 0:
                for i in range(5):
                    self.asteroids.append(Asteroid(self, (
                    random.randint(0, self.screen.get_width()), random.randint(0, self.screen.get_height())),
                                                   random.randint(80, 100), 2 ))


            if self.dead < 0:
                Game().main_menu()

            pygame.display.update()
            self.clock.tick(60)


Game().main_menu()