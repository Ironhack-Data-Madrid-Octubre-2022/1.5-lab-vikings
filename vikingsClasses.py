
# Soldier
import random

class Soldier:
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength
    def attack(self):
        return self.strength
    def receiveDamage(self, damage):
        self.health=self.health-damage



class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name=name
        self.health=health
        self.strength=strength
    def attack(self):
        return self.strength
    def receiveDamage(self, damage):
        self.health=self.health-damage
        if self.health > 0:
            return str(self.name) + " has received " + str(damage) + " points of damage"
        else:
            return str(self.name) + " has died in act of combat"
    def battleCry(self):
        return "Odin Owns You All!"

class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength
    def attack(self):
        return self.strength
    def receiveDamage(self, damage):
        self.health=self.health-damage
        if self.health > 0:
            return "A Saxon has received " + str(damage) + " points of damage"
        else:
            return "A Saxon has died in combat"



class War:
    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy=[]
    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
    def vikingAttack(self):
        str = ""
        indV = random.randint(0, len(self.vikingArmy)-1)
        indS = random.randint(0, len(self.saxonArmy)-1)
        str = self.saxonArmy[indS].receiveDamage(self.vikingArmy[indV].strength)
        if self.saxonArmy[indS].health <= 0:
            self.saxonArmy.pop(indS)
        return str
    def saxonAttack(self):
        str = ""
        indV = random.randint(0,len(self.vikingArmy)-1)
        indS = random.randint(0,len(self.saxonArmy)-1)
        str = self.vikingArmy[indV].receiveDamage(self.saxonArmy[indS].strength)
        if self.vikingArmy[indV].health <= 0:
            self.vikingArmy.pop(indV)
        return str
    def showStatus(self):
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        if not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        if (len(self.saxonArmy) != 0) & (len(self.vikingArmy) != 0):
            return "Vikings and Saxons are still in the thick of battle."