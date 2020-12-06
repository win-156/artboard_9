import pygame, sys

class GameState():           
	def __init__(self):
		self.state = "intro"

	def intro(self):      
		screen = pygame.display.set_mode((width,height))
		screen.fill((255,255,255))
		game1 = pygame.transform.scale(pygame.image.load("backround.png"), (width,height))
		screen.blit(game1,(0, 0))

		game_1 = pygame.transform.scale(pygame.image.load("minigame.png").convert_alpha(),(int(width/4), int(height/4)))
		game_1_rect = game_1.get_rect(center = (int(width/(18/7)), int(height/2)))

		game_2 = pygame.transform.scale(pygame.image.load("minigame.png").convert_alpha(),(int(width/4), int(height/4)))
		game_2_rect = game_2.get_rect(center = (int(width/(5/4)), int(height/2)))

		back_button= pygame.transform.scale(pygame.image.load("Nut-Quay-lai.jpg").convert_alpha(),(int(width/9), int(height/11)))
		back_button_rect = back_button.get_rect(center = (int(width - width/9), int(height/11)))


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:       
				pos = pygame.mouse.get_pos()             
				if game_1_rect.collidepoint(pos):    
					self.state = "game1"               
				if game_2_rect.collidepoint(pos):
					self.state = "game2"
				if back_button_rect.collidepoint(pos):
					self.state = "back"
		
			
			screen.blit(game_1,game_1_rect)
			screen.blit(game_2,game_2_rect)
			screen.blit(back_button, back_button_rect)
		
			pygame.display.update()

	def game1(self):            
		screen.fill((255,255,255))

		back_game1_button= pygame.transform.scale(pygame.image.load("Nut-Quay-lai.jpg").convert_alpha(),(int(width/9), int(height/11)))
		back_game1_button_rect = back_game1_button.get_rect(center = (int(width - width/9), int(height/11)))

		font = pygame.font.SysFont("Courier", 20)
		font = font.render("mang hinh game 1", False, (0, 128, 0))
		screen.blit(font, (100,200))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				pos = pygame.mouse.get_pos()
				if back_game1_button_rect.collidepoint(pos):
					self.state = "intro"

			screen.blit(back_game1_button, back_game1_button_rect)

			pygame.display.update()

	def game2(self):           
		screen.fill((0,0,0))

		back_game2_button= pygame.transform.scale(pygame.image.load("Nut-Quay-lai.jpg").convert_alpha(),(int(width/9), int(height/11)))
		back_game2_button_rect = back_game2_button.get_rect(center = (int(width - width/9), int(height/11)))


		font = pygame.font.SysFont("Courier", 20)
		font = font.render("mang hinh game 2", False, (255, 255, 255))
		screen.blit(font, (100,200))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				pos = pygame.mouse.get_pos()
				if back_game2_button_rect.collidepoint(pos):
					self.state = "intro"

			screen.blit(back_game2_button, back_game2_button_rect)

			pygame.display.update()

	def back(self):            
		screen.fill((255,255,255))
		font = pygame.font.SysFont("Courier", 20)
		font = font.render("dao dien game", False, (0, 128, 0))
		screen.blit(font, (100,200))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					self.state = "intro"

			pygame.display.update()

	def state_manager(self):             
		if self.state == "intro":        
			self.intro()
		if self.state == "game1":    
			self.game1()
		if self.state == "game2":     
			self.game2()
		if self.state == "back":     
			self.back()


pygame.init()
clock = pygame.time.Clock()

width = 800
height = 500

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Test")

game_state = GameState()      


while True:                          
	game_state.state_manager()       
	clock.tick(30)
