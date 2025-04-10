class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

    def saludo(self):
        return f"Hola, soy {self.nombre} de {self.ciudad}"

    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return "Verdad"
        else:
            return "Falso"

# b) Crea tres personas y muestra su saludo
persona1 = Persona("Ana Maria", 30, "La Paz")
persona2 = Persona("Cesar", 15, "Cochabamba")
persona3 = Persona("Sonia", 25, "Santa Cruz")

print(persona1.saludo())
print(persona2.saludo())
print(persona3.saludo())
print("***************************************************")
# c) Agrega un método para verificar si es mayor de edad
print(f"{persona1.nombre} es mayor de edad: {persona1.es_mayor_de_edad()}")
print(f"{persona2.nombre} es mayor de edad: {persona2.es_mayor_de_edad()}")
print(f"{persona3.nombre} es mayor de edad: {persona3.es_mayor_de_edad()}")
