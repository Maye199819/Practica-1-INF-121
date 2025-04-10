class Persona {
    String nombre;
    int edad;
    String ciudad;

    public Persona(String nombre, int edad, String ciudad) {
        this.nombre = nombre;
        this.edad = edad;
        this.ciudad = ciudad;
    }

    public String saludo() {
        return "Hola, soy " + this.nombre + " de " + this.ciudad;
    }

    public String esMayorDeEdad() {
        if (this.edad >= 18) {
            return "Verdad";
        } else {
            return "Falso";
        }
    }

    public static void main(String[] args) {
        // b) Crea tres personas y muestra su saludo
        Persona persona1 = new Persona("Ana Maria", 30, "La Paz");
        Persona persona2 = new Persona("Cesar", 15, "Cochabamba");
        Persona persona3 = new Persona("Sonia", 25, "Santa Cruz");

        System.out.println(persona1.saludo());
        System.out.println(persona2.saludo());
        System.out.println(persona3.saludo());
        System.out.println("***************************************************");

        // c) Agrega un método para verificar si es mayor de edad
        System.out.println(persona1.nombre + " es mayor de edad: " + persona1.esMayorDeEdad());
        System.out.println(persona2.nombre + " es mayor de edad: " + persona2.esMayorDeEdad());
        System.out.println(persona3.nombre + " es mayor de edad: " + persona3.esMayorDeEdad());
    }
}
