# Copyright 2017 John Curci jcurci92@bu.edu

import sys

class Particle():


    #IMPORTANT: 
        #Never access balls by ID.  
        #Program must be able to handle two balls with same ID 
    def __init__(self,name,x,y,dx,dy):
        self.name = name
        
        #x,y,dx,dy get updated when the Particle moves
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

        #x0,y0,dx0,dy0 are the initial values and should not change
        self.x0 = self.x
        self.y0 = self.y
        self.dx0 = self.dx
        self.dy0 = self.dy

    def __set__(self,x,y,dx,dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy



#This holds all of the particles and simulates their movement
class Field():

    def __init__(self):
        balls = []

    def __add__(self,ball):
        balls.append(ball)

    def simulate(self,startTime,endTime):
        #Here, balls move until there is a collision or
        #endTime is reached.  
        time = startTime
        
        while(1):

            if(time == endTime):
                return balls

            if(collision):
                print("some collision message")
                collisionTime = time
                balls = self.move(collisionTime,endTime)

            #TO DO:                
#Need to think about how to simulate "smooth" movement. 
#Don't want to calculate discrete jumps, just want to place
#objects at start and end location.
#Maybe send object along path and determine afterwards whether 
#they collided with anything, then redraw paths from collision
#time and repeat. 
#Do this until all paths are solved until final time.  



    def print_outputs(self,time):
        pass
        #TO DO
#Output: print a report for each t_i command line argument
#print in order of increasing time
#output ID x y dx dy\n then repeat for all objects 
#print with updated x y dx dy values
#print objects in the order they were entered
#program should not care what the object's ID is.  Doesn't care if two objects have same ID.  










    def collision(self,balls):
        pass
        #TO DO
#Need to do some kind of coordinate shift to
#calculate velocities after impact.
#Any number of balls may collide at the same instant.  




#main: 
    #read in the command line arguments
    #place the time inputs into a list of floats


def read_inputs(field):
    #Take in multiple lines of ID, x, y, dx, dy 
    #End on ctrl-D (EOF character)
    #unlimited number of lines
    x = []
    while(1):
        try:
            x.append(input())
        except:
            break
    print(x)

    #TO DO:
    #break up each line into tokens
    #return 1 if too many or too few arguments
    #return 1 if argument except ID is not a number
    #parse input and create Particle() objects
    #don't worry if objects are touching at start
    #have to deal with objects having the same name

    balls = balls[]
    for e in balls:
        field += e

    return 0




def main():

    #cmd line args:
    #ulimited in number, 
    #skip any less than 0, 
    #return 2 if no good input values
    #return 2 if any not a number
    try:
        times = [float(e) for e in sys.argv[1:]]
    except:
        exit(2)
    times = sorted([e for e in times if e >= 0])
    if len(times) == 0:
        exit(2)

    #create field object
    field = Field()


    #calls the method defined above
    #it reads from stdin and creates the balls
    #balls are loaded into field object
    read_inputs()


    i = 0
    simulate(0,times[i])
    print_outputs(times[i])
    while(i < len(times)-1):
        simulate(times[i],times[i+1])
        print_outputs(times[i+1])
        i += 1




if __name__ == '__main__':
    main()



#### Testing Notes ####

#What is the role and function of "random10.coordinates" file?
    #need to ecget this I think

#Following format is part of testing:
#collision 10 50 <random10.coordinates >random10.results
#"This saves the results into a text file called random10.results"