import random 

class Pet:

    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.direction = 0

    def eat(self):
        print("Despite being on a diet " + str(self.name) + " had a cheat day")

    def sleep(self):
        print("The alarm continues to blare Smashmouth but " + str(self.name) + " is still asleep")

    def play(self, other):
        if other != self:
            print(str(self.name) + " and " + str(other.name) + " had a great time playing together.") 
        elif self == other:
            print(str(self.name) + " played alone.... how sad.")
            
    def race(self, other):
        if other != self: 
            print(str(self.name) + " was too fast for " + str(other.name)) or print(str(other.name) + " was too fast for " + str(self.name)) 
        elif self == other:
            print(str(self.name) + " raced against themself and somehow still lost.")
            
    def fight(self, other):
        if other != self:
            print(str(self.name) + " and " + str(other.name) + " beat each other to a pulp.") 
        elif self == other:
            print("It turns out " + str(self.name) + "'s worst enemy was themself.") 
        
    def kill(self, other):
        if other != self:
            print(self.name + " murdered " + other.name + " in cold blood... think twice before stealing someone else's mans!")
        elif self == other:
            print(self.name + " had to escape the IRS... and they could only do that through death.") 

    def rotate_right(self):
        self.direction += 1

        if self.direction == 4:
            self.direction = 0

    def rotate_left(self):
        self.direction -= 1

        if self.direction == -1:
            self.direction = 3

    def move(self):
        if self.direction == 0:
            self.y += 1
        elif self.direction == 1:
            self.x += 1
        elif self.direction == 2:
            self.y -= 1
        elif self.direction == 3:
            self.x -= 1

    def __repr__(self):
        return "Name: " + self.name + \
               " [x=" + str(self.x) + \
               ", y=" + str(self.y) + \
               ", d=" + str(self.direction) + "]"
    
    
pet1 = Pet("Olivia")
pet2 = Pet("Keech")
pet3 = Pet("Taylor")
