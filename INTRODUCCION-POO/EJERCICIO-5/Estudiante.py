class Estudiante:
    def __init__(self, nombre, nota1, nota2):
        self.nombre = nombre
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_promedio(self):
        return (self.nota1 + self.nota2) / 2

    def aprobo(self):
        return self.calcular_promedio() >= 60

    def mostrar_resultados(self):
        promedio = self.calcular_promedio()
        print(f"Nombre: {self.nombre}")
        print(f"Promedio: {promedio}")
        if self.aprobo():
            print("Estado: Aprobado")
        else:
            print("Estado: Reprobado")
        print("--------------------")

# Crear tres estudiantes
estudiante1 = Estudiante("Sofia Rojas", 75, 60)
estudiante2 = Estudiante("Ismael Caseres", 50, 65)
estudiante3 = Estudiante("Selena Gomez", 90, 95)

# Mostrar sus promedios y si aprobaron
estudiante1.mostrar_resultados()
estudiante2.mostrar_resultados()
estudiante3.mostrar_resultados()
