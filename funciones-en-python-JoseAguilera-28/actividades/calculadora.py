"""
Crea un programa que muestre el menú con cinco opciones (del 1 al 5): 
sumar, restar, multiplicar, dividir, y salir. 
El usuario debe poder seleccionar una opción y proporcionar los números necesarios para realizar la operación. 
Muestra el resultado de la operación hasta que se seleccione la opción de salir. 
Evita el uso de variables globales y utiliza funciones para cada operación. 
Evita los errores en la medida de lo posible.

Hecho por Jose Aguilera 
22/10/25
"""

def show_menu():
    print("1. Sumar \n2. Restar \n3. Multiplicar \n4. Dividir \n5. Salir")


def validate_option():
    while True:
            option = input("Introduce una opción del menú: ")
            if option.isdigit():
                option = int(option)
                if option in range(1,6):
                    return option
                else:
                    print("Número fuera del rango.")
            else:
                print("Debes introducir un número.")



def sum(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def split(num1, num2):
    if num2 == 0:
        print("No puedes dividir entre 0.")
    else:
        return num1 / num2


def scape():
    print("Saliendo del programa.")
    exit()


def pide_numero(cadena):
    
    while True:
        string = input(cadena)
        if string.replace(".", "", 1).isnumeric(): 
            return float(string)
        #else:
        print("Solo se pueden introducir números.\n")


def check_string(string1, string2):
    if isinstance(string1, (int, float)) and isinstance(string2, (int, float)):
                num = float(string1)
                num2 = float(string2)
          
    else:
        return None
        #print("Solo se pueden introducir números.\n")
            

def get_numbers():
    a = input("Dame un número: ")

def menu():
    """Aquí ejecuto el programa al completo"""
    while True:
        show_menu() # Muestro el menú de opciones
        option = validate_option() # Pido la entrada de datos

        if option == 5:
            scape()
        
        num1 = pide_numero("Dame el primer número: ")
        num2 = pide_numero("Dame el segundo número: ")




        while False:
            print("-" * 15)
            string1 = input("Introduce el primer número: ").strip()
            string2 = input("Introduce el segundo número: ").strip()
            check_string(string1, string2)
            break

   
        match option: # Selecciono la función de la calculadora
            case 1: 
                print("El resultado es: ", sum(num1, num2))
            case 2: 
                print("El resultado es: ", sub(num1, num2))
            case 3: 
                print("El resultado es: ", multiply(num1, num2))
            case 4: 
                print("El resultado es: ", split(num1, num2))
            case _ :
                print("Opción no válida.")




