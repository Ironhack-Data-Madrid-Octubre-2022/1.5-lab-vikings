
# Soldier
import random

class Soldier:
    def __init__(self, health, strength):
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
        
    def receiveDamage(self,damage):
        self.health-=damage
        print("Vida1", self.health)
        if self.health>0:
            return f"{self.name} has received {damage} points of damage"
        if self.health<=0:
            return f"{self.name} has died in act of combat"
        
    def battleCry(self):
        return "Odin Owns You All!"

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength
        
    def receiveDamage(self, damage):
        self.health-=damage
        
        if self.health>0:
            return f"A Saxon has received {damage} points of damage"
        if self.health<=0:
            return "A Saxon has died in combat"
        
        

# War


class War:
    
    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy=[]
        
    def addViking(self, Viking ):
        self.vikingArmy.append(Viking)
        print("lista vikinga", self.vikingArmy)
        
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
        print("lista sajona", self.saxonArmy)
        
    def prueba(self):
        sajon=self.saxonArmy[0]
        print(sajon)
    def vikingAttack(self):
        sajon=self.saxonArmy[0]
        vikingo=self.vikingArmy[0]
        print("vikingo",type(vikingo))
        print("sajon" ,type(sajon))
        resultado_atk=sajon.receiveDamage(vikingo.attack())
        if sajon.health<=0:
            self.saxonArmy.pop()
        
        return resultado_atk
        
    
    def saxonAttack(self):
        
        sajon=self.saxonArmy[0]
        vikingo=self.vikingArmy[0]
        print("vikingo",type(vikingo))
        print("sajon" ,type(sajon))
        resultado_atk=vikingo.receiveDamage(sajon.attack())
        if vikingo.health<=0:
            self.vikingArmy.pop()
        
        return resultado_atk
    
    def showStatus(self):
        if len(self.saxonArmy)==0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy)==0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
        
    
        
Erik=Viking('HArald', 300,150) 
Arnulf=Saxon(60,25)  
Combate=War()   
Combate.addSaxon(Arnulf)
Combate.addViking(Erik)

#print("Daño recibido",Erik.receiveDamage(25))
#Combate.prueba()

Combate.showStatus()

#print(Combate.vikingAttack())
print(Combate.saxonAttack())

Combate.showStatus()


