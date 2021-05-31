from turtle import *
import random

s = Turtle() # we created a turtle object

colors = ["red", "green", "blue", "brown", "cyan", "grey", "burlywood", "pink"]

def draw(sides):
	angle = 360 / sides   # Example pentagon angle = 360 / 5 = 72
	for _ in range(sides):
		s.forward(100)
		s.right(angle)  # s.right(72) for pentagon

for side in range(3, 11):  # range for the sides of shapes
	s.color(random.choice(colors)) # randomly select the colors from colors list
	draw(side)
