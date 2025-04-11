class Coche:
    def __init__(self, marca, modelo, velocidad=0):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad

    def acelerar(self):
        self.velocidad += 10

    def frenar(self):
        if self.velocidad >= 5:
            self.velocidad -= 5
        else:
            self.velocidad = 0

    def mostrar_velocidad(self):
        print(f"El coche {self.marca} {self.modelo} va a una velocidad de {self.velocidad} km/h.")

# Crear dos coches
coche1 = Coche("Toyota", "Corolla")
coche2 = Coche("Volkswagen", "Golf")

# Acelerar varias veces
coche1.acelerar()
coche1.acelerar()
coche2.acelerar()
coche2.acelerar()
coche2.acelerar()

# Mostrar las velocidades 
print("Velocidades después de acelerar:")
coche1.mostrar_velocidad()
coche2.mostrar_velocidad()

# Frenar varias veces
coche1.frenar()
coche2.frenar()
coche2.frenar()
coche2.frenar()
coche2.frenar() # Intentar frenar más de lo posible

# Mostrar las velocidades después de frenar
print("\nVelocidades después de frenar:")
coche1.mostrar_velocidad()
coche2.mostrar_velocidad()
