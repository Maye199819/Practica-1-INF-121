class Administrativo:
    def __init__(self, nombre, sueldo_mes, cargo):
        self.nombre = nombre
        self.sueldo_mes = sueldo_mes
        self.cargo = cargo

    def sueldo_total(self):
        return self.sueldo_mes

    def mostrar_si_sueldo_es(self, x):
        if self.sueldo_mes == x:
            print(f"Administrativo: {self.nombre}")


# Instancias
c1 = Cocinero("Luis", 1500, 10, 15.5)
m1 = Mesero("Ana", 1000, 8, 10.0, 200)
m2 = Mesero("Pedro", 1000, 5, 10.0, 150)
a1 = Administrativo("Laura", 1800, "Gerente")
a2 = Administrativo("Carlos", 1500, "Contador")

# Sueldos totales
print("Sueldos Totales:")
print(f"Cocinero Luis: {c1.sueldo_total()}")
print(f"Mesero Ana: {m1.sueldo_total()}")
print(f"Mesero Pedro: {m2.sueldo_total()}")
print(f"Administrativo Laura: {a1.sueldo_total()}")
print(f"Administrativo Carlos: {a2.sueldo_total()}")

# Mostrar los que tienen sueldo_mes == 1000
print("\nEmpleados con sueldo_mes = 1000:")
c1.mostrar_si_sueldo_es(1000)
m1.mostrar_si_sueldo_es(1000)
m2.mostrar_si_sueldo_es(1000)
a1.mostrar_si_sueldo_es(1000)
a2.mostrar_si_sueldo_es(1000)
