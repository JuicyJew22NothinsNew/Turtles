import turtle

def turtleLetter(letter,tur):
    if letter=="box":
        tur.setheading(0)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)
        tur.right(90)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)

    elif letter == "A":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(30)
        tur.right(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(30)
        tur.right(180)
        tur.fd(15)
        tur.left(90)
        tur.fd(20)
        tur.pu()
        #fixes
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(35)
        #tur.right(180)
    elif letter == "B":
	    elif letter == "B":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(35)
        tur.right(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(30)
        tur.right(90)
        tur.fd(20)
        tur.right(180)
        tur.fd(20)
        tur.right(90)
        tur.right(180)
        tur.fd(15)
        tur.left(90)
        tur.fd(20)
        tur.pu()
        #fixes
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(35)
    elif letter == "C":
	    pass
    elif letter == "D":
	    pass
    elif letter == "E":
	    pass
    elif letter == "F":
	    pass
    elif letter == "G":
	     tur.setheading(0)
	    tur.pu()
	    tur.left(180)
	    tur.pd()
	    tur.fd(30)
	    tur.left(90)
	    tur.fd(50)
	    tur.left(90)
	    tur.fd(30)
	    tur.left(90)
	    tur.fd(15)
	    tur.left(90)
	    tur.fd(20)
	    tur.pu()
	    #fixes
	    tur.right(90)
	    tur.fd(20)
	    tur.right(90)
	    tur.fd(35)
	    tur.left(90)
	    tur.fd(35)
	    tur.right(90)
	    #tur.right(180)			
    elif letter == "H":
	    pass
    elif letter == "I":
	    pass
    elif letter == "J":
	    pass
    elif letter == "K":
	    pass
    elif letter == "L":
        tur.pendown()
        tur.right(90)
        tur.forward(30)
        tur.left(90)
        tur.forward(20)
        tur.penup()
        tur.forward(20)
        tur.left(90)
        tur.forward(30)
        tur.right(90)
    elif letter == "M":
        tur.pendown()
        tur.right(90)
        tur.forward(30)
        tur.penup()
        tur.left(180)
        tur.forward(30)
        tur.right(135)
        tur.pendown()
        tur.forward(20)
        tur.left(90)
        tur.forward(20)
        tur.right(135)
        tur.forward(30)
        tur.penup()
        tur.left(90)
        tur.forward(10)
        tur.left(90)
        tur.forward(30)
        tur.right(90)
    elif letter == "N":
	    pass
    elif letter == "O":
	    pass
    elif letter == "P":
	    pass		
    elif letter == "Q":
	    pass
    elif letter == "R":
	    pass
    elif letter == "S":
	    pass
    elif letter == "T":
	    pass
    elif letter == "U":
	    pass
    elif letter == "V":
	tur.pendown()
        tur.right(45)
        tur.fd(30)
        tur.right(270)
        tur.fd(30)
	    pass
    elif letter == "W":
	tur.pendown()
        tur.right(45)
        tur.fd(10)
        tur.right(270)
        tur.fd(10)
        tur.pendown()
        tur.right(90)
        tur.fd(10)
        tur.right(270)
        tur.fd(10) 
	  
	    pass
    elif letter == "X":
		tur.pendown()
        tur.right(45)
        tur.fd(20)
        tur.left(180)
        tur.fd(10)
        tur.right(90)
        tur.fd(10)
        tur.left(180)
        tur.fd(20)
	    pass
    elif letter == "Y":
	tur.pendown()
        tur.right(45)
        tur.fd(20)
        tur.right(45)
        tur.fd(20)
        tur.left(180)
        tur.fd(20)
        tur.right(45)
        tur.fd(20)
	    pass
    elif letter == "Z":
	tur.pendown()
        tur.right(360)
        tur.fd(30)
        tur.right(135)
        tur.fd(30)
        tur.right(225)
        tur.fd(30)
	    pass		

        
    elif letter == "Ax":
        # code here
        tur.forward(40)
		
    else:
        turtleLetter("box",tur)
	
2






window = turtle.Screen()
tur = turtle.Turtle()
tur.speed(1)
#turtleLetter("box",tur)
turtleLetter("A",tur)


window.exitonclick()
