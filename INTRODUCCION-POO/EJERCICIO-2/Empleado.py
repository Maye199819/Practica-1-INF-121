class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def calcular_sueldo_anual(self):
        return self.sueldo * 12

    def aplicar_aumento(self, porcentaje):
        self.sueldo *= (1 + porcentaje / 100)


empleado1 = Empleado("Patroclio", 1500)
empleado2 = Empleado("Fernanda", 4200)

print(f"Sueldo anual de {empleado1.nombre}: {empleado1.calcular_sueldo_anual()}")
print(f"Sueldo anual de {empleado2.nombre}: {empleado2.calcular_sueldo_anual()}")
print("***************************************************")

print(f"Sueldo de {empleado1.nombre} antes del aumento: {empleado1.sueldo}")
empleado1.aplicar_aumento(10)
print(f"Sueldo de {empleado1.nombre} después del aumento: {empleado1.sueldo}")
print("***************************************************")

print(f"Sueldo de {empleado2.nombre} antes del aumento: {empleado2.sueldo}")
empleado2.aplicar_aumento(10)
print(f"Sueldo de {empleado2.nombre} después del aumento:
