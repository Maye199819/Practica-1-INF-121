# Instanciar
mi_perro = Perro("Rocky", 3, "Pastor Aleman")
mi_gato = Gato("Pelusa", "Blanco y plomo")
mi_pajaro = Pajaro("Tachuela", "Loro")

animales = [mi_perro, mi_gato, mi_pajaro]

print("\n--- Sonidos de los animales ---")
for animal in animales:
    animal.hacerSonido()

print("\n--- Movimientos de los animales ---")
for animal in animales:
    animal.moverse()
