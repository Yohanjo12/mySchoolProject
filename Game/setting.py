import pygame
class Setting:


	def __init__(self):

		self.screen_width = 800
		self.screen_height = 600
		self.title = "*Alien game*"
		self.bg_color = (216, 0, 115)
		self.bg_image = pygame.image.load("img/c.jpg")
		




		#self.ship_speed = 5
		self.ship_life = 5
		#self.rocket_speed = 2
#setting bullet 1
		#self.bullet_speed = 4
		self.bullet_width = 10
		self.bullet_height = 15
		self.bullet_color = (255, 255, 255)
		self.bullets_limit = 5
#settingbullet2
		self.bullet2_speed = 4
		self.bullet2_width = 3  
		self.bullet2_height = 15
		self.bullet2_color = (0, 100, 255)
		self.bullets2_limit = 5

#setting aliens
		#self.alien_speed = 10.0
		self.alien_army_drop_speed = 10.0
		#self.alien_army_direction = 1 # 1 right, -1 left

		#scaling level
		self.speedup_level = 1.5
		self.score_scale = 2.0

		self.init_dynamic_setting()


	def init_dynamic_setting(self):
		self.ship_speed = 5
		self.rocket_speed = 2
		self.alien_speed = 5
		self.bullet_speed = 4
		self.alien_points = 50
		self.alien_army_direction = 1 # 1 right, -1 left

	def increase_speed(self):
		self.ship_speed *= self.speedup_level
		self.bullet_speed *= self.speedup_level
		self.rocket_speed *= self.speedup_level
		self.alien_speed *= self.speedup_level
		self.alien_points *= self.score_scale
