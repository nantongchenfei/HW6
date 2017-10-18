import math
from numpy import *
import sys
import time
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib import animation

ballRadius = 5
ballMass = 1
timeCheck = []
CK = 0
timeCheck.sort()
RealTime = 0.0
timeStep = 1.0
showtimeList = list(range(1,1001))
balls = []
numBalls = 6
Walls=[[-100,100],[-100,100]]
ShowMovie = 'yes'
ShowPlot = 'No'

class ballCollision():
    def __init__(self, List = []):
        self.ID = List[0]
        self.PosX = float(List[1])
        self.PosY = float(List[2])
        self.VelX = float(List[3])
        self.VelY = float(List[4])
        self.trace = [[self.PosX],[self.PosY]]
        self.overbound = False

    def collision(self, other):
        thita = arctan((other.PosY - self.PosY) / (other.PosX - self.PosX+(1e-16)))
        transM = array([[cos(thita), -sin(thita)], [sin(thita), cos(thita)]])
        retransM = array([[cos(thita), sin(thita)], [-sin(thita), cos(thita)]])
        [[obX1, obY1],[obX2, obY2]] = dot(array([[self.VelX, self.VelY],[other.VelX, other.VelY]]), transM)
        [[self.VelX, self.VelY],[other.VelX, other.VelY]] = dot([[obX2, obY1],[obX1, obY2]], retransM)

    def timeToCollision(self,other):
        A = self.PosX - other.PosX
        B = self.VelX - other.VelX
        C = self.PosY - other.PosY
        D = self.VelY - other.VelY
        E = 2*A*B*C*D - A*A*D*D -B*B*C*C +(2*ballRadius)**2*B**2 +(2*ballRadius)**2*D**2
        F = A*B+C*D
        timeToCollision = 0.0
        if  E > 0 and (-F- sqrt(E)) >= 0:
            timeToCollision = (-F - sqrt(E))/(B*B+D*D)
        else:
            timeToCollision = -1
        return timeToCollision                
            
    def __str__(self):
        return "{:<6} {:<6} {:<6} {:<6} {:<6}".format(str(self.ID), str(self.PosX), str(self.PosY), str(self.VelX), str(self.VelY))

    def distance(self, other):
        return sqrt((self.PosX - other.PosX)**2 + (self.PosY - other.PosY)**2)

    def XYupdate(self, deltaTime):
        self.PosX = self.PosX + self.VelX * deltaTime
        self.PosY = self.PosY + self.VelY * deltaTime
        self.trace[0].append(self.PosX)
        self.trace[1].append(self.PosY)
        if (self.PosX - Walls[0][0] < ballRadius and self.VelX < 0) or (Walls[0][1] - self.PosX < ballRadius and self.VelX > 0):
            self.VelX = -  self.VelX
            self.overbound = True
        elif (self.PosY - Walls[1][0] < ballRadius and self.VelY < 0) or (Walls[1][1] - self.PosY < ballRadius and self.VelY > 0):
            self.VelY = -  self.VelY
            self.overbound = True
        else:
            self.overbound = False
        

##****************data for test********************
balls = []
balls.append(ballCollision(['2MU133',50 ,50, -1 ,-1]))
balls.append(ballCollision(['0WI913',-50, 50 ,1 ,0.5]))
balls.append(ballCollision(['6UP738', -50, -50 ,1 ,1]))
balls.append(ballCollision(['2MU133',0 ,0, 0.6 ,0.8]))
balls.append(ballCollision(['0WI913',12, 16 ,-0.6 ,-0.8]))
balls.append(ballCollision(['6UP738', -20, -20 ,2 ,2]))
##*********************************************
numBalls = len(balls)
        
def ballsUpdate(balls,time):
    boundaryOver = False
    for ball in balls:
        ball.XYupdate(time)
        boundaryOver = boundaryOver or ball.overbound
    return boundaryOver

def computeNextCollisionTime(balls,RealTime):
    i,j = 0,0
    shortestTimeToCollision = 0.0
    CollisionList = {}
    ballsToCollide = []
    for i in range(numBalls):
        for j in range(i+1,numBalls):
            CollisionList[(balls[i],balls[j])] = balls[i].timeToCollision(balls[j])
    balls_list = list(CollisionList.keys())
    value_list = list(CollisionList.values())
    templist = [value for value in value_list if value != -1]
    if len(templist) != 0:
        shortestTimeToCollision = min(templist)
        ballsToCollide = balls_list[value_list.index(shortestTimeToCollision)]
        NextCollisionTime = RealTime + shortestTimeToCollision
##        print('real time is: '+ str(RealTime) + '.  Next time collision is: ' + str(NextCollisionTime))
    else:
        NextCollisionTime = 1e+50
    return (ballsToCollide, NextCollisionTime)

if ShowMovie == 'yes' or ShowPlot == 'yes':
    timeCheck = showtimeList ## just for showing movie

while (RealTime < timeCheck[-1]):
    ballsToCollide, timeToCollide = computeNextCollisionTime(balls,RealTime)
    while(timeCheck[CK] < min(timeToCollide, timeCheck[-1])):
        hitwall = ballsUpdate(balls, (timeCheck[CK]-RealTime))
        if( hitwall == False):
            ##print(timeCheck[CK])
            ##for ball in balls:
                ##print(ball)
            RealTime = timeCheck[CK]
            CK += 1
        else:
            ballsToCollide, timeToCollide = computeNextCollisionTime(balls,RealTime)
    if timeToCollide < timeCheck[-1]:        
        ballsUpdate(balls, (timeToCollide - RealTime))
        ballsToCollide[0].collision(ballsToCollide[1])
        RealTime = timeToCollide
    else:
        break
if ShowPlot == 'yes':
    plt.plot(balls[0].trace[0],balls[0].trace[1],balls[1].trace[0],balls[1].trace[1],balls[2].trace[0],balls[2].trace[1])
    plt.show()
else:
    pass
##****************movie for show*********************
if ShowMovie == 'yes':
    Figsize = [8,8]
    WinDPI = 96
    fig = plt.figure(figsize=Figsize)
    ax = plt.axes()
    ax.set_xlim(Walls[0])
    ax.set_ylim(Walls[1])
    lines = []
    colors = ['r','b','g','y','r','b']

    for k in range(0, numBalls):
        lobj,  = ax.plot([],[],'o',markeredgecolor = colors[k],markerfacecolor = 'w', markersize = WinDPI * ballRadius * Figsize[0]/(Walls[0][1]- Walls[0][0]))
        lines.append(lobj)

    def init():
        for item in lines:
            item.set_data([],[])
        return lines

    def traceMove(i):
        for lnum,item in enumerate(lines):
            item.set_data(balls[lnum].trace[0][i],balls[lnum].trace[1][i])        
        return lines

    anim = animation.FuncAnimation(fig, traceMove, init_func=init, frames=1000, interval=20, blit=True)
    plt.show()
    plt.close()
else:
    pass
##*********************************************        
            
        
    
