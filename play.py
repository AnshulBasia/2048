from game import *
import math

print "1. Enter 1 to start and continue playing."   
print "2. Enter 0 to stop if you are not good enough."



play=input()
if(int(play)==1):
    print "What do you wish to achieve ? Enter a power of 2, preferably less than or equal to 2048 unless you are me."
    aim=input()
    exp=math.log(aim,2)
    if(not exp.is_integer()):
        print "Enter the power carefully, and your punishment is to run the program again :/"
        quit()
        
    print "Enter the height of grid :"
    height=input()
    print "Enter the width of the grid :"
    width=input()
    controller()
    game=TwentyFortyEight(height,width,aim) 
    while(int(play)==1):
        controller()
        print
        print "Enter your move:"
        print "Enter 0 to stop."
        move=input()
        if(int(move)==0):
            break
        game.move(move)
        
        
    print "Tired..?"
    print "Everyone has their limits, go and do something which you can complete."
    quit()
else:
    print "You are done, man!!"
    quit()
