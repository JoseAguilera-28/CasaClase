import unittest


class Persona:
    def __init__(self, edad: int):
        self.edad = edad

    def is_mayor_de_edad(self) -> bool:
        assert self.edad >= 0, "La edad no puede ser negativa"
        return self.edad >= 18


class TestPersona(unittest.TestCase):

    def test_edad_negativa_error(self):
        casos_error = [-1, -100]

        for valor in casos_error:
            p = Persona(valor)
            with self.assertRaises(AssertionError):
                p.is_mayor_de_edad()

    def test_es_menor_de_edad(self):
        casos_false = [0, 17]

        for valor in casos_false:
            p = Persona(valor)
            resultado = p.is_mayor_de_edad()
            self.assertFalse(resultado, f"Falló con edad: {valor}")

    def test_es_mayor_de_edad(self):
        casos_true = [18, 100]

        for valor in casos_true:
            p = Persona(valor)
            resultado = p.is_mayor_de_edad()
            self.assertTrue(resultado, f"Falló con edad: {valor}")


if __name__ == '__main__':
    unittest.main()




# ESTA ES LA TABLA DE VALORES LÍMITE


#    ID	     Valor de Entrada (edad)   Tipo de Prueba	                       Salida Esperada
#    1	       -1	                   (Inválido inferior inmediato)	       ERROR (AssertionError)
#    2	       -100	                   (Clase inválida)                        ERROR (AssertionError)
#    3	        0	                   (Límite inferior absoluto)	           False
#    4	        17	                   (Límite superior de "menor")	           False
#    5	        18	                   (Límite inferior de "mayor")	           True
#    6	        100                    (Clase válida)	                       True



# ESTA ES LA TABLA DE EQUIVALENCIAS


#    ID Clase	   Descripción del Rango	             Tipo de Clase	        Resultado Esperado
#    CE1	       edad < 0 (Números negativos)	         Inválida	            ERROR (AssertionError)
#    CE2	       0 <= edad <= 17 (Entre 0 y 17 años)	 Válida	                False
#    CE3	       edad >= 18 (De 18 años en adelante)	 Válida	                True