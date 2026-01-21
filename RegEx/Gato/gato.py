# Continuando con la POO Crea una clase Gato.  Cada gato tendrá:
#
# - un nombre (comprueba mediante regex)
# - una fecha de nacimiento (comprueba mediante regex)
# - una raza (comprueba mediante regex)
# - un peso (1-15).
#
# El comportamiento es el siguiente:
#
# - Cuando el gato juega pierde peso
# - Cuando el gato come gana peso
# - El gato puede morir de inanición o por sobrepeso.
# - Si el gato está muerto no puede ni jugar ni comer
# - Calcula la edad del gato. Investiga los módulos de python que lo calculan
#
# En tu diseño ten en cuenta lo siguiente y, en caso de existir, referencia en enlaces y añade código:
# - El estado del gato debe ser privado
# - Crea todos los getters y setters de los atributos
# - Los atributos y métodos que no son de instancia.
# - Crea una excepción y lánzala en el constructor en caso de ser necesario

from utiles.Mi_Menu import Menu

CAMADA_GATOS = []

class Gato:
    def __init__(self, nombre, fecha_nacimiento, raza, peso):
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.raza = raza
        self.peso = peso
        self.PESO_MAXIMO = 15
        self.PESO_MINIMO = 1

    def jugar(self):
        print("El gato está jugando!, ha encontrado tu ovillo de lana.")
        nuevo_peso = 1
        self.peso = self.peso - nuevo_peso
        return self.peso

    def comer(self):
        print("El gato está comiendo!, come un trozo de comida que cayó al suelo.")
        nuevo_peso = 1
        self.peso = self.peso + nuevo_peso
        return self.peso

    def gato_muerto(self, causa):
        print(f"El gato ha muerto por {causa}")

    def main(self):
        while True:
            introduccion = ("Esté es el menú de los gatos!")
            print((len(introduccion) * "-"))
            print(Menu(titulo= "Esté es el menú de los gatos!", opciones= [
            "1. Añadir un gato a la camada",
            '2. Dar de comer al gato',
            "3. Jugar con el gato",
            "4. Información de la camada"
            ]))
            print((len(introduccion) * "-"))
            print("Que quieres hacer?")
            print((len(introduccion) * "-"))

            try:
                opcion = int(input("Introduce una opción válida del menú: "))
                if opcion == 1:
                    if self.PESO_MINIMO <= self.peso <= self.PESO_MAXIMO:
                        print(
                            f"El gato {self.nombre} de raza {self.raza} pesa {self.peso} kilos, nació el {self.fecha_nacimiento} y está muy feliz.")
                    elif self.PESO_MINIMO <= G1.peso:
                        self.gato_muerto(causa="sobrepeso")
                        break
                    else:
                        self.gato_muerto(causa="inanición")
                        break
                if opcion == 2:
                    self.comer()
                if opcion == 3:
                    self.jugar()
            except ValueError:
                print("ERROR: Por favor, introduce un número válido")

if __name__ ==  "__main__":
    G1 = Gato(nombre="Arquímedes", fecha_nacimiento="27/7/2007", raza="Griega", peso=4)
    G1.main()