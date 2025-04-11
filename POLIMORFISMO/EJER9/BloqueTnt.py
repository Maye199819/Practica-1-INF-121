class BloqueTnt:
    def __init__(self, tipo, dano):
        self.__tipo = tipo
        self.__dano = dano

    def accion(self):
        print(f"TNT tipo {self.__tipo} activada... ¡Corre!")

    def colocar(self, orientacion):
        print(f"TNT colocada en orientacion: {orientacion}")

    def romper(self):
        print(f"La TNT explotó y causó {self.__dano} de dano.")
