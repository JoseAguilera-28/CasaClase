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
import re

CAMADA_GATOS = []

class Gato:
    def __init__(self, nombre, fecha_nacimiento, raza, peso):
        self.__nombre = nombre
        self.__fecha_nacimiento = fecha_nacimiento
        self.__raza = raza
        self.__peso = peso
        self.PESO_MAXIMO = 15
        self.PESO_MINIMO = 1

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def fecha_nacimiento(self):
        return self.__fecha_nacimiento


    @fecha_nacimiento.setter
    def fecha_nacimiento(self, fecha_nacimiento):
        self.__fecha_nacimiento = fecha_nacimiento

    @property
    def raza(self):
        return self.__raza

    @raza.setter
    def raza(self, raza):
        self.__raza = raza

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, peso):
        self.__peso = peso

    # def add(self, lista):
    #     lista.append(self)
    #     print(f"{self.nombre} ha sido añadido a la lista.")

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

    @staticmethod
    def indice_gatos():
        print("-" * 15)
        for indice, gatos in enumerate(CAMADA_GATOS):
            print(indice, gatos)
        print("-" * 15)

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
                    print("Añadiendo a un nuevo integrante a la camada")
                    # Validación de Nombre
                    while True:
                        nombre_gato_nuevo = input("Nombre del gato: ")
                        if re.match(r"^[A-Z][a-z]+$", nombre_gato_nuevo):
                            break
                        print("Formato incorrecto. Debe empezar por mayúscula y contener solo letras.")

                    # Validación de Fecha
                    while True:
                        fecha_gato_nuevo = input("Fecha de nacimiento (DD/MM/AAAA): ")
                        # Regex sencilla para fecha
                        if re.match(r"^\d{2}/\d{2}/\d{4}$", fecha_gato_nuevo):
                            break
                        print("Formato incorrecto. Usa DD/MM/AAAA")

                    # Validación de Raza
                    while True:
                        raza_gato_nuevo = input("Raza del gato: ")
                        if re.match(r"^[A-Z][a-z]+$", raza_gato_nuevo):
                            break
                        print("La raza solo debe contener letras.")

                    # Validación de Peso
                    while True:
                        try:
                            peso_gato_nuevo = float(input("Peso actual (1-15 kg): "))
                            if self.PESO_MINIMO <= peso_gato_nuevo <= self.PESO_MAXIMO:
                                break
                            print(f"El peso debe estar entre {self.PESO_MINIMO} y {self.PESO_MAXIMO} kg.")
                        except ValueError:
                            print("Introduce un número válido.")

                    # añado el gato a la camada si todo está correcto
                    try:
                        nuevo_gato = Gato(nombre= nombre_gato_nuevo, fecha_nacimiento= fecha_gato_nuevo, raza= raza_gato_nuevo, peso= peso_gato_nuevo)
                        CAMADA_GATOS.append(nuevo_gato)
                        print(f"{nuevo_gato.nombre} ha sido añadido a la camada, se ve muy feliz con su nueva familia!")
                    except Exception as e:
                        print(f"Ocurrió un error al crear el gato: {e}")




                if opcion == 2:
                    print("Vas a dar de comer a un gato!")
                    print(self.indice_gatos())
                    int(input("Introduce el índice del gato al que vas a dar de "))


                if opcion == 3:
                    self.jugar()
                if opcion == 4:
                    if self.PESO_MINIMO <= self.peso <= self.PESO_MAXIMO:
                        for _ in CAMADA_GATOS:
                            print(
                                f"El gato {self.nombre} de raza {self.raza} pesa {self.peso} kilos, nació el "
                                f"{self.__fecha_nacimiento} y está muy feliz.")
                    elif self.PESO_MINIMO <= G1.peso:
                        self.gato_muerto(causa="sobrepeso")
                        break
                    else:
                        self.gato_muerto(causa="inanición")
                        break
            except ValueError:
                print("ERROR: Por favor, introduce un número válido")

if __name__ ==  "__main__":
    G1 = Gato(nombre="Arquímedes", fecha_nacimiento="27/7/2007", raza="Griega", peso=4)
    CAMADA_GATOS.append(G1)
    G1.main()


    # variable = GATO
    # variable.comer