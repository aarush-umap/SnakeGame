# main.py

import pygame
import os
import time
import random
from SinglyLinkedList import SinglyLinkedList
from ListNode import ListNode
from Apple import Apple
from Snake import Snake
pygame.font.init()

# Set up window
WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake!")

# Load colors
HEAD_COLOR = pygame.Color(158, 169, 161)
BODY_COLOR = pygame.Color(128, 143, 133)
APPLE_COLOR = pygame.Color(218, 255, 125)
BG_COLOR = pygame.Color(25, 25, 25)

# BG
BG = pygame.Rect(0, 0, WIDTH, HEIGHT)

# Icon sizes
SQUARE_SIZE = 25

# main method
def main():
	run = True

	# Level Setup
	FPS = 15
	main_font = pygame.font.SysFont("fixedsys", 70)
	apple_font = pygame.font.SysFont("fixedsys", 30)

	clock = pygame.time.Clock()

	start = False
	lost = False
	apples_eaten = 0

	rand_x = 525 
	#random.randrange(0, WIDTH - SQUARE_SIZE, SQUARE_SIZE)
	rand_y = 300
	#random.randrange(0, HEIGHT - SQUARE_SIZE, SQUARE_SIZE)

	apple = Apple(rand_x, rand_y, APPLE_COLOR, SQUARE_SIZE)
	
	player = SinglyLinkedList()
	player.add_first(Snake(200, 300, HEAD_COLOR, SQUARE_SIZE, 0, 0))
	player.add_last(Snake(175, 300, BODY_COLOR, SQUARE_SIZE, 0, 0))
	player.add_last(Snake(150, 300, BODY_COLOR, SQUARE_SIZE, 0, 0))
	player.add_last(Snake(125, 300, BODY_COLOR, SQUARE_SIZE, 0, 0))
	player.add_last(Snake(100, 300, BODY_COLOR, SQUARE_SIZE, 0, 0))
	direction = None
	vel = 1 

	def redraw_window():
		pygame.draw.rect(WIN, BG_COLOR, BG)
		temp = player.first
		while temp != None:
			temp.value.draw(WIN)
			temp = temp.get_next()
		apple.draw(WIN)

		apple_label = apple_font.render(str(apples_eaten), 1, (255,255,255))
		WIN.blit(apple_label, (WIDTH - apple_label.get_width() - 10, 20))
		if lost:
			lost_label = main_font.render("Game Over", 1, (255, 255, 255))
			WIN.blit(lost_label, (int(WIDTH/2 - lost_label.get_width()/2), 350))

		pygame.display.update()

	while(run):
		clock.tick(FPS)
		redraw_window()

		temp = player.first.get_next()
		while temp != None:
			if collision((player.first.value.x, player.first.value.y), (temp.value.x, temp.value.y)):
				lost = True
			temp = temp.get_next()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		keys = pygame.key.get_pressed()

		head = player.first.value
		changed_dir = False

		if not_in_bounds(head) or lost:
			lost = True
			run = False

		if keys[pygame.K_LEFT] and head.vel_x == 0: # left
			#player.first.vel_x = -5
			#player.first.vel_y = 0
			changed_dir = True
			start = True
			direction = "left"
		elif keys[pygame.K_RIGHT] and head.vel_x == 0: # right
			#player.first.vel_x = 5
			#player.first.vel_y = 0
			changed_dir = True
			start = True
			direction = "right"
		elif keys[pygame.K_UP] and head.vel_y == 0: # up
			#player.first.vel_x = 0
			#player.first.vel_y = -5
			changed_dir = True
			start = True
			direction = "up"
		elif keys[pygame.K_DOWN] and head.vel_y == 0: # down
			#player.first.vel_x = 0
			#player.first.vel_y = 5
			changed_dir = True
			start = True
			direction = "down"

		change_in_x = 0
		change_in_y = 0
		if direction == "left":
			head.color = BODY_COLOR
			new_y = head.y
			if changed_dir:
				new_y = ((head.y//25) * 25) + round_up_or_down(head.y%25)
				change_in_y = head.y - new_y
			player.add_first(Snake(head.x - SQUARE_SIZE - vel, new_y, HEAD_COLOR, SQUARE_SIZE, -vel, 0))
		if direction == "right":
			head.color = BODY_COLOR
			new_y = head.y
			if changed_dir:
				new_y = ((head.y//25) * 25) + round_up_or_down(head.y%25)
				change_in_y = head.y - new_y
			player.add_first(Snake(head.x + SQUARE_SIZE + vel, new_y, HEAD_COLOR, SQUARE_SIZE, vel, 0))
		if direction == "up":
			head.color = BODY_COLOR
			new_x = head.x
			if changed_dir:
				new_x = ((head.x//25) * 25) + round_up_or_down(head.x%25)
				change_in_x = head.x - new_x
			player.add_first(Snake(new_x, head.y  - SQUARE_SIZE - vel, HEAD_COLOR, SQUARE_SIZE, 0, -vel))
		if direction == "down":
			head.color = BODY_COLOR
			new_x = head.x
			if changed_dir:
				new_x = ((head.x//25) * 25) + round_up_or_down(head.x%25)
				change_in_x = head.x - new_x
			player.add_first(Snake(new_x, head.y + SQUARE_SIZE + vel, HEAD_COLOR, SQUARE_SIZE, 0, vel))

		if changed_dir:
			temp = player.first.next_node
			while temp != None:
				temp.get_value().x -= change_in_x
				temp.get_value().y -= change_in_y
				temp = temp.get_next()

		eaten = collision((player.first.value.x, player.first.value.y) , (apple.x, apple.y))
		if start and not(eaten):
			player.delete_last()
		elif eaten:
			apples_eaten += 1
			rand_x = random.randrange(0, WIDTH - SQUARE_SIZE, SQUARE_SIZE)
			rand_y = random.randrange(0, HEIGHT - SQUARE_SIZE, SQUARE_SIZE)
			apple = Apple(rand_x, rand_y, APPLE_COLOR, SQUARE_SIZE)
			if apples_eaten%2 == 0:
				FPS += 1

def round_up_or_down(num):
	if num > 12.5:
		return 25
	return 0

def collision(coor1, coor2):
	rect1 = pygame.Rect(coor1[0]+1, coor1[1]+1, SQUARE_SIZE-2, SQUARE_SIZE-2)
	rect2 = pygame.Rect(coor2[0]+1, coor2[1]+1, SQUARE_SIZE-2, SQUARE_SIZE-2)
	return rect1.colliderect(rect2)

def not_in_bounds(snake_head):
	return snake_head.x < 0 or snake_head.x > WIDTH or snake_head.y < 0 or snake_head.y > HEIGHT




def main_menu():
	title_font = pygame.font.SysFont("fixedsys", 70)
	run = True
	while run:
		pygame.draw.rect(WIN, BG_COLOR, BG)
		title_label = title_font.render("Press the mouse to begin!", 1, (255,255,255))
		WIN.blit(title_label, (int(WIDTH/2 - title_label.get_width()/2), 350))
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				main()
	pygame.quit()
main_menu()