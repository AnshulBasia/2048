from merge import *
import random
class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    
        
    def __init__(self, grid_height, grid_width, goal):
        self.height = grid_height
        self.width = grid_width
        self.aim=goal
        self.Grid=[[0 for x in range(self.width)] for y in range(self.height)]
        #Building the Grid.
        for x in range(2):
            self.putnumberrandomly()
        self.printtheGrid()   
    def __str__(self):
        #Return a string representation of the grid for debugging.
        string=""
        for indexi in range(self.height):
            for indexl in range(self.width):
                string+=str(self.Grid[indexi][indexl])
            string+='\n'
        return string

    def putnumberrandomly(self):
        a=randint(0,self.width-1)
        b=randint(0,self.height-1)
        while(self.Grid[b][a]!=0):
            a=random.randint(0,self.width-1)
            b=random.randint(0,self.height-1)
        # To ensure we get 70% 2 and 30% 4 in our grid at random position
        
        c=randint(0,9)
        if(c<=7):
            self.Grid[b][a]=2
        else:
            self.Grid[b][a]=4
    def printtheGrid(self):
        print
        for x in range(self.height):
            print self.Grid[x]
        
            
    def checkifwon(self, goal):
        for y in range(self.height):
            for x in range(self.width):
                if(self.Grid[y][x]==goal):
                    return True
        return False
    def checkiflost(self):
        b=1
        for y in range(self.height):
            for x in range(self.width):
                if(self.Grid[y][x]==0):
                    b=0
                    break
        if(b==0):
            return False
        else:
            return True
    def move(self,a):
        print
        if(int(a)==8):
            print "UP"
            for x in range(self.width):
                list=[]
                for y in range(self.height):
                    list.append(self.Grid[y][x])
                
                list=merge(list)
               
                for y in range(self.height):
                    self.Grid[y][x]=list[y]    
        if(int(a)==4):
            print "LEFT"
            for x in range(self.height):
                list=[]
                list=self.Grid[x]
                list=merge(list)
                self.Grid[x]=list
        if(int(a)==6):
            print "RIGHT"
            for x in range(self.height):
                list=[]
                list=self.Grid[x]
                list.reverse()
                list=merge(list)
                list.reverse()
                self.Grid[x]=list
        if(int(a)==2):
            print "DOWN"
            for x in range(self.width):
                list=[]
                for y in range(self.height):
                    list.append(self.Grid[y][x])
                list.reverse()
                list=merge(list)
                list.reverse()
                for y in range(self.height):
                    self.Grid[y][x]=list[y]
        if(int(a)!=2 and int(a)!=8 and int(a)!=6 and int(a)!=4):
            print "a",a
            print "Are you nuts..?"
            print "Use some brains and give a valid input"
            return
        self.printtheGrid()
        print "Generating a random no. at random empty position"
        print "......."
        time.sleep(1)
        print
        print "HERE"
        self.putnumberrandomly()
        self.printtheGrid()
        
        if(self.checkifwon(self.aim)):
            print "yeah! smarty"
            print "Congratulations, you won."
            quit()
            
        if(self.checkiflost()):
            print "LOSER"
            quit()
            
                

def controller():
    print
    print"            8-UP            "
    print"   4-LEFT         6-RIGHT    "
    print"            2-DOWN            "
