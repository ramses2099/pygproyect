import pygame as pg


class SpaceGame:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((800, 600))
        pg.display.set_caption("Py Game Test")
        self.clock = pg.time.Clock()
        self.running = True
        self.dt = 0
        
        # Initialize Game Objects
        # self.player = Player(x=400, y=500)
        # self.enemies = EnemyManager()

    def run(self):
        while self.running:
            self._handle_events()
            self._update()
            self._draw()
            self.dt = self.clock.tick(60) / 1000
            print(f"FPS: {self.dt:.2f}")

    def _handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def _update(self):
        # self.player.update()
        # self.enemies.update()
        # Collision logic goes here
        # self.check_collisions()
        pass
        

    def _draw(self):
        self.screen.fill((0, 0, 20)) # Dark space background
        # self.player.draw(self.screen)
        # self.enemies.draw(self.screen)
        pg.display.flip()




def main():
    game = SpaceGame()
    game.run()
    
    
if __name__ == "__main__":
    main()