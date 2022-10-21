import random
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


class Viking(Soldier):
    
    def __init__(self, name, health, strength):
        
        self.name = name
        self.health = health
        self.strength = strength
        
    
    def receiveDamage(self,damage):
        
        self.health -= damage
        
        if self.health > 0:
            return f'{self.name} has received {damage} points of damage'
        
        elif self.health <= 0:
            return f'{self.name} has died in act of combat'
        
        
    def battleCry(self):
        
        return 'Odin Owns You All!'
               

# Saxon


class Saxon(Soldier):
    
    
    def __init__(self, health, strength):

        self.health = health
        self.strength = strength
        
    def receiveDamage(self,damage):
        
        self.health -= damage
        
        if self.health > 0:
            return f'A Saxon has received {damage} points of damage'
        
        elif self.health <= 0:
            return 'A Saxon has died in combat'
    

# War


class War:

    
    def __init__(self):
        
        self.vikingArmy=[]
        self.saxonArmy=[]
           
    
    def addViking(self,Viking):
        
        self.vikingArmy.append(Viking)
        
        
    def addSaxon(self, Saxon):
        
        self.saxonArmy.append(Saxon)
        
    def vikingAttack(self):
        
        vikingo=random.choice(self.vikingArmy)
        sajon=random.choice(self.saxonArmy)
        
        ataque=sajon.receiveDamage(vikingo.strength)
        
        if sajon.health <= 0:
            
            self.saxonArmy.remove(sajon)
            
        return ataque
    
    def saxonAttack(self):
        
        vikingo=random.choice(self.vikingArmy)
        sajon=random.choice(self.saxonArmy)
        
        ataque=vikingo.receiveDamage(sajon.strength)
        
        if vikingo.health <= 0:
            
            self.vikingArmy.remove(vikingo)
            
        return ataque
    
    def showStatus(self):
        
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        
        elif len(self.saxonArmy) >= 1 and len(self.saxonArmy) >= 1:
            return "Vikings and Saxons are still in the thick of battle."


    
            
       
       
        
        
        
        
        
    
    
