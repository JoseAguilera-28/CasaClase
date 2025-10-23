[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/fe9UT_pe)
# Funciones en Python
Las funciones son bloques de código reutilizables que realizan una tarea específica. En Python, las funciones se definen utilizando la palabra clave `def`, seguida del nombre de la función y paréntesis que pueden incluir parámetros. Aquí tienes un ejemplo básico:

```python
def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Alice")  # Salida: Hola, Alice!
```
En este ejemplo, hemos definido una función llamada `saludar` que toma un parámetro `nombre` y imprime un saludo personalizado. Luego, llamamos/invocamos a la función pasando el nombre "Alice" como argumento.

Las funciones pueden devolver valores utilizando la palabra clave `return`. Aquí tienes un ejemplo de una función que suma dos números y devuelve el resultado:

```python
def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print(f"El resultado de la suma es: {resultado}")  # Salida: El resultado de la suma es: 8
``` 
En este caso, la función `sumar` toma dos parámetros `a` y `b`, y devuelve su suma. Luego, almacenamos el resultado en la variable `resultado` y lo imprimimos.

En Python, en caso de que una función no tenga una declaración `return`, devolverá automáticamente `None`. Aquí tienes un ejemplo:

```python
def funcion_sin_retorno():
    print("Esta función no devuelve nada.") 
resultado = funcion_sin_retorno()

print(f"El resultado de la función es: {resultado}")  # El resultado será None porque la función no tiene una declaración return
```
En el caso en que se quiera devolver múltiples valores desde una función, se pueden retornar como una tupla. Aquí tienes un ejemplo:

```python
def operaciones(a, b):
    suma = a + b
    resta = a - b
    return suma, resta
resultado_suma, resultado_resta = operaciones(10, 5)
print(f"Suma: {resultado_suma}, Resta: {resultado_resta}")  # Salida: Suma: 15, Resta: 5
```

# Parámetros opcionales con valores por defecto

Hasta ahora hemos visto funciones con parámetros obligatorios o posicionales. Sin embargo, Python también permite definir parámetros opcionales con valores predeterminados. Aquí tienes un ejemplo:

```python
def saludar(nombre, mensaje="¡Hola!"):
    print(f"{mensaje}, {nombre}!")

saludar("Alice")  # Salida: ¡Hola!, Alice!
saludar("Bob", "Buenos días")  # Salida: Buenos días, Bob!
``` 

Pueden mezclarse parámetros obligatorios y opcionales, pero los parámetros opcionales deben ir al final de la lista de parámetros.
Algunas de las normas a tener en cuenta con los parámetros son:
- Los parámetros pueden ser posicionales o con nombre.
- Los parámetros con valores por defecto deben ir al final de la lista de parámetros, tras los parámetros obligatorios o posicionales.
- Los valores por defecto se evalúan en el momento de la definición de la función, no en el momento de la llamada.
- no pueden definirse dos parámetros con el mismo nombre

```python
def saludar(nombre, mensaje="¡Hola!"):
    print(f"{mensaje}, {nombre}!")

saludar("Alice")  # Salida: ¡Hola!, Alice!
saludar("Bob", "Buenos días")  # Salida: Buenos días, Bob!
```
# Parámetros variables

Además, las funciones pueden aceptar un número variable de argumentos utilizando `*args` para argumentos posicionales y `**kwargs` para argumentos con nombre. Aquí tienes un ejemplo:

```python
def mostrar_info(*args, **kwargs):
    print("Argumentos posicionales:")
    for arg in args:
        print(f" - {arg}")
    print("Argumentos con nombre:")
    for key, value in kwargs.items():
        print(f" - {key}: {value}")

mostrar_info("Python", "Java", "JavaScript", lenguaje="Python", version="3.9")
```
En este ejemplo, la función `mostrar_info` puede aceptar cualquier cantidad de argumentos posicionales y con nombre, y los imprime en la consola.


Hay que dejar claro distinta terminología:
- **Definir una función**: Crear una función con un nombre y un bloque de código asociado.
- **Llamar/invocar a una función**: Ejecutar la función utilizando su nombre y proporcionando los argumentos necesarios.
- **Parámetros**: Variables que se definen en la declaración de la función y que reciben los valores cuando se llama a la función.
- **Argumentos**: Valores que se pasan a la función cuando se llama/invoca. Pueden ser posicionales o con nombre.
- **Valor de retorno**: El valor que una función devuelve al finalizar su ejecución, utilizando la palabra clave `return`.
- **Ámbito de las variables**: El contexto en el que una variable es accesible. Las variables definidas dentro de una función tienen un ámbito local y no son accesibles fuera de esa función, a menos que se utilice la palabra clave `global` para declarar una variable global.

# Docstrings
Las Docstrings son cadenas de texto que se utilizan para documentar funciones, clases y módulos en Python. Se colocan justo después de la definición de la función y se encierran entre triples comillas (`"""`). Aquí tienes un ejemplo:

```python
def sumar(a, b):
    """Suma dos números."""
    return a + b

print(sumar.__doc__)  # Salida: Suma dos números.
```
En este ejemplo, la Docstring describe brevemente lo que hace la función `sumar`. Puedes acceder a la Docstring utilizando el atributo `__doc__` de la función. En pycharm, al colocar el cursor sobre el nombre de la función, se mostrará la Docstring como una ayuda emergente. 

Además, las Docstrings deben incluir información más detallada sobre los parámetros y el valor de retorno de la función. Aquí tienes un ejemplo más completo:

```python
def sumar(a, b):
    """Suma dos números.

    Parámetros:
    a (int): El primer número.
    b (int): El segundo número.

    Retorna:
    int: La suma de a y b.
    """
    return a + b
```

# Buenas prácticas
- Usa nombres descriptivos para las funciones y los parámetros.
- El nombre de una función debe ser un verbo que describa la acción que realiza.
- Documenta tus funciones utilizando docstrings para explicar su propósito, parámetros y valor de retorno.
- Evita funciones demasiado largas; divide el código en funciones más pequeñas y manejables.
- Utiliza valores predeterminados para parámetros opcionales cuando sea apropiado.
- Maneja los errores y excepciones dentro de las funciones para mejorar la robustez del código.
- Prueba tus funciones de manera independiente para asegurarte de que funcionan correctamente.

# Listado de ejercicios

Realiza los siguientes ejercicios para practicar la definición y el uso de funciones en Python:
1. Define una función llamada `es_par` que tome un número entero como parámetro y devuelva `True` si el número es par y `False` si es impar. Invócala con diferentes números y muestra los resultados.
2. Crea una función llamada `factorial` que calcule el factorial de un número entero no negativo. Utiliza un bucle para calcular el factorial y devuelve el resultado. Prueba la función con varios valores.
3. Define una función llamada `fibonacci` que genere una lista con los primeros `n` números de la secuencia de Fibonacci. La función debe tomar un parámetro `n` y devolver la lista correspondiente. Invoca la función con diferentes valores de `n` y muestra los resultados.
4. Crea una función llamada `es_palindromo` que verifique si una cadena de texto es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda). La función debe ignorar espacios y mayúsculas/minúsculas. Prueba la función con varias cadenas.
5. Define una función llamada `calcular_area_circulo` que tome el radio de un círculo como parámetro y devuelva el área del círculo utilizando la fórmula `área = π * radio^2`. Utiliza la constante `math.pi` para obtener el valor de π. Invoca la función con diferentes radios y muestra los resultados.
6. Crea una función llamada `contar_vocales` que tome una cadena de texto como parámetro y devuelva el número de vocales presentes en la cadena. La función debe contar tanto vocales mayúsculas como minúsculas. Prueba la función con varias cadenas.
7. Define una función llamada `ordenar_lista` que tome una lista de números como parámetro y devuelva una nueva lista con los números ordenados de menor a mayor. Utiliza el método de ordenación incorporado de Python. Invoca la función con diferentes listas y muestra los resultados.
8. [Crea un programa que muestre el menú con cinco opciones (del 1 al 5): sumar, restar, multiplicar, dividir, y salir. El usuario debe poder seleccionar una opción y proporcionar los números necesarios para realizar la operación. Muestra el resultado de la operación hasta que se seleccione la opción de salir. Evita el uso de variables globales y utiliza funciones para cada operación. Evita los errores en la medida de lo posible.](actividades/calculadora.py)

# De interés
- [Definir funciones](https://docs.python.org/es/3.14/tutorial/controlflow.html#defining-functions)
- [Luis llamas](https://www.luisllamas.es/python-funciones/)
- [argumentos](https://aulasoftwarelibre.github.io/taller-de-python/Python_Avanzado/Argumentos/)
- [keyword-arguments](https://docs.python.org/3.14/tutorial/controlflow.html#keyword-arguments)
