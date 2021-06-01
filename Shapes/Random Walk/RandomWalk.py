from turtle import Turtle ,Screen
import random
import turtle as t

s = t.Turtle()
colors = ["red", "green", "blue", "brown", "cyan", "aquamarine", "burlywood", "yellow"]
directions = [0, 90, 180, 270, 360]

for _ in range(200):
	s.speed("fastest")
	s.pensize(10)
	s.setheading(random.choice(directions))
	s.color(random.choice(colors))
	s.forward(40)