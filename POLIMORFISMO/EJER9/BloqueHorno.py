class BloqueHorno:
    def __init__(self, color, capacidad_comida):
        self.__color = color
        self.__capacidad_comida = capacidad_comida

    def accion(self):
        print(f"Horno color {self.__color} encendido para cocinar {self.__capacidad_comida} comidas.")

    def colocar(self, orientacion):
        print(f"Horno instalado en orientacion: {orientacion}")

    def romper(self):
        print("Horno roto. Toda la comida fue perdida.")
