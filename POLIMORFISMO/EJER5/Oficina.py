class Oficina:
    def __init__(self, nro_sillas, nro_escritorios, nro_estanterias):
        self.nro_sillas = nro_sillas
        self.nro_escritorios = nro_escritorios
        self.nro_estanterias = nro_estanterias

    def mostrar(self):
        print(f"Oficina - Sillas: {self.nro_sillas}, Escritorios: {self.nro_escritorios}, Estanterías: {self.nro_estanterias}")

    def cantidad_muebles(self):
        return self.nro_sillas + self.nro_escritorios + self.nro_estanterias
