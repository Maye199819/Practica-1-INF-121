public class Coche {
    String marca;
    String modelo;
    int velocidad;

    public Coche(String marca, String modelo) {
        this.marca = marca;
        this.modelo = modelo;
        this.velocidad = 0;
    }

    public void acelerar() {
        this.velocidad += 10;
    }

    public void frenar() {
        if (this.velocidad >= 5) {
            this.velocidad -= 5;
        } else {
            this.velocidad = 0;
        }
    }

    public void mostrarVelocidad() {
        System.out.println("El coche " + this.marca + " " + this.modelo + " va a una velocidad de " + this.velocidad + " km/h.");
    }

    public static void main(String[] args) {
        Coche coche1 = new Coche("Toyota", "Corolla");
        Coche coche2 = new Coche("Volkswagen", "Golf");

        coche1.acelerar();
        coche1.acelerar();
        coche2.acelerar();
        coche2.acelerar();
        coche2.acelerar();

        System.out.println("Velocidades después de acelerar:");
        coche1.mostrarVelocidad();
        coche2.mostrarVelocidad();

        coche1.frenar();
        coche2.frenar();
        coche2.frenar();
        coche2.frenar();
        coche2.frenar(); 

        System.out.println("\nVelocidades después de frenar:");
        coche1.mostrarVelocidad();
        coche2.mostrarVelocidad();
    }
}
