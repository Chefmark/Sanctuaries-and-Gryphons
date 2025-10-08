import pygame
import config

class Menu:
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = config.SCREEN_WIDTH / 2, config.SCREEN_HEIGHT / 2
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)


    def draw_cursor(self):
        self.game.draw_text(self.game.screen, "*", 75, config.WHITE, self.cursor_rect.x, self.cursor_rect.y)