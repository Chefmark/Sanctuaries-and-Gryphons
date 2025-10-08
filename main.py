from game.game import Game


game = Game()

while game.running:
    game.game_loop()