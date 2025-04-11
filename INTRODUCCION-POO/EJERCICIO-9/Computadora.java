public class Computadora {
    private String marca;
    private String modelo;
    private String procesador;
    private int ramGb;
    private int discoDuroGb;
    private boolean encendida;

    public Computadora(String marca, String modelo, String procesador, int ramGb, int discoDuroGb) {
        this.marca = marca;
        this.modelo = modelo;
        this.procesador = procesador;
        this.ramGb = ramGb;
        this.discoDuroGb = discoDuroGb;
        this.encendida = false;
    }

    public void mostrarComponentes() {
        System.out.println("Componentes principales de la computadora:");
        System.out.println("  Marca: " + this.marca);
        System.out.println("  Modelo: " + this.modelo);
        System.out.println("  Procesador: " + this.procesador);
        System.out.println("  RAM: " + this.ramGb + " GB");
        System.out.println("  Disco Duro: " + this.discoDuroGb + " GB");
    }

    public void mostrarEstado() {
        if (this.encendida) {
            System.out.println("La computadora esta encendida.");
        } else {
            System.out.println("La computadora esta apagada.");
        }
    }

    public void encender() {
        if (!this.encendida) {
            this.encendida = true;
            System.out.println("Encendiendo la computadora...");
        } else {
            System.out.println("La computadora ya esta encendida.");
        }
    }

    public void apagar() {
        if (this.encendida) {
            this.encendida = false;
            System.out.println("Apagando la computadora...");
        } else {
            System.out.println("La computadora ya esta apagada.");
        }
    }

    public static void main(String[] args) {
        // Crear una instancia de la computadora
        Computadora miComputadora = new Computadora("Dell", "Inspiron 15", "Intel Core i5", 8, 512);

        // Mostrar los componentes
        miComputadora.mostrarComponentes();
        System.out.println("-".repeat(30));

        // Mostrar el estado inicial
        miComputadora.mostrarEstado();
        System.out.println("-".repeat(30));

        // Encender la computadora
        miComputadora.encender();
        miComputadora.mostrarEstado();
        System.out.println("-".repeat(30));

        // Intentar encenderla de nuevo
        miComputadora.encender();
        System.out.println("-".repeat(30));

        // Apagar la computadora
        miComputadora.apagar();
        miComputadora.mostrarEstado();
        System.out.println("-".repeat(30));

        // Intentar apagarla de nuevo
        miComputadora.apagar();
    }
}
