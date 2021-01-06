# Apple.py
import pygame

class Apple:
	def __init__(self, x, y, color, sq):
		self.x = x + 1
		self.y = y + 1
		self.color = color
		self.sq = sq - 2

	def draw(self, window):
		pygame.draw.rect(window, self.color, pygame.Rect(self.x, self.y, self.sq, self.sq))

	def get_x(self):
		return self.x

	def get_y(self):
		return self.y