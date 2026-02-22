import re

class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__empleados = {}

    @property
    def nombre(self): return self.__nombre
    
    @nombre.setter
    def nombre(self, valor):
        if not re.match(r"^[a-zA-Z\s]+$", valor):
            raise ValueError("Nombre de empresa inválido.")
        self.__nombre = valor

    def agregar_empleado(self, empleado):
        from excepciones import IDDuplicadoError
        if empleado.id_emp in self.__empleados:
            raise IDDuplicadoError(f"El empleado '{empleado.id_emp}' ya existe")
        self.__empleados[empleado.id_emp] = empleado

    def total_nomina(self):
        return sum(e.calcular_salario() for e in self.__empleados.values())

    def __str__(self):
        subrayado = "-" * 30
        res = f"\n{subrayado}\nEmpresa: {self.nombre}\n{subrayado}\n"
        for emp in self.__empleados.values():
            res += str(emp) + "\n"
        
        total_f = f"${self.total_nomina():,.0f}".replace(",", ".")
        res += f"Coste total en nóminas: {total_f}"
        return res