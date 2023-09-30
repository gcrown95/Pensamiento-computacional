class persona:

    def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

    def sakyda(self, otra_persona): 
    return f'Hola {otra_persona.nombre}, me llamo {self.nombre}.'

