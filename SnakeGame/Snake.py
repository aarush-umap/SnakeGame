# Snake.py
import pygame

class Snake:
	def __init__(self, x, y, color, sq, vel_x, vel_y):
		self.x = x 
		self.y = y 
		self.color = color
		self.sq = sq 
		self.vel_x = vel_x
		self.vel_y = vel_y

	def draw(self, window):
		pygame.draw.rect(window, self.color, pygame.Rect(self.x, self.y, self.sq, self.sq))

	def get_x(self):
		return self.x

	def get_y(self):
		return self.y