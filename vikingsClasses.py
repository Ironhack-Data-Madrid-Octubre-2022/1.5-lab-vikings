
# Soldier


class Soldier:
    
    def __init__(self,health,strength):
        
        self.health = health
        self.strength = strength
        
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health -= damage 

# Viking


class Viking(Soldier):
    
    def __init__(self,name,health,strenght):
        
        Soldier.__init__(self,health,strenght)
        
        self.name = name
    
    
    
    def receiveDamage(self,damage):
        self.health -= damage
        if self.health >0:
            result = self.name + ' has received ' + str(damage) + ' points of damage'
            return result
        else:
            result = self.name +  ' has died in act of combat'
            return result
       
    def battleCry(self):
        cry = "Odin Owns You All!"
        return cry
    
# Saxon


class Saxon(Soldier):
    
    def __init__(self,health,strenght):
        
        Soldier.__init__(self,health,strenght)
        
    def receiveDamage(self,damage):
        self.health -= damage
        if self.health >0:
            result = "A Saxon has received " +str(damage)+ " points of damage"
            return result
        else:
            result = 'A Saxon has died in combat'
            return result 
    
    
    

# War


class War:
    
    def __init__(self):
        
        
    vikingArmy = []
    saxonArmy = []
    
    def addViking(self,viking):
        vikingArmy.append(viking)
    
    
    def addSaxon(self,saxon):
        saxonArmy.append(saxon)
    
    
    def vikingAttack()
    
    
    def saxonAttack()
    
    
    def showStatus()
    
    
    
    
    
    
    
    
