
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength
        
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health-=damage
    
        
# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):  
        self.health=health
        self.strength=strength
        self.name=name
        
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:            
            return self.name + ' has received ' + str(damage) + ' points of damage'
        else:
            return self.name + ' has died in act of combat'             


    def battleCry(self):
        battleCry=('Odin Owns You All!')
        return battleCry
# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength
    
    def receiveDamage(self,damage):
        self.health-=damage
        if self.health > 0:
            return 'A Saxon has received ' + str(damage) + ' points of damage'
        else:
            return 'A Saxon has died in combat'

# War


class War:
    
    vikingArmy=[]
    saxonArmy=[]
    
    def addViking(Viking):
        Viking.__init__(self, name, health, strength)
            if len(vikingArmy) < 10:
                vikingArmy.append(Viking)
        
        
            
