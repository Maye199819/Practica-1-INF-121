class Computadora:
    def __init__(self, marca, modelo, procesador, ram_gb, disco_duro_gb):
        self.marca = marca
        self.modelo = modelo
        self.procesador = procesador
        self.ram_gb = ram_gb
        self.disco_duro_gb = disco_duro_gb
        self.encendida = False

    def mostrar_componentes(self):
        print("Componentes principales de la computadora:")
        print(f"  Marca: {self.marca}")
        print(f"  Modelo: {self.modelo}")
        print(f"  Procesador: {self.procesador}")
        print(f"  RAM: {self.ram_gb} GB")
        print(f"  Disco Duro: {self.disco_duro_gb} GB")

    def mostrar_estado(self):
        if self.encendida:
            print("La computadora esta encendida.")
        else:
            print("La computadora esta apagada.")

    def encender(self):
        if not self.encendida:
            self.encendida = True
            print("Encendiendo la computadora...")
        else:
            print("La computadora ya esta encendida.")

    def apagar(self):
        if self.encendida:
            self.encendida = False
            print("Apagando la computadora...")
        else:
            print("La computadora ya esta apagada.")

# Crear una instancia de la computadora
mi_computadora = Computadora("Dell", "Inspiron 15", "Intel Core i5", 8, 512)

# Mostrar los componentes
mi_computadora.mostrar_componentes()
print("-" * 30)

# Mostrar el estado inicial
mi_computadora.mostrar_estado()
print("-" * 30)

# Encender la computadora
mi_computadora.encender()
mi_computadora.mostrar_estado()
print("-" * 30)

# Intentar encenderla de nuevo
mi_computadora.encender()
print("-" * 30)

# Apagar la computadora
mi_computadora.apagar()
mi_computadora.mostrar_estado()
print("-" * 30)

# Intentar apagarla de nuevo
mi_computadora.apagar()
