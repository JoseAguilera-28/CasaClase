import re
from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, id_emp, nombre, apellidos, salario_base, nombre_empresa):
        self.id_emp = id_emp 
        self.nombre = nombre
        self.apellidos = apellidos
        self.salario_base = salario_base
        self.__correo = self.genera_correo(nombre_empresa)

    @property
    def id_emp(self): return self.__id_emp

    @id_emp.setter
    def id_emp(self, valor):
        if not re.match(r"^[JQE]\d{2}$", valor):
            raise ValueError(f"ID {valor} no válido.")
        self.__id_emp = valor

    @property
    def nombre(self): return self.__nombre
    @nombre.setter
    def nombre(self, v): self.__nombre = v

    @property
    def apellidos(self): return self.__apellidos
    @apellidos.setter
    def apellidos(self, v): self.__apellidos = v

    @property
    def salario_base(self): return self.__salario_base
    @salario_base.setter
    def salario_base(self, v): self.__salario_base = float(v)

    def genera_correo(self, empresa_nombre):
        dominio = empresa_nombre.replace(" ", "").lower()
        pre = (self.apellidos[:2] + self.nombre[0] + self.id_emp).lower()
        pre = pre.translate(str.maketrans("áéíóúñ", "aeioun"))
        return f"{pre}@{dominio}.com"

    def calcular_salario(self):
        return self.salario_base

    def __str__(self):
        nom_f = f"{self.nombre:^15}"
        ape_f = f"{self.apellidos:^20}"
        sal_f = f"{self.calcular_salario():,.0f}€".replace(",", ".")
        return f"{self.id_emp}  {self.__correo:<30} {nom_f} {ape_f} {sal_f}"

class QA(Empleado):
    def __init__(self, id_emp, nombre, apellidos, salario, empresa, especialidad):
        super().__init__(id_emp, nombre, apellidos, salario, empresa)
        self.especialidad = especialidad

    def __str__(self):
        return f"{super().__str__()} {self.especialidad}"

class JefeProyecto(Empleado):
    def __init__(self, id_emp, nombre, apellidos, salario, empresa, bono):
        super().__init__(id_emp, nombre, apellidos, salario, empresa)
        self.bono = float(bono)

    def calcular_salario(self):
        return super().calcular_salario() + self.bono

    def __str__(self):
        bono_f = f"{self.bono:,.0f}€,".replace(",", ".")
        return f"{super().__str__()} {bono_f}"