import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

	def __init__(self, game):
		super().__init__()
		self.screen = game.screen
		self.game_setting = game.game_setting
		self.color = self.game_setting.bullet_color

		self.rect = pygame.Rect(0,0, self.game_setting.bullet_width, self.game_setting.bullet_height)

		self.rect.midleft = game.ship.rect.midleft

		self.x = float(self.rect.x)

	def update(self):
		self.x -= self.game_setting.bullet_speed


		self.rect.x = self.x



	def draw_bullet(self):
		pygame.draw.rect(self.screen, self.color, self.rect)