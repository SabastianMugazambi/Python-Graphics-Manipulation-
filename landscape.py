#Sabastian Mugazambi

from graphics import *
import math


#Creating the Graphics Window and customizing it. 
window = GraphWin('landscape',500,700)
window.setBackground('light sky blue')
window.setCoords(0,0,1,1)

#Drawing landscape which includes; sea, land and buldings.
sea = Rectangle(Point(0,-0.1),Point(1,0.05))
sea.setFill('blue')
sea.draw(window)

building1 = Rectangle(Point(0.95,0),Point(1.1,0.4))
building1.setFill('brown')
building1.draw(window)
building1.setWidth(5)
building1.setOutline('snow')
building2 = Rectangle(Point(0.9,0),Point(0.95,0.3))
building2.setFill('gray')
building2.draw(window)
building2.setWidth(5)
building2.setOutline('snow')
building3 = Rectangle(Point(0.85,0),Point(0.9,0.35))
building3.setFill('black')
building3.draw(window)
building3.setWidth(5)
building3.setOutline('snow')
building4 = Rectangle(Point(0.65,0),Point(0.85,0.2))
building4.setFill(color_rgb(150,150,0))
building4.draw(window)
building4.setWidth(5)
building4.setOutline('snow')
building5 = Oval(Point(0.85,0.35),Point(0.9,0.45))
building5.setFill('black')
building5.setOutline('brown')
building5.setWidth(5)
building5.draw(window)

land = Oval(Point(0.1,-0.1),Point(1.9,0.1))
land.setFill(color_rgb(0,250,0))
land.draw(window)

#Setting initial location of cloud. 
#drawing the initial cloud.
cloud1 = Oval(Point(0,0.8),Point(0.2,0.83))
cloud1.setOutline('snow')
cloud1.setFill('snow')
cloud1.draw(window)
cloud2 = Oval(Point(0.01,0.815),Point(0.19,0.845))
cloud2.setOutline('snow')
cloud2.setFill('snow')
cloud2.draw(window)
cloud3 = Oval(Point(0.05,0.83),Point(0.188,0.86))
cloud3.setOutline('snow')
cloud3.setFill('snow')
cloud3.draw(window)

#Raw input from the user.
#Below I am asking the user to enter the windspeed and the time lapse since the cloud was on its original position. 
print"Not happy with the position of the cloud?, Let me fix it for you!."
x = float(raw_input('What is the windspeed in miles per hour?'))
y = float(raw_input('How many hours have passed?'))

#Calculations for the position of the cloud and assigning variable to significant numbers.
#Since I assigned coodinates of (1,1) to my top right coner then 1mile = 0.05units in the window
d = x*y
d2 = 0.05*d #to match my units in the window.
D = d2 % 1 #to always make sure the cloud appears in the window,
           # however, if you do not want the cloud to always apear delete 'D = d2 % 1' and replace D with d2 everywhere in the algorythm. 

#Undrawing the cloud at initial position so as to redraw it at desired position. 
cloud1.undraw()
cloud2.undraw()
cloud3.undraw()

#drawing the customized set of clouds.
cloud1 = Oval(Point(D,0.8),Point(D+0.2,0.83))
cloud1.setOutline('snow')
cloud1.setFill('snow')
cloud1.draw(window)
cloud2 = Oval(Point(D+0.01,0.815),Point(D+0.19,0.845))
cloud2.setOutline('snow')
cloud2.setFill('snow')
cloud2.draw(window)
cloud3 = Oval(Point(D+0.05,0.83),Point(D+0.188,0.86))
cloud3.setOutline('snow')
cloud3.setFill('snow')
cloud3.draw(window)

print"Here is your picture, have a beautiful day!"


raw_input('Hit Enter to close')
window.close()

