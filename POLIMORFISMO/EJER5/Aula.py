class Aula:
    def __init__(self, nombre, capacidad, nro_pupitres):
        self.nombre = nombre
        self.capacidad = capacidad
        self.nro_pupitres = nro_pupitres

    def mostrar(self):
        print(f"Aula - Nombre: {self.nombre}, Capacidad: {self.capacidad}, Pupitres: {self.nro_pupitres}")

    def cantidad_muebles(self):
        return self.nro_pupitres
