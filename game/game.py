import pygame
from game.states.title import Title
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

        self.events = []  # <--- store last frame events here

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
        font = pygame.font.Font("assets/fonts/8-BIT WONDER.TTF", size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center = (x, y))
        surface.blit(text_surface, text_rect)

    def reset_keys(self):
        for action in self.actions:
            self.actions[action] = False

    def next(self):
        if not self.fading:
            self.fading = 'OUT'
            self.alpha = 0

    def update(self):
        self.screen.fill(config.BLACK)
        self.state_stack[-1].update(self.dt, self.actions)
        self.all_sprites.update(self.dt)
        if self.fading == 'OUT':
            self.alpha += 8
            if self.alpha >= 255:
                self.fading = 'IN'
                self.state_stack.append(self.next_state)
        else:
            self.alpha -= 8
            if self.alpha <= 0:
                self.fading = None
                

    def render(self):
        self.state_stack[-1].render(self.screen)
        self.screen.blit(pygame.transform.scale(self.screen, (config.SCREEN_WIDTH, config.SCREEN_HEIGHT)), (0, 0))
        if self.fading:
            self.veil.set_alpha(self.alpha)
            self.screen.blit(self.veil, (0, 0))
        pygame.display.flip()
    

    def check_events(self):
        events = pygame.event.get()
        self.events = events
        for event in events:
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.actions['space'] = True
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.actions['left'] = True
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.actions['right'] = True
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.actions['up'] = True
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.actions['down'] = True
                if event.key == pygame.K_RETURN:
                    self.actions['enter'] = True
                if event.key == pygame.K_ESCAPE:
                    self.actions['escape'] = True

    def game_loop(self):
        while self.running and not self.playing:
            self.check_events()
            self.render()
            self.update()
        
        while self.playing:
            self.dt = self.clock.tick(60) / 1000
            self.check_events()
            self.render()
            self.update()
