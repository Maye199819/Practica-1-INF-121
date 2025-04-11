class Cocinero:
    def __init__(self, nombre, sueldo_mes, horas_extra, sueldo_hora):
        self.nombre = nombre
        self.sueldo_mes = sueldo_mes
        self.horas_extra = horas_extra
        self.sueldo_hora = sueldo_hora

    def sueldo_total(self):
        return self.sueldo_mes + self.horas_extra * self.sueldo_hora

    def mostrar_si_sueldo_es(self, x):
        if self.sueldo_mes == x:
            print(f"Cocinero: {self.nombre}")


