import pygame

import config

class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        pygame.display.set_caption("Sanctuaries and Gryphons")
        self.clock=pygame.time.Clock()
        self.running, self.playing = True, False
        self.state_stack = []
        self.dt = 0
        self.player = None


        self.actions = {
                'space':False, 
                'left':False, 
                'right':False, 
                'up':False, 
                'down':False, 
                'move left':False, 
                'move right':False, 
                'move up':False, 
                'move down':False, 
                'enter':False, 
                'left mouse':False,
                'escape':False
                }
        
        self.next_state = None
        self.fading = None
        self.alpha = 0
        sr = pygame.display.get_surface().get_rect()
        self.veil = pygame.Surface(sr.size)
        self.veil.fill((0, 0, 0))
        self.all_sprites = pygame.sprite.Group()
        self.load_states()


    def load_states(self):
        self.title = Title(self, "Title")
        self.state_stack.append(self.title)

    def draw_text(sel, surface, text, size, color, x, y):
        font = pygame.font.Font("game/assets/8-BIT WONDER.TTF", size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center = (x, y))
        surface.blit(text_surface, text_rect)