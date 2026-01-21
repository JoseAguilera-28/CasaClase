import pytest
from persona import Persona


def test_caso_1_error_menos_1():
    with pytest.raises(ValueError):
        Persona(-1)

def test_caso_2_error_menos_100():
    with pytest.raises(ValueError):
        Persona(-100)


def test_caso_3_falso_0():
    persona = Persona(0)
    assert persona.isMayorDeEdad() == False

def test_caso_4_falso_17():
    persona = Persona(17)
    assert persona.isMayorDeEdad() == False


def test_caso_5_verdadero_18():
    persona = Persona(18)
    assert persona.isMayorDeEdad() == True

def test_caso_6_verdadero_100():
    persona = Persona(100)
    assert persona.isMayorDeEdad() == True