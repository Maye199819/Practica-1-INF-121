public class Main {
    public static void main(String[] args) {
        Cocinero c1 = new Cocinero("Luis", 1500, 10, 15.5f);
        Mesero m1 = new Mesero("Vaneza", 1000, 8, 10.0f, 200);
        Mesero m2 = new Mesero("Pablo", 1000, 5, 10.0f, 150);
        Administrativo a1 = new Administrativo("Lurdes", 1800, "Gerente");
        Administrativo a2 = new Administrativo("Camilo", 1500, "Contador");

        System.out.println("Sueldos Totales:");
        System.out.println("Cocinero Luis: " + c1.sueldoTotal());
        System.out.println("Mesero Vaneza: " + m1.sueldoTotal());
        System.out.println("Mesero Pablo: " + m2.sueldoTotal());
        System.out.println("Administrativo Lurdes: " + a1.sueldoTotal());
        System.out.println("Administrativo Camilo: " + a2.sueldoTotal());

        System.out.println("\nEmpleados con sueldo_mes = 1000:");
        c1.mostrarSiSueldoEs(1000);
        m1.mostrarSiSueldoEs(1000);
        m2.mostrarSiSueldoEs(1000);
        a1.mostrarSiSueldoEs(1000);
        a2.mostrarSiSueldoEs(1000);
    }
}
