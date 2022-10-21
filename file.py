from vikingsClasses import *

def insertar_vikingos(*args,**kvargs):
    guerra=War()
    for e in args:
        print("e es", e)
        for ex in e:
            print("ex es", ex)
            '''for n,h,s in ex.items():
                print("n es",n)
                print(h)
                print(s)
                vikingo=Viking(n,h,s)
                guerra.addViking'''
            
    print(guerra.vikingArmy)
    

            
            

            
        
        
        
        
        

lista=({"name1":"Harald", "health1":300, "strength1":250},
       {"name2":"Erik", "health2":300, "strength2":250},
       {"name3":"Gunalf", "health3":300, "strength3":250},
       {"name4":"Grelda", "health4":300, "strength4":250})

prueba={"name4":"Grelda", "health4":300, "strength4":250}

insertar_vikingos(lista)


'''for e in lista:
    for k,v in e.items():
        print(k,v)'''
    
    
        
    