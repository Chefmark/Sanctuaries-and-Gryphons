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
        self.charactername = TextBox(self.game.screen, self.mid_w - 400, self.mid_h - 115, 400, 40,
                                       fontSize = 18, borderColour = config.BLACK, textColour = config.BLACK, radius=10, borderThickness=2, font=self.font)

        # position the "Set Attributes" text just below the name textbox
        textbox_bottom_y = (self.mid_h - 115) + 40  # textbox top + height
        set_center_y = textbox_bottom_y + 20
        self.set_text = self.font.render("Set Attributes", True, config.BLACK)
        self.set_rect = self.set_text.get_rect(center =(self.mid_w - 250, set_center_y))

        # attributes (labels + dynamic numeric values) aligned in columns
        attr_start_y = set_center_y + 40
        spacing = 40

        # align labels with the "Set Attributes" text left edge
        label_x = self.set_rect.left
        # create labels first so we can measure widest label and position values consistently
        self.attributes = {
            "Strength": 10,
            "Intelligence": 10,
            "Dexterity": 10,
            "Constitution": 10
        }

        self.attr_labels = {}
        for i, name in enumerate(self.attributes.keys()):
            y = attr_start_y + i * spacing
            label_surf = self.font.render(name, True, config.BLACK)
            label_rect = label_surf.get_rect(midleft=(label_x, y))
            self.attr_labels[name] = (label_surf, label_rect)

        # compute value column x based on widest label + padding so values line up neatly
        max_label_width = max(surf.get_width() for surf, _ in self.attr_labels.values())
        padding = 24
        self.attr_value_x = label_x + max_label_width + padding

        # placeholders for value rects (value surfaces will be created each frame)
        self.attr_value_rects = {}
        for i, name in enumerate(self.attributes.keys()):
            y = attr_start_y + i * spacing
            self.attr_value_rects[name] = pygame.Rect(self.attr_value_x, y - 12, 0, 0)


    def render(self, surface):
        surface.fill(config.BLACK)
        surface.blit(self.image, self.rect)
        self.charactername.draw()
        # helper prompt
        self.game.draw_text(surface, "Enter your name", 18, config.WHITE, self.mid_w - 250, self.mid_h - 150)

        # draw set attributes header
        surface.blit(self.set_text, self.set_rect)

        # draw attribute labels and dynamic values aligned in columns
        for name, (label_surf, label_rect) in self.attr_labels.items():
            surface.blit(label_surf, label_rect)
            # render current value fresh so it stays dynamic
            value_text = str(self.attributes[name])
            value_surf = self.font.render(value_text, True, config.BLACK)
            # align values midleft at the computed value column and same row as label
            value_rect = value_surf.get_rect(midleft=(self.attr_value_x, label_rect.centery))
            surface.blit(value_surf, value_rect)


    def update(self, delta_time, actions):
        events = getattr(self.game, "events", [])
        pygame_widgets.update(events)
        self.game.reset_keys()
