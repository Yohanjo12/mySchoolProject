import pygame
from pygame.sprite import Sprite

class Cliff(Sprite):

	def __init__(self, game):
		super().__init__()
		self.screen = game.screen
		self.screen_rect = game.screen.get_rect()
		self.settings = game.game_setting
		self.image = pygame .image.load("img/cliff.PNG")
		pygame.transform.scale(self.image, (100,1000))
		self.rect = self.image.get_rect()
		self.rect.bottomleft = self.screen_rect.bottomleft
		
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)


	def blitme(self):

		self.screen.blit(self.image, self.rect)