class Videojuego:
    def __init__(self, nombre, plataforma="PC", cantidadJugadores=1):
        self.nombre = nombre
        self.plataforma = plataforma
        self.cantidadJugadores = cantidadJugadores

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Plataforma: {self.plataforma}")
        print(f"Cantidad de Jugadores: {self.cantidadJugadores}")

    # Método sobrecargado
    def agregarJugadores(self, cantidad=1):
        if cantidad > 0:
            self.cantidadJugadores += cantidad
        else:
            print("Cantidad inválida. No se puede agregar un número negativo de jugadores.")


# Instancias
juego1 = Videojuego("Galaga", "Maquinita", 1)
juego2 = Videojuego("LOL", "PC")
juego3 = Videojuego("Minecraft")

print("--- Videojuego 1 ---")
juego1.mostrar()

print("\n--- Videojuego 2 ---")
juego2.mostrar()

print("\n--- Videojuego 3 ---")
juego3.mostrar()

# Pruebas con el método sobrecargado
print("\n--- Agregando jugadores a Videojuego 2 ---")
juego2.agregarJugadores()  # Agrega 1 jugador
print("Después de agregar 1 jugador:")
juego2.mostrar()

juego2.agregarJugadores(3)  # Agrega 3 jugadores
print("Después de agregar 3 jugadores:")
juego2.mostrar()

juego2.agregarJugadores(-1)  # Intenta agregar una cantidad inválida
print("Después de intentar agregar una cantidad inválida:")
juego2.mostrar()
