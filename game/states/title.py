from game.states.state import State
from game.states.menu import Menu
import pygame
import config

class Title(State, Menu):
    def __init__(self, game, name):
        State.__init__(self, game, name)
        Menu.__init__(self, game)
        self.open = False

        self.image = pygame.transform.scale(pygame.image.load("game/assets/sanctuariesandgryphonsmaintitle2.png"), (config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        self.rect = self.image.get_rect(center = (self.mid_w, self.mid_h))

        self.font = pygame.font.Font("game/assets/8-BIT WONDER.TTF", 18)
        self.rpg_text = self.font.render("A RPG by Markus.", True, config.BLACK)
        self.rpg_rect = self.rpg_text.get_rect(center =(config.SCREEN_WIDTH/2, config.SCREEN_HEIGHT/2))
        self.new_text = self.font.render("New Game", True, config.BLACK)
        self.new_rect = self.new_text.get_rect(center =(config.SCREEN_WIDTH/2, config.SCREEN_HEIGHT/2 - 100))
        self.load_text = self.font.render("Load Game", True, config.BLACK)
        self.load_rect = self.load_text.get_rect(center =(config.SCREEN_WIDTH/2, config.SCREEN_HEIGHT/2 - 50))
        self.quit_text = self.font.render("Quit", True, config.BLACK)
        self.quit_rect = self.quit_text.get_rect(center =(config.SCREEN_WIDTH/2, config.SCREEN_HEIGHT/2 + 100))

        self.cursor_rect.center = (self.mid_w + 85, self.mid_h + 10)
        self.menu_options = {
            "New Game":self.new_rect,
            "Load Game":self.load_rect,
            "Quit":self.quit_rect
        }
        self.index = 0

    