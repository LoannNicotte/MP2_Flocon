import turtle 

def flocon(d=7):
    turtle.penup()
    turtle.goto(-270,0)
    turtle.speed(0)
    turtle.pendown()
    for i in range(2):
        for i in range(2):
            for i in range (2):
                for i in range(2):
                    for i in range(2):
                        turtle.forward(d)
                        turtle.lt(60)
                        turtle.forward(d)
                        turtle.rt(120)
                        turtle.forward(d)
                        turtle.lt(60)
                        turtle.forward(d)
                        turtle.lt(60)
                    turtle.rt(180)
                turtle.rt(180)
            turtle.rt(180)
        turtle.rt(180)
        for i in range(2):
            for i in range (2):
                for i in range(2):
                    for i in range(2):
                        turtle.forward(d)
                        turtle.lt(60)
                        turtle.forward(d)
                        turtle.rt(120)
                        turtle.forward(d)
                        turtle.lt(60)
                        turtle.forward(d)
                        turtle.lt(60)
                    turtle.rt(180)
                turtle.rt(180)
            turtle.rt(180)
    turtle.exitonclick()
    
def flocon_full(d=6):
    turtle.penup()
    turtle.goto(-250,142)
    turtle.speed(0)
    turtle.pendown()
    for i in range(3):
        for i in range(2):
            for i in range(2):
                for i in range (2):
                    for i in range(2):
                        for i in range(2):
                            turtle.forward(d)
                            turtle.lt(60)
                            turtle.forward(d)
                            turtle.rt(120)
                            turtle.forward(d)
                            turtle.lt(60)
                            turtle.forward(d)
                            turtle.lt(60)
                        turtle.rt(180)
                    turtle.rt(180)
                turtle.rt(180)
            turtle.rt(180)
            for i in range(2):
                for i in range (2):
                    for i in range(2):
                        for i in range(2):
                            turtle.forward(d)
                            turtle.lt(60)
                            turtle.forward(d)
                            turtle.rt(120)
                            turtle.forward(d)
                            turtle.lt(60)
                            turtle.forward(d)
                            turtle.lt(60)
                        turtle.rt(180)
                    turtle.rt(180)
                turtle.rt(180)
    turtle.exitonclick()
        
flocon_full()
