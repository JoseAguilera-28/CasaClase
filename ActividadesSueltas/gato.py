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

ORDA_GATOS = []

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

    def show_menu(self):
        print("""
        1. Información del gato
        2. Dar de comer al gato
        3. Jugar con el gato
        """)

    def main(self):
        while True:
            introduccion = ("Esté es el menú de los gatos!")
            print((len(introduccion)*"-"))
            print(introduccion)
            print((len(introduccion)*"-"))
            print("Que quieres hacer?")
            print(self.show_menu())
            try:
                opcion = int(input("Introduce una opción válida del menú: "))
                if opcion == 1:
                    if self.PESO_MINIMO <= G1.peso <= self.PESO_MAXIMO:
                        print(
                            f"El gato {G1.nombre} de raza {G1.raza} pesa {G1.peso} kilos, nació el {G1.fecha_nacimiento} y está muy feliz.")
                        break
                    elif self.PESO_MINIMO <= G1.peso:
                        return self.gato_muerto(causa="sobrepeso")
                    else:
                        return self.gato_muerto(causa="inanición")
                if opcion == 2:
                    self.comer()
                if opcion == 3:
                    self.jugar()
            except:
                raise ValueError("Por favor, introduce un número válido")







if __name__ ==  "__main__":
    G1 = Gato(nombre="Arquímedes", fecha_nacimiento="27/7/2007", raza="Griega", peso=4)
    G1.main()