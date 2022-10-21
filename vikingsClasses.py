
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
         
    vikingArmy=[]
    saxonArmy=[]
    
    
    def addViking(self, Viking = 1):
        self.vikingArmy.append(Viking)
    
    def addSaxon(self, Saxon = 1):
        self.saxonArmy.append(Saxon)
        
    def vikingAttack(self):
        
        attv = random.choice(self.vikingArmy)
            
        atts = random.choice(self.saxonArmy)
        
        resultado = atts.receiveDamage(attv.strength)
        
        if atts.health <= 0:
            
            self.saxonArmy.remove(atts)
            
       


