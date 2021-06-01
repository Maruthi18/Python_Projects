from turtle import Turtle, Screen
import turtle as t



t.bgcolor("black") # background color
t.pensize(2) # penSize or nib Thickness
t.speed(100) # Drawing Speed

colors = ["red", "green", "blue", "brown", "cyan", "aquamarine", "burlywood", "yellow"] # colors list to iterate

for _ in range(6):
	for color in colors: # iterate colors list one by one
		t.color(color) # select the color from colors list
		t.circle(100) # Draw a circle with radian 100
		t.right(10) # outside the circle is 10 degrees