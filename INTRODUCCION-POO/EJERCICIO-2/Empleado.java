class Empleado {
    String nombre;
    double sueldo;

    public Empleado(String nombre, double sueldo) {
        this.nombre = nombre;
        this.sueldo = sueldo;
    }

    public double calcularSueldoAnual() {
        return this.sueldo * 12;
    }

    public void aplicarAumento(double porcentaje) {
        this.sueldo *= (1 + porcentaje / 100);
    }

    public static void main(String[] args) {
        // c) Crea dos empleados y muestra sus sueldos antes y después del aumento
        Empleado empleado1 = new Empleado("Patroclio", 1500.0);
        Empleado empleado2 = new Empleado("Fernanda", 4200.0);

        System.out.println("Sueldo anual de " + empleado1.nombre + ": " + empleado1.calcularSueldoAnual());
        System.out.println("Sueldo anual de " + empleado2.nombre + ": " + empleado2.calcularSueldoAnual());
        System.out.println("***************************************************");

        System.out.println("Sueldo de " + empleado1.nombre + " antes del aumento: " + empleado1.sueldo);
        empleado1.aplicarAumento(10.0);
        System.out.println("Sueldo de " + empleado1.nombre + " después del aumento: " + empleado1.sueldo);
        System.out.println("***************************************************");

        System.out.println("Sueldo de " + empleado2.nombre + " antes del aumento: " + empleado2.sueldo);
        empleado2.aplicarAumento(10.0);
        System.out.println("Sueldo de " + empleado2.nombre + " después del aumento: " + empleado2.sueldo);
    }
}
