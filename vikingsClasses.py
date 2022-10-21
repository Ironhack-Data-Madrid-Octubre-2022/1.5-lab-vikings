
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
    def __init__(self, name, health, strength):
        self.name=name
        self.health=health
        self.strength=strength

    def receiveDamage(self, damage):
        self.health-=damage
        if self.health > 0:
            return self.name+' '+"has received"+' '+str(damage)+' '+"points of damage"
        if self.health < 1:
            return self.name+' '+"has died in act of combat"
           
    def battleCry(self):
        return 'Odin Owns You All!'

    

# Saxon


class Saxon(Soldier):
    def __init__(self,health, strength):
        self.health=health
        self.strength=strength

    
    def receiveDamage(self, damage):
        self.health-=damage
        if self.health > 0:
            return "A Saxon has received"+' '+str(damage)+' '+"points of damage"
        if self.health < 1:
            return "A Saxon has died in combat"
        
    

# War

import random

class War:
    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy=[]

    def addViking(self, Vik):
        Vik= self.vikingArmy.append(Vik)

    def addSaxon(self,Sax):
        Sax=self.saxonArmy.append(Sax)

    def vikingAttack(self):
        v = random.choice(self.vikingArmy)
        s = random.choice(self.saxonArmy)

        hitsax=s.receiveDamage(v.attack())
        if s.health <= 0:
            self.saxonArmy.remove(s)
        return hitsax


    def saxonAttack(self):
        vi = random.choice(self.vikingArmy)
        sa = random.choice(self.saxonArmy)
        hit_vi = vi.receiveDamage(sa.attack())
        if vi.health <= 0 :
            self.vikingArmy.remove(vi)
        return hit_vi
        

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."








        

   
