#Udacity - Programming Foundations with Python
#Python 2.7.13
#Assignment - Learn about classes by writing a program that draw a circle out
#of sqaures.
#

import turtle

def draw_square(my_turtle):
    for i in range(1,5):
        my_turtle.forward(100)
        my_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    #Create an instance of turtle - Brad
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    for i in range(1,37): #complete 360 degree
        draw_square(brad)
        brad.right(10) #turn 10 degree

    #Create an instance of turtle - Angie
    #angie = turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("blue")
    #angie.circle(100)

    window.exitonclick()

draw_art()
    
