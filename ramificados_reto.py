
# # # # Variables de generación
# Usuario uno
name_1= input("Nombre de la primera persona: ")
edad_1= int(input("¿Cuál es la edad de la primera persona?:")) 

# Usuario dos
name_2= input("Nombre de la primera persona: ")
edad_2= int(input("¿Cuál es la edad de la segunda persona?:"))

# Condicionales
if edad_1 > edad_2:
    print(f'{name_1} es mayor que {name_2}')
elif edad_1 < edad_2:
    print(f'{name_1} es menor que {name_2}') 
else:
    print( "Ambas personas tienen la misma edad")