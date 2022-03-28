# TurtleDraw
#
# By: Jeffrey Lacca
# Credits: Dr. Ray Klum, Prof. Eric Pogue, Internet
#
# All rights reserved
#
# Note: many more examples can be found online

from tkinter import Canvas
import turtle

TEXTFILENAME = 'turtle-draw.txt'

# ask user for file name

print('TurtleDraw-JL')


Junior = turtle.Turtle()
Junior.speed(10)
Junior.penup()
turtle.screensize(canvheight=450,canvwidth=450,)

print('Reading a text file line by line.')

turtleDrawTextfile = open(TEXTFILENAME, 'r')
line = turtleDrawTextfile.readline()
TotDistance = 0
x1 = 0
y1 = 0
tdistance = 0

while line:
	print(line, end='')
	parts = line.split(' ')

	if (len(parts) ==3):
		color = parts[0]
		x = int(parts[1])
		y = int(parts[2])

		Junior.color(color)
		Junior.goto(x,y)

		# calculate the distance and add it to the total distance.
	if x1 >= 0:
		tdistance = ((((x - x1)**2) + ((y - y1)**2))**0.5)
		x1 = x	
		y1 = y
	Junior.pendown()
	
	if (len(parts) ==1):#assumes that a single word = stop
		Junior.penup()
	TotDistance = TotDistance + tdistance	
		

	line = turtleDrawTextfile.readline()
	print("\n Total Distance: ", TotDistance)

#print the total near the bottom

print('\n Click Mouse to Close the Window')

turtle.penup()
turtle.goto(200,-200)
turtle.pendown()
turtle.write(TotDistance, align='left',move=False)


turtle.exitonclick()