from game.states.state import State
from game.states.menu import Menu
from game.states.create import CreateCharacter
import pygame
import config

class Title(State, Menu):
    def __init__(self, game, name):
        State.__init__(self, game, name)
        Menu.__init__(self, game)
        self.open = False

        self.image = pygame.transform.scale(pygame.image.load("assets/title/sanctuariesandgryphonsmaintitle2.png"), (config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        self.rect = self.image.get_rect(center = (self.mid_w, self.mid_h))

        self.font = pygame.font.Font("assets/fonts/8-BIT WONDER.TTF", 18)
        self.rpg_text = self.font.render("A RPG by Chef Mark.", True, config.WHITE)
        self.rpg_rect = self.rpg_text.get_rect(center =(config.SCREEN_WIDTH/2, config.SCREEN_HEIGHT/2 + 250))
        self.new_text = self.font.render("New Game", True, config.WHITE)
        self.new_rect = self.new_text.get_rect(center =(config.SCREEN_WIDTH/2, config.SCREEN_HEIGHT/2 + 50))
        self.load_text = self.font.render("Load Game", True, config.WHITE)
        self.load_rect = self.load_text.get_rect(center =(config.SCREEN_WIDTH/2, config.SCREEN_HEIGHT/2 + 100))
        self.quit_text = self.font.render("Quit", True, config.WHITE)
        self.quit_rect = self.quit_text.get_rect(center =(config.SCREEN_WIDTH/2, config.SCREEN_HEIGHT/2 + 150))

        self.cursor_rect.center = (self.mid_w + 85, self.mid_h + 10)
        self.menu_options = {
            "New Game":self.new_rect,
            "Load Game":self.load_rect,
            "Quit":self.quit_rect
        }
        self.index = 0

    def move_cursor(self, actions):
        if actions['down']:
            self.index += 1
            if self.index == 3:
                self.index = 0
        if actions['move down']:
            self.index += 1
            if self.index == 3:
                self.index = 0        
        if actions['up']:
            self.index -= 1
            if self.index < 0:
                self.index = 2
        if actions['move up']:
            self.index -= 1
            if self.index < 0:
                self.index = 2

        self.cursor_rect.y = self.menu_options[list(self.menu_options.keys())[self.index]].y + 10
    
    def render(self, screen):
        screen.fill(config.BLACK)
        screen.blit(self.image, self.rect)
        if not self.open:
            screen.blit(self.rpg_text, self.rpg_rect)
            self.new_button = screen.blit(self.new_text, self.new_rect)
            self.load_button = screen.blit(self.load_text, self.load_rect)
            self.quit_button = screen.blit(self.quit_text, self.quit_rect)
            self.draw_cursor()

    def update(self, delta_time, actions):
        self.move_cursor(actions)
        if actions['enter'] or actions['space']:
            if self.index == 0:
                self.open = True
                self.game.create_character = CreateCharacter(self.game, "Create Character")
                self.game.next_state = self.game.create_character
                self.game.next()
            if self.index == 1:
                self.game.next_state = "Load Game"
                self.open = True
            if self.index == 2:
                self.game.running, self.game.playing = False, False

        self.game.reset_keys()