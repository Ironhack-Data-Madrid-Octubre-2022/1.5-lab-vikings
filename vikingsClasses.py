
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
    
    def __init__(self,name,health,strength):
        
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
    
        return "Odin Owns You All!"

# Saxon

class Saxon(Soldier):
    
    def __init__(self,health,strength):
        
        self.health = health
        self.strength = strength
        
    def receiveDamage(self,damage):
        
        self.health -= damage
        
        if self.health > 0:
            return f'A Saxon has received {damage} points of damage'
        elif self.health <= 0:
            return f'A Saxon has died in combat'

# War
class war:
    
    vikingArmy = []
    saxonArmy = []
    
    def addViking(self, Viking):
        
        vikingArmy.append(Viking)
        
    def addSaxon(self, Saxon)
    
        saxonArmy.append(saxon)
        
    def vikingAttack()

