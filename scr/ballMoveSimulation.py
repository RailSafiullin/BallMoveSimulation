import pygame
from ball import Ball
import sys
class BallMoveSimulation:
    def __init__(self, WINDOW_WIDTH=900, WINDOW_HEIGHT=600,
                ball_x=450, ball_y=20, BALL_RADIUS=20,
                BALL_COLOR=(25, 25, 105),
                ball_vx=0.0, ball_vy=0.0, ball_ax=0.0, ball_ay=9.8, k=0.6,
                clock_tick=120, escape_height=10.0):
        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.WINDOW_HEIGHT = WINDOW_HEIGHT
        self.clock_tick = clock_tick
        self.ball_x = ball_x
        self.ball_y = ball_y
        self.BALL_RADIUS = BALL_RADIUS
        self.BALL_COLOR = BALL_COLOR
        self.ball_vx = ball_vx
        self.ball_vy = ball_vy
        self.ball_ax = ball_ax / self.clock_tick
        self.ball_ay = ball_ay / self.clock_tick
        self.k = k
        self.escape_height = escape_height

        self.ball_x = self.WINDOW_WIDTH // 2
        self.ball_y = self.WINDOW_HEIGHT // 4

        pygame.init()

        self.simulation_window = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption("Elastic Ball Simulation")
        self.clock = pygame.time.Clock()

        self.ball = Ball(self.ball_x, self.ball_y, self.BALL_RADIUS, self.BALL_COLOR, self.ball_vx, self.ball_vy,
                        self.ball_ax, self.ball_ay, self.simulation_window, self.k)
        
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
            self.ball.update()

            if self.ball.y + self.ball.radius > self.WINDOW_HEIGHT - self.escape_height:
                if abs(self.ball.vy) < 0.1 and self.ball.vy <= 0:
                    pygame.quit()
                    sys.exit()

            self.ball.draw()
            pygame.display.update()
            self.clock.tick(self.clock_tick)