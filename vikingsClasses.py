
# Soldier

import random

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
    def __init__(self):
    
        self.vikingArmy= []
        self.saxonArmy= []        
        
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)    
    
    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
    
    def vikingAttack(self):
        kinguito=random.choice(self.vikingArmy)
        joncito=random.choice(self.saxonArmy)        
        combate=joncito.receiveDamage(kinguito.attack())
        
        if joncito.health<=0:
            self.saxonArmy.remove(joncito)
          
        
        return combate
    
    def saxonAttack(self):
        kinguito=random.choice(self.vikingArmy)
        joncito=random.choice(self.saxonArmy)
        combate=kinguito.receiveDamage(joncito.attack())
        
        if kinguito.health<=0:
            self.vikingArmy.remove(kinguito)
        
        return combate
    
    def showStatus(self):
        if len(self.vikingArmy)>0 and len(self.saxonArmy)>0:
            return "Vikings and Saxons are still in the thick of battle."
        elif len(self.vikingArmy)==0:
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy)==0:
            return "Vikings have won the war of the century!"
                            