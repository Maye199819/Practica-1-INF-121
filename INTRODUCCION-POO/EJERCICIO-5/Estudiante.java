public class Estudiante {
    String nombre;
    double nota1;
    double nota2;

    public Estudiante(String nombre, double nota1, double nota2) {
        this.nombre = nombre;
        this.nota1 = nota1;
        this.nota2 = nota2;
    }

    public double calcularPromedio() {
        return (this.nota1 + this.nota2) / 2.0;
    }

    public boolean aprobo() {
        return calcularPromedio() >= 60;
    }

    public void mostrarResultados() {
        double promedio = calcularPromedio();
        System.out.println("Nombre: " + this.nombre);
        System.out.println("Promedio: " + promedio);
        if (aprobo()) {
            System.out.println("Estado: Aprobado");
        } else {
            System.out.println("Estado: Reprobado");
        }
        System.out.println("--------------------");
    }

    public static void main(String[] args) {
        // Crear tres estudiantes
        Estudiante estudiante1 = new Estudiante("Sofia Rojas", 75, 60);
        Estudiante estudiante2 = new Estudiante("Ismael Caseres", 50, 65);
        Estudiante estudiante3 = new Estudiante("Selena Gomez", 90, 95);

        // Mostrar sus promedios y si aprobaron
        estudiante1.mostrarResultados();
        estudiante2.mostrarResultados();
        estudiante3.mostrarResultados();
    }
}
