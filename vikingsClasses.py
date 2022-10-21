
# Soldier


class Soldier:
    def __init__(self,health,strength):
        self.health=health
        self.strength=strength
    def attack(self):
        return self.strength
    def receiveDamage(self,damage):
        self.health-=damage
    

# Viking


class Viking(Soldier):
    def __init__(self,name,health,strength):
        self.name=name
        self.health=health
        self.strength=strength
    def receiveDamage(self,damage):
        self.health -= damage
        if self.health > 0:
            return (str(self.name) + " has received " + str(damage) + " points of damage")
        else:
            return (str(self.name) + " has died in act of combat")
    def battleCry(self):
        return "Odin Owns You All!"
        
        
    

# Saxon


class Saxon(Soldier):
    def __init__(self,health,strength):
        self.health=health
        self.strength=strength
    def receiveDamage(self,damage):
        self.health -= damage
        if self.health > 0:
            return ("A Saxon has received " + str(damage) + " points of damage")
        else:
            return ("A Saxon has died in combat")

# War

import random

class War:
    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy=[]
    def addViking(self, Viking=1):
        self.vikingArmy.append(Viking)
    def addSaxon(self, Saxon=1):
        self.saxonArmy.append(Saxon)
    def vikingAttack(self):
        
        attv = random.choice(self.vikingArmy)
        atts = random.choice(self.saxonArmy)
        resultado = atts.receiveDamage(attv.strength)
        
        if atts.health <=0:
            self.saxonArmy.remove(atts)
            return resultado
    def saxonAttack(self):
        
        attv = random.choice(self.vikingArmy)
        atts = random.choice(self.saxonArmy)
        resultado = attv.receiveDamage(atts.strength)
        
        if attv.health <= 0:
            self.vikingArmy.remove(attv)
        return resultado
    
    def showStatus(self):
        
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        if not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        if len(self.saxonArmy) >= 1 and len(self.vikingArmy) >= 1:
            return "Vikings and Saxons are still in the thick of battle."
            
    
