# testear en la consola cargando el archivo que es .py con python delante, es decir, python 1-testsSoldier.py. Previamente conda activate clase
# Soldier


class Soldier:
    
    def __init__(self, health, strength):
        
        self.health=health
        self.strength=strength
        
    def attack(self):
        
        return self.strength
    
    def receiveDamage(self, damage):
        
        self.health -= damage



# Viking

class Viking(Soldier):
    
    def __init__(self, name, health, strength):
        
        self.name=name
        self.health=health
        self.strength=strength
    
    def attack(self):
        
        return self.strength 
    
    def receiveDamage(self, damage):
        
        self.health -= damage
        
        if damage <= self.health:
            return self.name + ' has received ' + str(damage) + ' points of damage'
        else:
            return self.name + ' has died in act of combat'
    
    def battleCry(self):
        return ('Odin Owns You All!')
    
    

# Saxon


class Saxon(Soldier):
    
    def __init__(self, health, strength):
        
        self.health=health
        self.strength=strength
    
    
    def attack(self):
        
        return self.strength     
    
            
    def receiveDamage(self, damage):    
    
        self.health -= damage    
            
            
        if self.health > 0:
            return 'A Saxon has received ' + str(damage) + ' points of damage' 
        else:
            return 'A Saxon has died in combat'

# War

class War():
    
    def __init__(self):
               
        self.vikingArmy=[]
        self.saxonArmy=[]
        
        
    def addViking(self, Viking):
        
        self.Viking=Viking
        self.vikingArmy.append(Viking)
        
    

    def addSaxon(self, Saxon):
        
        self.Saxon=Saxon
        self.saxonArmy.append(Saxon)
        
    def receiveDamage(self, damage):    
    
        self.health -= damage        
        
        
            
    def vikingAttack(self):
        
        Saxon.__init__(self.receiveDamage()) == Viking.__init__(self.strength())
        
        if Saxon.__init__(self.health()) in seslf.saxonArmy == 0 : self.saxonArmy.clear()

        

    
    
    
    def saxonAttack(self):
        
        Viking.__init__(self.receiveDamage()== Saxon.__init__(self.strength())
      
       
        if Vikin.__init__(self.health()) in self.vikingArmy == 0 : self.vikingArmy.clear()

            
    
    
    
    def showStatus(self):
        
        if Viking not in self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        if Saxon not in self.saxonArmy:
            return "Vikings have won the war of the century!"
        if Viking in self.vikingArmy and self.saxonArmy:
            return "Vikings and Saxons are still in the thick of battle."
    
    
    
    
    
    
    
    
