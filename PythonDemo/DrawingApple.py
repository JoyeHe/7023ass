from turtle import *

def draw_apple():
    speed(13)
    bgcolor("sky blue")
    pensize(3)
    
    # Draw apple body (red circle)
    penup()
    goto(0, -80)
    pendown()
    color("red", "red")
    begin_fill()
    circle(80)
    end_fill()
    
    # Draw apple indent at top
    penup()
    goto(-30, 50)
    pendown()
    color("red", "dark red")
    begin_fill()
    seth(180)
    circle(30, 180)
    end_fill()
    
    # Draw stem
    penup()
    goto(-5, 80)
    pendown()
    color("brown", "saddle brown")
    pensize(8)
    begin_fill()
    seth(90)
    fd(25)
    right(90)
    fd(10)
    right(90)
    fd(25)
    right(90)
    fd(10)
    end_fill()
    
    # Draw leaf
    penup()
    goto(5, 80)
    pendown()
    color("green", "green")
    pensize(2)
    begin_fill()
    seth(45)
    circle(20, 90)
    left(90)
    circle(20, 90)
    end_fill()
    
    # Add highlight shine
    penup()
    goto(-25, 20)
    pendown()
    color("pink", "pink")
    begin_fill()
    circle(15)
    end_fill()
    
    hideturtle()
    done()

draw_apple()
