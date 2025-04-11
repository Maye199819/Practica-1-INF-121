class Mesero:
    def __init__(self, nombre, sueldo_mes, horas_extra, sueldo_hora, propina):
        self.nombre = nombre
        self.sueldo_mes = sueldo_mes
        self.horas_extra = horas_extra
        self.sueldo_hora = sueldo_hora
        self.propina = propina

    def sueldo_total(self):
        return self.sueldo_mes + self.horas_extra * self.sueldo_hora + self.propina

    def mostrar_si_sueldo_es(self, x):
        if self.sueldo_mes == x:
            print(f"Mesero: {self.nombre}")


