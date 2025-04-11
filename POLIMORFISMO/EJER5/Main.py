# Instancias
o1 = Oficina(4, 2, 1)
o2 = Oficina(6, 3, 2)
a1 = Aula("Aula 101", 30, 30)
a2 = Aula("Aula 202", 40, 40)
lab1 = Laboratorio("Lab Química", 25, 12, 25)

# Mostrar datos
print("--- Mostrar Ambientes ---")
o1.mostrar()
o2.mostrar()
a1.mostrar()
a2.mostrar()
lab1.mostrar()

# Mostrar cantidad de muebles
print("\n--- Cantidad de Muebles ---")
print(f"Oficina 1: {o1.cantidad_muebles()}")
print(f"Oficina 2: {o2.cantidad_muebles()}")
print(f"Aula 1: {a1.cantidad_muebles()}")
print(f"Aula 2: {a2.cantidad_muebles()}")
print(f"Laboratorio: {lab1.cantidad_muebles()}")
