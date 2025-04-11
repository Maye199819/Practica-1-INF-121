class Gato(Animal):
    def __init__(self, nombre, color):
        super().__init__(nombre)
        self.color = color

    def hacerSonido(self):
        print("Miau!")

    def moverse(self):
        print(f"{self.nombre} esta saltando.")
