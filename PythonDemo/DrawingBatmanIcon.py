from turtle import *

def draw_batman():
    speed(13)  # Painting speed control
    bgcolor("black")  # Dark background for Batman
    pensize(3)
    
    # Draw Batman's head
    penup()
    goto(0, -50)
    pendown()
    color("gray", "dark gray")
    begin_fill()
    circle(80)  # Head circle
    end_fill()
    
    # Draw Batman's iconic pointed ears
    penup()
    goto(-50, 20)
    pendown()
    color("gray", "dark gray")
    begin_fill()
    seth(120)
    fd(60)
    right(120)
    fd(60)
    goto(-50, 20)
    end_fill()
    
    penup()
    goto(50, 20)
    pendown()
    begin_fill()
    seth(60)
    fd(60)
    left(120)
    fd(60)
    goto(50, 20)
    end_fill()
    
    # Draw Batman's eyes (white)
    penup()
    goto(-25, 0)
    pendown()
    color("white")
    begin_fill()
    seth(0)
    for _ in range(3):
        fd(20)
        left(120)
    end_fill()
    
    penup()
    goto(25, 0)
    pendown()
    begin_fill()
    for _ in range(3):
        fd(20)
        left(120)
    end_fill()
    
    # Draw Batman's mask outline
    penup()
    goto(-60, 10)
    pendown()
    pensize(5)
    color("black")
    seth(0)
    circle(70, 180)
    
    # Draw the bat symbol on chest
    penup()
    goto(0, -150)
    pendown()
    color("yellow", "yellow")
    begin_fill()
    # Bat wings
    seth(60)
    fd(40)
    right(120)
    fd(40)
    right(120)
    fd(40)
    seth(-60)
    fd(40)
    left(120)
    fd(40)
    left(120)
    fd(40)
    end_fill()
    
    hideturtle()
    done()

draw_batman()
