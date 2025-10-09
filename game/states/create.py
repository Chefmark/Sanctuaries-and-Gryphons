from game.states.menu import Menu
from game.states.state import State
import pygame
import pygame_widgets
from pygame_widgets.textbox import TextBox
import config

class CreateCharacter(State,Menu):
    def __init__(self, game, name):
        State.__init__(self, game, name)
        Menu.__init__(self, game)
        self.open = False

        self.image = pygame.transform.scale(pygame.image.load("assets/title/charactercreator.png"),
                                            (config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        self.rect = self.image.get_rect(center = (self.mid_w, self.mid_h))
        self.font = pygame.font.Font("assets/fonts/8-BIT WONDER.TTF", 18)
        self.textbox = TextBox(self.game.screen, self.mid_w - 200, self.mid_h - 100, 400, 40,
                                       fontSize = 18, borderColour = config.BLACK, textColour = config.BLACK, radius=10, borderThickness=2, font=self.font)

    def render(self, surface):
        surface.fill(config.BLACK)
        surface.blit(self.image, self.rect)
        self.textbox.draw()
        self.game.draw_text(surface, "Enter your name", 18, config.WHITE, self.mid_w, self.mid_h - 150)


    def update(self, delta_time, actions):
        events=pygame.event.get()
        pygame_widgets.update(events)
        self.game.reset_keys()
