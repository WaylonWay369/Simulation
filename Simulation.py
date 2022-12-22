import random
import Physics
from time import sleep

class Object():
    def __init__(self, id , type):
        self.id = id
        self.type = type 

class Living(Object):
    def __init__(self,_id, type):
        super().__init__(_id, type)
        self.isAlive = True
        self.energy = 50
        self.id = str(_id)
        self.sight = 2
        self.sightdict = {}
        self.age = 0 
        self.maxhealth = 100
        self.health = self.maxhealth
        self.transform = Physics.Transform()
        ##print("New Life: " + str(self.id))
        
    def Stats(self):
        print("Id: " + str(self.id))
        print("Sight: " + str(self.sight))
        print("Age: " + str(self.age))
        print("Energy: " + str(self.energy))
        print("Health: " + str(self.health) + "/" + str(self.maxhealth))
        print("Position: " + str(self.transform.GetPosition()))
        
    def UpdateSight(self):
        x , y = self.transform.GetPosition()
        
        print(x,y)
        
    
    
    def Damage(self):
        self.health -=50
        if(self.health <= 0):
            self.isAlive = False
            del self
            
class Animal(Living):
    def __init__(self, _id):
        super().__init__(_id, "Animal")
        print("New Animal: " + str(self.id))
        self.stepsize = random.randint(1, 3)
        self.transform.SetPosition(random.randint(0, 11), random.randint(0, 11))
        
    def Attack(self,_prey):
        self.energy -= 1
        h = self.health
        ph = _prey.health
        
        if(h>=ph):
            _prey.Damage()
            print(str(_prey.id) + " got hurt")
            print(str(_prey.id) + " health is at " + str(_prey.health))
            return
        if(h<ph):
            self.Damage()
            print(str(self.id) + " got hurt")
            print(str(_prey.id) + " health is at " + str(_prey.health))
            return
                
                
    def Chase(self, _prey): 
        
        if(self.transform.GetPosition() == _prey.transform.GetPosition()):
            self.Attack(_prey)
            print(f"{str(self.id)} is at {str(self.transform.GetPosition())} attacking {str(_prey.id)} at {str(_prey.transform.GetPosition())}")
                    
            return
        if(_prey.transform.GetPosition()[0] > self.transform.GetPosition()[0]):
            self.transform.Translate("Right")
            self.energy -= 1
            print(f"{str(self.id)} is at {str(self.transform.GetPosition())} chasing {str(_prey.id)} at {str(_prey.transform.GetPosition())}")
           
            return
        
        if(_prey.transform.GetPosition()[0] < self.transform.GetPosition()[0]):
            self.transform.Translate("Left")
            self.energy -= 1
            print(f"{str(self.id)} is at {str(self.transform.GetPosition())} chasing {str(_prey.id)} at {str(_prey.transform.GetPosition())}")
            
            return
        
        if(_prey.transform.GetPosition()[1] > self.transform.GetPosition()[1]):
            self.transform.Translate("Forward")
            self.energy -= 1
            print(f"{str(self.id)} is at {str(self.transform.GetPosition())} chasing {str(_prey.id)} at {str(_prey.transform.GetPosition())}")
           
            return
            
        if(_prey.transform.GetPosition()[1] < self.transform.GetPosition()[1]):
            self.transform.Translate("Backward")
            self.energy -= 1
            print(f"{str(self.id)} is at {str(self.transform.GetPosition())} chasing {str(_prey.id)} at {str(_prey.transform.GetPosition())}")
            
            return   
        
if __name__ == "__main__":
    run = bool(True)
    population_size = int(input("Population Size: "))
    speed = int(input("Simulation Speed: "))
    mmax = population_size - 1
    if speed != 0:
        speed = 10/speed
        
    
    population = []
    age = 0 
    for x in range(population_size):
        ani = Animal(x)
        population.append(ani)
        ani.Stats()
    while run:
        print(f"max is {mmax} age is {age}")
        for x in population:
            
            if len(population) <= 1 :
                print(f"{x.id} is the last alive")
                run = False
                break
            
            if x.isAlive:
                x.age = age
                
                prey = population[random.randint(0, mmax)]
                if prey == x:
                    break
                for b in range(x.stepsize):
                    x.Chase(prey)
                    print(f'{x.id} health is at {x.health} and is now at location {x.transform.GetPosition()}')
                sleep(speed)
                
            else:
                mmax -= 1
                population.remove(x)
                print(f'{x.id} removed, {mmax} ')

        age += 1