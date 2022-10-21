
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
        if self.health > 0: return f'{self.name} has received {damage} points of damage'
        elif self.health <= 0: return f'{self.name} has died in act of combat'

    def battleCry(self):
        return 'Odin Owns You All!'

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        
    def receiveDamage(self,damage):        
        self.health -= damage
        if self.health > 0: return f'A Saxon has received {damage} points of damage'
        elif self.health <= 0: return f'A Saxon has died in combat'
# War

import random

class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
        
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon) 
        
    def vikingAttack(self):
        rand_vik = random.choice(self.vikingArmy)
        rand_sax = random.choice(self.saxonArmy)
        resultado = rand_sax.receiveDamage(rand_vik.strength)
        if rand_sax.health <=0:
            self.saxonArmy.remove(rand_sax)
            
        return resultado
        
        
    def saxonAttack(self):
        rand_vik = random.choice(self.vikingArmy)
        rand_sax = random.choice(self.saxonArmy)
        resultado= rand_vik.receiveDamage(rand_sax.strength)
        if rand_vik.health <=0:
            self.vikingArmy.remove(rand_vik)
            
        return resultado
    
    def showStatus(self):
        if len(self.saxonArmy)==0: return 'Vikings have won the war of the century!'
        elif len(self.vikingArmy)==0: return 'Saxons have fought for their lives and survive another day...'
        else: return 'Vikings and Saxons are still in the thick of battle.'
        