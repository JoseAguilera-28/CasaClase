import unittest
from camara import CamaraClimatica

class TestCamaraClimatica(unittest.TestCase):



    def test_temp_invalida_baja(self):
        # CE1: Límite inferior inmediato (-0.1 o -1)
        camara = CamaraClimatica(temperatura=-1, humedad=50)
        self.assertFalse(camara.es_segura(), "Falló: -1 grado debería ser inseguro")

    def test_temp_limite_inferior(self):
        # CE2: Límite inferior exacto (0)
        camara = CamaraClimatica(temperatura=0, humedad=50)
        self.assertTrue(camara.es_segura(), "Falló: 0 grados debería ser seguro")

    def test_temp_limite_superior(self):
        # CE2: Límite superior exacto (10)
        camara = CamaraClimatica(temperatura=10, humedad=50)
        self.assertTrue(camara.es_segura(), "Falló: 10 grados debería ser seguro")

    def test_temp_invalida_alta(self):
        # CE3: Límite superior inmediato (10.1 o 11)
        camara = CamaraClimatica(temperatura=11, humedad=50)
        self.assertFalse(camara.es_segura(), "Falló: 11 grados debería ser inseguro")

    # --- PRUEBAS DE HUMEDAD (Manteniendo Temperatura fija en 5 que es válida) ---

    def test_humedad_invalida_baja(self):
        # CE4: Límite inferior inmediato (29)
        camara = CamaraClimatica(temperatura=5, humedad=29)
        self.assertFalse(camara.es_segura(), "Falló: 29% humedad debería ser inseguro")

    def test_humedad_limite_inferior(self):
        # CE5: Límite inferior exacto (30)
        camara = CamaraClimatica(temperatura=5, humedad=30)
        self.assertTrue(camara.es_segura(), "Falló: 30% humedad debería ser seguro")

    def test_humedad_limite_superior(self):
        # CE5: Límite superior exacto (70)
        camara = CamaraClimatica(temperatura=5, humedad=70)
        self.assertTrue(camara.es_segura(), "Falló: 70% humedad debería ser seguro")

    def test_humedad_invalida_alta(self):
        # CE6: Límite superior inmediato (71)
        camara = CamaraClimatica(temperatura=5, humedad=71)
        self.assertFalse(camara.es_segura(), "Falló: 71% humedad debería ser inseguro")


if __name__ == '__main__':
    unittest.main()




# Dominio,      ID Clase,   Tipo,      Límite Inferior,  Límite Superior,  Descripción
# Temperatura,  CE1,        Inválida,  −∞,               <0,               Temperatura demasiado baja
# Temperatura,  CE2,        Válida,    0,                10,               Rango seguro de temperatura
# Temperatura,  CE3,        Inválida,  >10,              +∞,               Temperatura demasiado alta
# Humedad,      CE4,        Inválida,  −∞,               <30,              Humedad demasiado baja
# Humedad,      CE5,        Válida,    30,               70,               Rango seguro de humedad
# Humedad,      CE6,        Inválida,  >70,              +∞,               Humedad demasiado alta




# ID Test,  Variable a Probar,   Valor de Entrada, Valor de la otra variable, Clase Probada,   Resultado Esperado
# T1,       Temperatura,         -1,               50,                        CE1,             False
# T2,       Temperatura,         0,                50,                        CE2,             True
# T3,       Temperatura,         10,               50,                        CE2,             True
# T4,       Temperatura,         11,               50,                        CE3,             False
# T5,       Humedad,             29,               5,                         CE4,             False
# T6,       Humedad,             30,               5,                         CE5,             True
# T7,       Humedad,             70,               5,                         CE5,             True
# T8,       Humedad,             71,               5,                         CE6,             False