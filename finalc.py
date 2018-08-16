import turtle
import random
import pygame
import time
score=0
lives=3
turtle.tracer(1,0)
fish_x_pos=0
fish_y_pos=-250
turtle.register_shape("backg1.gif")  
turtle.shape("backg1.gif")#Add river picture
heart=turtle.Turtle()
turtle.register_shape("hearts.gif")#ADD HEARTS TO THE LIVE
heart.shape("hearts.gif")
heart.penup()
heart.goto(420,320)
fish=turtle.Turtle()
turtle.register_shape("fish2.gif")
fish.shape("fish2.gif")#MAKING THE FISH 
fish.showturtle()
fish.penup()
fish.goto(0,-250)#STARTING POINT OF FISH

def check():#CHECKING IF THE FISH OUTSIDE THE FRAME
    if fish.pos()[0]>=475:
        fish.goto(470,fish.pos()[1])
    if fish.pos()[0]<=-475:
        fish.goto(-470,fish.pos()[1])
def move_fish_right():#moving fish right and checking if the fish is inside the Frame
    
    fish.goto(fish.pos()[0]+30,fish_y_pos)
    check()
     
def move_fish_left():#moving fish left and checking if the fish is inside the Frame
    
    fish.goto(fish.pos()[0]-30,fish_y_pos)
    check()
turtle.register_shape("popop.gif")#adding thr trash gif
hope=turtle.Turtle()
hope.shape("popop.gif")
caleb=turtle.Turtle()
mahmod=turtle.Turtle()
mahmod.shape("popop.gif")
mahmod.penup()
caleb.shape("popop.gif")
caleb.penup()
sondos=turtle.Turtle()
sondos.shape("popop.gif")
adam = turtle.Turtle()
sondos.penup()
rani=turtle.Turtle()
rani.shape("popop.gif")
rani.penup()
basil=turtle.Turtle()
basil.shape("popop.gif")
basil.penup()
valeria = turtle.Turtle()
kareem = turtle.Turtle()
omer = turtle.Turtle()
rommie = turtle.Turtle()
adam.shapesize(3)
valeria.shapesize(3)
omer.shapesize(3)
kareem.shapesize(3)
rommie.shapesize(3)
adam.shape("popop.gif")
valeria.shape("popop.gif")
kareem.shape("popop.gif")
omer.shape("popop.gif")
rommie.shape("popop.gif")
turtle.setup(1000,700)
hope.penup()
kareem.penup()
omer.penup()
rommie.penup()
distance = 5
valeria.up()
adam.up()
speed=12

def move_turtle():#moving the trush
    global speed
    global distance
    for t in my_turtles:
        x,y = t.pos()
        t.goto(x,y-distance)
    check_edge()
    check_player()
    if score==100:
         distance+=3
    if score==1000:
       distance+=3
    if score==2000:
        distance+=4
    if score==5000:
        distance+=4
    if score==20000:
        distance+=3
       
    turtle.ontimer(move_turtle, speed)

def rand_x():#giving us a random x to the trash
    x_range = (-50,50)
    
    return 10*random.randint(x_range[0], x_range[1])
    

def check_edge():
    for t in my_turtles:
        x,y = t.pos()
        if y <= -330:
            
            t.hideturtle()
            if random.randint(1,10) == 10:
                t.goto(rand_x(),330)
                t.showturtle()
def check_life():

     if lives==0:
        quit()
writer=turtle.Turtle()
writer1=turtle.Turtle()
def check_player():#checking if the player are hitting the trash
    global score
    score+=1
    for t in my_turtles:
        
        if abs(fish.pos()[0]-t.pos()[0])<40+distance and abs( fish.pos()[1]-t.pos()[1])<20:
            global lives
            t.goto(0,-2342)
            lives-=1
            check_life()
        else:
            writer1.undo()
            writer1.penup()
            writer1.ht()
            writer1.goto(-300,300)
            writer1.write(score,font=("Arial",30,"normal"))                
    writer.undo()
    writer.penup()

    writer.ht()

    writer.goto(350,300)
    writer.write(lives,font=("Arial",30,"normal"))
valeria.goto(rand_x(),330)
adam.goto(rand_x(),330)
my_turtles = [adam, valeria, kareem, omer, rommie,hope,caleb,sondos,rani,basil,mahmod]
move_turtle()
turtle.onkeypress(move_fish_right,"Right")
turtle.onkeypress(move_fish_left,"Left") 
turtle.listen() 
pygame.init()

pygame.mixer.music.load("musb.mp3")

pygame.mixer.music.play()
time.sleep(1)


 
