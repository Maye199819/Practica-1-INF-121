class Laboratorio:
    def __init__(self, nombre, capacidad, nro_mesas, nro_sillas):
        self.nombre = nombre
        self.capacidad = capacidad
        self.nro_mesas = nro_mesas
        self.nro_sillas = nro_sillas

    def mostrar(self):
        print(f"Laboratorio - Nombre: {self.nombre}, Capacidad: {self.capacidad}, Mesas: {self.nro_mesas}, Sillas: {self.nro_sillas}")

    def cantidad_muebles(self):
        return self.nro_mesas + self.nro_sillas
