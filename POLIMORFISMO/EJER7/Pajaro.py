class Pajaro(Animal):
    def __init__(self, nombre, tipo):
        super().__init__(nombre)
        self.tipo = tipo

    def hacerSonido(self):
        print("Pio pio!")

    def moverse(self):
        print(f"{self.nombre} esta volando.")
