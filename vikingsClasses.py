
# Soldier
import random

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        #self.health = health
        #self.strength = strength
        Soldier.__init__(self, health, strength)
    
    def receiveDamage(self, damage):
        self.health -= damage
        
        if self.health <= 0:
            return self.name + ' has died in act of combat'
        elif self.health > 0:
            return self.name + ' has received ' + str(damage) + ' points of damage'
            
    def battleCry(self):
        return "Odin Owns You All!"

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        Soldier.__init__(self, health, strength)
        
    def receiveDamage(self, damage):
        self.health -= damage
        
        if self.health <= 0:
            return 'A Saxon has died in combat'
        elif self.health > 0:
            return 'A Saxon has received ' + str(damage) + ' points of damage'

# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
        
    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
        
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
        
    def vikingAttack(self):
        atts = random.choice(self.saxonArmy)
        attv = random.choice(self.vikingArmy)
        resultado = atts.receiveDamage(attv.strength)
        if atts.health <= 0:
            self.saxonArmy.remove(atts)
        return resultado
    
    def saxonAttack(self):
        atts = random.choice(self.saxonArmy)
        attv = random.choice(self.vikingArmy)
        resultado = attv.receiveDamage(atts.strength)
        if attv.health <= 0:
            self.vikingArmy.remove(attv)
        return resultado
    
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
