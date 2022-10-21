
# Soldier


class Soldier:
    

    def __init__(self,health,strength):
        
        self.health = health
        
        self.strength = strength
        
    def attack(self):
        
        return self.strength
    
    def receiveDamage(self,damage):
        
        self.health -= damage



# Viking

class Viking(Soldier):     #las hijas se ponen dentro en los parentesis
    
    def __init__(self, name, health, strength):
        
        self.name=name
        
        self.health=health
        
        self.strength=strength
        
    def receiveDamage(self, damage):
        
        self.health -= damage
 
        if self.health > 0:
            
            return (str(self.name) + " has received " + str(damage) + " points of damage")
        
        else:
            
            return (str(self.name) + " has died in act of combat")
        
    def battleCry(self):
        
        return "Odin Owns You All!"


       
# Saxon


class Saxon(Soldier):

    def __init__ (self, health, strength):
        
        self.health=health
        
        self.strength=strength
      
    def receiveDamage(self, damage):
       
        self.health -= damage
        
        if self.health > 0:
            
            return ("A Saxon has received " + str(damage) + " points of damage")
        
        else:
            
            return ("A Saxon has died in combat")

# War

class War:
    
    def __init__ (self, health, strength):
            
            self.VikingArmy = []
            self.saxonArmy = []
            
    def  addViking(self,Viking):
            self.VikingArmy = 1
    
    def addSaxon (self, Saxon):
            self.SaxonArmy = 1
            
    def VirkinAttack(self):
        self.receiveDamage = 1
        
    
    


