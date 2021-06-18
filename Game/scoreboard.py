import pygame.font
from pygame.sprite import Group

from ship import Ship 

class Scoreboard:

	def __init__(self, game):
		self.game = game
		self.screen = game.screen
		self.screen_rect = self.screen.get_rect()

		self.settings = game.game_setting
		self.stats = game.my_statistics


		self.text_color = (255,255,255)
		self.font = pygame.font.SysFont(None, 48)

		self.show_score()
		self.show_high_score()
		self.show_ships()
		self.show_level()
	


	def show_score(self):
		round_score = round(self.stats.score, -1)
		#score_string = str(self.stats.score)
		score_string = "{:,}".format(round_score)
		self.score_image = self.font.render(score_string, True, self.text_color, self.settings.bg_image)

		self.score_rect_image = self.score_image.get_rect()
		self.score_rect_image.right = self.screen_rect.right - 30
		self.score_rect_image.top = 10

	def draw_score(self):
		self.screen.blit(self.score_image, self.score_rect_image)
		self.screen.blit(self.high_score_image, self.high_score_rect_image)
		self.screen.blit(self.level_image, self.level_rect_image)
		self.ships.draw(self.screen)

	def show_high_score(self):
		round_high_score = round(self.stats.high_score, -1)
		#score_string = str(self.stats.score)
		high_score_string = "{:,}".format(round_high_score)
		self.high_score_image = self.font.render(high_score_string, True, self.text_color, self.settings.bg_image)

		self.high_score_rect_image = self.high_score_image.get_rect()
		self.high_score_rect_image.midtop = self.screen_rect.midtop
		self.high_score_rect_image.top = 10

	def check_high_score_(self):
		if self.stats.score > self.stats.high_score:
			self.stats.high_score = self.stats.score
			self.show_high_score()

	def show_level(self):
		#level_score = round(self.stats.level_score, -1)
		level_string = "LEVEL : "+str(self.stats.level)
		#level_string = "{:,}".format(level_score)
		self.level_image = self.font.render(level_string, True, self.text_color, self.settings.bg_image)

		self.level_rect_image = self.level_image.get_rect()
		self.level_rect_image.right = self.screen_rect.right - 30
		self.level_rect_image.top = 40

	def show_ships(self):
		self.ships = Group()

		for every_ship in range(self.stats.my_shipP1_life):
			ship = Ship(self.game)
			ship.rect.x = 10 + every_ship*ship.rect.width

			ship.rect.y = 10
			self.ships.add(ship)
