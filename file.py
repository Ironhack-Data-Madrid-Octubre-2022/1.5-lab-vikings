from vikingsClasses import *

def insertar_vikingos(*args):
    nombre=""
    salud=0
    fuerza=0
    
    guerra=War()
    for e in args:
        print("e es", e)
        for ex in e:
            print("ex es", ex)
            
            for n in ex.keys():
                nombre=ex['name']
                
                salud=ex['health']
                
                fuerza=ex['strength']
                
            
            vikingo=Viking(nombre, salud, fuerza )
            guerra.addViking(vikingo)
            
            print("recorre", [i for i in guerra.vikingArmy])
                
                
                
                
                #vikingo=Viking(n,h)
                #guerra.addViking
            
    
    

            
            

            
        
        
        
        
        

lista=({"name":"Harald", "health":300, "strength":250},
       {"name":"Erik", "health":300, "strength":250},
       {"name":"Gunalf", "health":300, "strength":250},
       {"name":"Grelda", "health":300, "strength":250})

prueba={"name4":"Grelda", "health":300, "strength4":250}

insertar_vikingos(lista)


'''for e in lista:
    for k in e.values():
        print(k)'''
    
    
        
    