from vikingsClasses import *

def insertar_vikingos(*args):
    '''
    Metodo que inserta una lista de vikingos
    
    '''
    
    nombre=""
    salud=0
    fuerza=0
    
    guerra=War()
    for e in args:
        
        for ex in e:
            
            
            for n in ex.keys():
                nombre=ex['name']
                
                salud=ex['health']
                
                fuerza=ex['strength']
                
            
            vikingo=Viking(nombre, salud, fuerza )
            guerra.addViking(vikingo)
            
            print("recorre vikingos", [i for i in guerra.vikingArmy])
    return guerra.vikingArmy
            
            
def insertar_sajones(*args):
    
    '''
    Metodo que inserta una lista de vikingos
    
    '''
    
    salud=0
    fuerza=0
    
    guerra=War()
    for e in args:
        
        for ex in e:
            
            
            for n in ex.keys():
                salud=ex['health']
                
                fuerza=ex['strength']
                
            sajon=Saxon(salud, fuerza)
            guerra.addSaxon(sajon)
            
        
            
    return guerra.saxonArmy
            

def combate(vikingos, sajones, turno):
    
    '''
    Metodo para que combatan dos listas de vikingos y sajones
    
    '''
    guerra=War()
    for v in lista_vikingos:
        guerra.addViking(v)
    for s in lista_sajones:
        guerra.addSaxon(s)
    
    accion=turno
    for v in range(turno):
        print("El turno es", accion)
        if len(guerra.saxonArmy)==0 or len(guerra.vikingArmy)==0:
            return guerra.showStatus()
            
        guerra.vikingAttack()
        if len(guerra.saxonArmy)==0:
            return guerra.showStatus()
        guerra.saxonAttack()
        if len(guerra.vikingArmy)==0:
            return guerra.showStatus()
        print("Ejercito saxon",len(guerra.saxonArmy))
        print("Ejercito viking",len(guerra.vikingArmy))
      
        turno-=1    
        accion-=1
        
    return guerra.showStatus()

#Listas de prueba

vikingos1=({"name":"Harald", "health":300, "strength":500},
       {"name":"Erik", "health":300, "strength":500},
       {"name":"Gunalf", "health":300, "strength":500},
       {"name":"Grelda", "health":300, "strength":500})

sajones1=({ "health":100, "strength":56},
       {"health":300, "strength":250},
       {"health":150, "strength":300},
       { "health":410, "strength":150})


##Insertamos las listas y las cargamos al combate
lista_vikingos=insertar_vikingos(vikingos1)
lista_sajones=insertar_sajones(sajones1)

print(combate(lista_vikingos,lista_sajones,4))



    
        
