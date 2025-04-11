public class Videojuego {
    private String nombre;
    private String plataforma;
    private int cantidadJugadores;

    // Constructor
    public Videojuego(String nombre, String plataforma, int cantidadJugadores) {
        this.nombre = nombre;
        this.plataforma = plataforma;
        this.cantidadJugadores = cantidadJugadores;
    }

    // Constructor con valores por defecto
    public Videojuego(String nombre, String plataforma) {
        this(nombre, plataforma, 1);
    }

    public Videojuego(String nombre) {
        this(nombre, "PC", 1);
    }

    // Método mostrar
    public void mostrar() {
        System.out.println("Nombre: " + nombre);
        System.out.println("Plataforma: " + plataforma);
        System.out.println("Cantidad de Jugadores: " + cantidadJugadores);
    }

    // Método sobrecargado agregarJugadores
    public void agregarJugadores() {
        this.cantidadJugadores += 1;
    }

    public void agregarJugadores(int cantidad) {
        if (cantidad > 0) {
            this.cantidadJugadores += cantidad;
        } else {
            System.out.println("Cantidad inválida. No se puede agregar un número negativo de jugadores.");
        }
    }

    // Programa principal
    public static void main(String[] args) {
        Videojuego juego1 = new Videojuego("Galaga", "Maquinita", 1);
        Videojuego juego2 = new Videojuego("LOL", "PC");
        Videojuego juego3 = new Videojuego("Minecraft");

        System.out.println("--- Videojuego 1 ---");
        juego1.mostrar();

        System.out.println("\n--- Videojuego 2 ---");
        juego2.mostrar();

        System.out.println("\n--- Videojuego 3 ---");
        juego3
