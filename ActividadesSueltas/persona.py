class Persona:
    def __init__(self, edad):
        if edad < 0:
            raise ValueError("Error: La edad no puede ser negativa")
        self.edad = edad

    def isMayorDeEdad(self):
        return self.edad >= 18