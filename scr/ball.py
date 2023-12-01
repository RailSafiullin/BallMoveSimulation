import pygame


# Define the Ball class
class Ball:
    def __init__(self, x, y, radius, color, ball_vx, ball_vy, ball_ax, ball_ay, screen, k):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.screen = screen
        self.vx = ball_vx
        self.vy = ball_vy
        self.ax = ball_ax
        self.ay = ball_ay
        self.k = k

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (int(self.x), int(self.y)), self.radius)

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vx += self.ax
        if self.y + self.radius < self.screen.get_height():
            self.vy += self.ay