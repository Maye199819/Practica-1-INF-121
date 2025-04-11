class BloqueCofre:
    def __init__(self, capacidad, resistencia, tipo):
        self.__capacidad = capacidad
        self.__resistencia = resistencia
        self.__tipo = tipo

    def accion(self):
        print(f"Abriendo cofre tipo {self.__tipo} con capacidad {self.__capacidad}")

    def colocar(self, orientacion):
        print(f"Cofre colocado en orientacion: {orientacion}")

    def romper(self):
        print("El cofre fue destruido. Los objetos se perdieron.")
