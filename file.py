from vikingsClasses import *

'''def insertar_vikingos(*args,**kvargs):
    for e in *args:
        for n,h,s in **kvargs.values():
            Viking.name=n
            Viking.health=h
            Viking.strength=s'''
            
        
        
        
        
        

lista=[{"name1":"Harald", "health1":300, "strength1":250},
       {"name2":"Erik", "health2":300, "strength2":250},
       {"name3":"Gunalf", "health3":300, "strength3":250},
       {"name4":"Grelda", "health4":300, "strength4":250}]

for e in lista:
    print(e)
    for k,v in e:
        print(v)
        
    