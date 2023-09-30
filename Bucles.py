# List of elements to iter
animales=["aranas", "perros","gatos", "saltamontes", "osos","leones", "tigres"]
color = ["naranja", "rojo", "verde", "azul","negro"]
# First foor loop
for element in animales:
    print(element)
    
for unit in color:
    print(unit)
    
for unit, element in zip(animales, color):
    print(unit, element)