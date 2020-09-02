import sys 
import pygame,pygame.font, pygame.event, pygame.draw, string
from setting import settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien

def run_game():
	pygame.init()
	ai_settings=settings()
	screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	ship=Ship(ai_settings,screen)
	bullets=Group()
	aliens=Group()
	gf.creat_fleet(ai_settings,screen,ship,aliens)
	

	while True:
		gf.check_events(ai_settings,screen,ship,bullets)
		ship.update()
		bullets.update()
		gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
		gf.update_aliens(ai_settings,aliens)
		gf.update_screen(ai_settings,screen,ship,aliens,bullets)
		
		


run_game()