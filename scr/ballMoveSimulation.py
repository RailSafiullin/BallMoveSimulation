import pygame
import sys


class BallMoveSimulation:
    def __init__(self, WINDOW_WIDTH=900, WINDOW_HEIGHT=600,
                clock_tick=120):
        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.WINDOW_HEIGHT = WINDOW_HEIGHT
        self.clock_tick = clock_tick
        
        pygame.init()

        self.simulation_window = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption("Elastic Ball Simulation")
        self.clock = pygame.time.Clock()

    def start_simulation(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()

            self.simulation_window.fill((225, 225, 225))
            pygame.display.update()
            self.clock.tick(self.clock_tick)