from turtle import *

def hello_world():
    for i in range(3):
        print('hello world')
hello_world()
# -----------------------------------
def sum_two_number(number1,number2):
    sum = number1 + number2
    print(sum)
sum_two_number(1,2)
# -----------------------------------
def draw_square(length,color_line):
	color(color_line)
	for i in range(4):
		forward(length)
		left(90)
draw_square(100,'black')
# -----------------------------------
for j in range(30):
    draw_square(j * 5, 'red')
    left(17)
    penup()
    forward(j * 2)
    pendown()
# ---------------------------------
def draw_star(a,b,length):
	penup()
	setx(a)
	sety(b)
	pendown()
	for j in range(5):	
		right(144)	
		forward(length)
speed(0)
color('blue')
for j in range(100):
    import random
    a = random.randint(-300, 300)
    b = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(a, b, length)
draw_star(0,200,200)

mainloop(