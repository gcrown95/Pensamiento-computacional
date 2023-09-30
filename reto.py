
elec_met= int(input(f"""Bienvenido al simulador de obtencion de valores de una raiz cuadrada. Aca tienes acceso a tres posibles metodos, por favor selecciona uno:
1. Busqueda Binaria
2. Enumeracion exhaustiva
3. Aproximacion
Escoge un metodo: """))
if elec_met==1:
    print("Escogiste el metodo de busqueda binaria")
    objetivo = int(input("Escoge un numero: "))
    epsilon = 0.00001
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2
elif elec_met==2:
    print("Escogiste el metodo de enumeraciones")
    objetivo=int(input("Escoge un numero entero: "))
    respuesta=0
    while respuesta**2<objetivo:
        print(respuesta)
        respuesta=+1
    if respuesta**2 == objetivo:
        print(f"La raiz cuadrada de {objetivo} es {respuesta}")
    else:
        print(f"{objetivo} no tiene una raiz cuadrada")
elif elec_met==3: 
    print("Escogiste el metodo por aproximacion")
    objetivo = int(input("Escoge un numero: "))
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0
    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(abs(respuesta**2 - objetivo), respuesta)
        respuesta += paso
    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f"No se encontro la raiz cuadrada del {objetivo}")
    else:
        print(f"La raiz cuadrada de {objetivo} es {respuesta}")
else: 
    print(F"Por favor, escoja entre 1,2 o 3")
        