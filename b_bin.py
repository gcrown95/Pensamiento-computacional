objetivo = int(input("Escoge un numero: "))
epsilon = 0.00001
bajo = 0.0
alto = max(1.0, objetivo)
respuesta = (alto + bajo) / 2

while abs (respuesta**2 - objetivo) >=  epsilon:
    print(f"Bajo = {bajo}, alto= {alto}, respuestas= {respuesta}")
    if respuesta**2 < objetivo:
        bajo = respuesta
    else:
        alto = respuesta
    
    respuesta = (alto + bajo) / 2
    print(f"Raiz cuadrada {respuesta}")