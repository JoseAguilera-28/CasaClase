from empresa import Empresa
from modelos import JefeProyecto, QA
from excepciones import IDDuplicadoError

def ejecutar_examen():
    try:
        suricata = Empresa("Suricata del Sur")
        print(suricata) 

        datos = [
            JefeProyecto("J11", "Ana Isabel", "García Márquez", 3000, suricata.nombre, 500),
            QA("Q01", "Luisa María", "Ruiz Zafón", 1500, suricata.nombre, "Security Tester"),
            QA("Q02", "María Anacleta", "Núñez Pedralvo", 1500, suricata.nombre, "QA Automation Engineer")
        ]

        for e in datos:
            suricata.agregar_empleado(e)

        yo = QA("Q03", "Jose", "Aguilera", 2000, suricata.nombre, "Junior Dev")
        suricata.agregar_empleado(yo)

        print(suricata)

        try:
            suricata.agregar_empleado(QA("Q02", "Invasor", "Error", 1000, suricata.nombre, "Fallará"))
        except IDDuplicadoError as e:
            print(f"\n{e}")

    except Exception as e:
        print(f"Error en el sistema: {e}")

if __name__ == "__main__":
    ejecutar_examen()