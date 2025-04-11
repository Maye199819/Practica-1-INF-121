class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre)
        self.edad = edad
        self.raza = raza

    def hacerSonido(self):
        print("Guau!")

    def moverse(self):
        print(f"{self.nombre} esta corriendo.")
