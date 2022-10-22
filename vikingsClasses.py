
# Soldier


class Soldier:
    
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        
    def attack(self):
        return self.strength
    
    def receiveDamage(self,damage):
        self.health -= damage        

# Viking


class Viking(Soldier):
    
    def __init__(self, name, health, strength):
        
        Soldier.__init__(self, health, strength)
        
        self.name = name
        
    def receiveDamage(self,damage):
        self.health -= damage
        
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return self.name + ' has died in act of combat'
    
    def battleCry(self):
        return 'Odin Owns You All!'
        

# Saxon


class Saxon(Soldier):
        
        def receiveDamage(self,damage):
            self.health -= damage
            
            if self.health > 0:
                return f"A Saxon has received {damage} points of damage"
            
            else:
                return "A Saxon has died in combat"

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
        import random
        sajon = random.choice(self.saxonArmy)
        vikingo = random.choice(self.saxonArmy)
        
        sajon = Saxon(Viking.strength)#strengthviking
        viking = Viking(Saxon.strength)#strengthsajon
        
        #En python, a los atributos se accede con la sintaxis objeto.atributo y a los métodos con objeto.metodo().
                   
                   

        
        sajon.receiveDamage(self,damage)
        
        
        
        
        
        
        self.vikingArmy.pop()
        return receiveDamage(self,damage)
        
    def saxonAttack(self):
        damage == strength
        self.saxonArmy.pop()
        return receiveDamage(self,damage)
        
    def showStatus():
        
        
        if self.saxonArmy(len) == 0:
            return "Vikings have won the war of the century!"
        elif self.vikingArmy(len) == 0:
            return "Saxons have fought for their lives and survive another day..."
        elif self.saxonArmy(len) != 0 and self.vikingArmy(len) != 0:
            return "Vikings and Saxons are still in the thick of battle."
        
            




