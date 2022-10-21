from vikingsClasses import *

def insertar_vikingos(*args):
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
    
    salud=0
    fuerza=0
    
    guerra=War()
    for e in args:
        
        for ex in e:
            
            
            for n in ex.keys():
                salud=ex['health']
                print("salud",salud)
                
                fuerza=ex['strength']
                print("fuerza",fuerza)
                
            
            sajon=Saxon(salud, fuerza)
            guerra.addSaxon(sajon)
            
        print("recorre sajones", [i for i in guerra.saxonArmy])
            
    return guerra.saxonArmy
            

def combate(vikingo, sajones, turno):
    guerra=War()
    while(turno!=0):
        
        guerra.vikingAttack()
        guerra.saxonAttack()
        
        turno-=1
        
    return guerra.showStatus()



        
        
        
        

                
                
                
                
                #vikingo=Viking(n,h)
                #guerra.addViking
            
    
    

            
            

            
        
        
        
        
        

vikingos1=({"name":"Harald", "health":300, "strength":250},
       {"name":"Erik", "health":300, "strength":250},
       {"name":"Gunalf", "health":300, "strength":250},
       {"name":"Grelda", "health":300, "strength":250})

sajones1=({ "health":100, "strength":56},
       {"health":300, "strength":250},
       {"health":150, "strength":300},
       { "health":410, "strength":150})



lista_vikingos=insertar_vikingos(vikingos1)
lista_sajones=insertar_sajones(sajones1)

combate(lista_vikingos,lista_sajones,5)




'''for e in lista:
    for k in e.values():
        print(k)'''
    
    
        
