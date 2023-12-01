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
        self.check_collision()

    def check_collision(self):
        if self.y + self.radius > self.screen.get_height():
            self.y = self.screen.get_height() - self.radius
            self.vy = -self.k * self.vy
            if abs(self.vy) < 0.1:
                self.vy = 0
        if self.y - self.radius < 0:
            self.y = self.radius
            self.vy = -self.k * self.vy
        if self.x + self.radius > self.screen.get_width():
            self.x = self.screen.get_width() - self.radius
            self.vx = -self.k * self.vx
            if abs(self.vx) < 0.1:
                self.vx = 0
        if self.x - self.radius < 0:
            self.x = self.radius
            self.vx = -self.k * self.vx
            if abs(self.vx) < 0.1:
                self.vx = 0