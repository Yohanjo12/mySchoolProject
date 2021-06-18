import pygame
from pygame.sprite import Sprite

class Bullet2(Sprite):

	def __init__(self, game):
		super().__init__()
		self.screen = game.screen
		self.game_setting = game.game_setting
		self.color = self.game_setting.bullet2_color

		self.rect = pygame.Rect(0,0, self.game_setting.bullet2_width, self.game_setting.bullet2_height)

		self.rect.midtop = game.rocket.rect.midtop

		self.y = float(self.rect.y)

	def update(self):
		self.y -= self.game_setting.bullet2_speed


		self.rect.y = self.y



	def draw_bullet(self):
		pygame.draw.rect(self.screen, self.color, self.rect)