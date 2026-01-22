class CamaraClimatica:
    def __init__(self, temperatura: float, humedad: float):
        self.temperatura = temperatura
        self.humedad = humedad

    def es_segura(self) -> bool:
        """
        Verifica si la cámara está dentro de los rangos permitidos.
        Temp: [0, 10]
        Humedad: [30, 70]
        """
        # Verificamos Temperatura (CE2)
        temp_ok = 0 <= self.temperatura <= 10

        # Verificamos Humedad (CE5)
        humedad_ok = 30 <= self.humedad <= 70

        # Ambas deben ser verdaderas
        return temp_ok and humedad_ok