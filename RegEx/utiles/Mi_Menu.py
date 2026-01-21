from utiles.Mi_Menu_Error import MenuError

class Menu:

    def __init__(self, titulo, opciones):
        self.set_opciones(opciones)
        self.__titulo = titulo

    def set_opciones(self, opciones):
        if not isinstance(opciones, list):
            raise MenuError("Error: pasa una lista de opciones")
        self.__opciones = opciones

    def __str__(self):
        return f'{self.__titulo}: {self.__opciones}'

    def show(self):
        """
        Muestro el menú y devuelvo la opción elegida por el usuario desde el teclado
        """

        cadena = ""
        contador = 1
        for opcion in self.__opciones:
            cadena += f"{contador}. {opcion}\n"
            contador += 1
        cadena += f"{contador}. Salir"
        print(f"""\
\n\n\n
------------------------------------------
{self.__titulo}: 
------------------------------------------
{cadena}
------------------------------------------
""")
        return self.opcion_valida()

    def opcion_valida(self):
        while True:
            try:
                opcion = int(input(f"Dame una opción válida: (1..{len(self.__opciones) + 1}): "))
                if opcion > 0 and opcion <= len(self.__opciones):
                    return opcion
                print("Error. Intoduce una opción válida: ")
            except ValueError as ve:
                print("Error. Intoduce un entero. ")


if __name__ == '__main__':
    # Esto es solo para comprobar si funciona el menú
    m = Menu("Ascensor", ["Crear Ascensor", "Viajar"])
    print(m)



# m = Menu("Ascensor", ["Crear Ascensor", "Viajar"])
# print(m)
#
# while True:
#     opcion = m.show()
#     if opcion == 1:
#         print("opción primera")
#     elif opcion == 2:
#         print("opción segundo")
#     else:  # opcion ==3: Salirrrrrrrrrrrrrrrrrrrrrr
#         print("Adiós")
#         break
