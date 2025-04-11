import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Celular {
    private int espacioTotalMb;
    private int espacioOcupadoMb;
    private List<Map<String, Object>> aplicacionesInstaladas;
    private int maxAplicaciones;
    private int bateria;

    public Celular(int espacioTotalMb) {
        this.espacioTotalMb = espacioTotalMb;
        this.espacioOcupadoMb = 0;
        this.aplicacionesInstaladas = new ArrayList<>();
        this.maxAplicaciones = 20;
        this.bateria = 100;
    }

    public Celular() {
        this(1024);
    }

    public void instalarAplicacion(String nombre, int pesoMb) {
        if (aplicacionesInstaladas.size() < maxAplicaciones) {
            if (espacioOcupadoMb + pesoMb <= espacioTotalMb) {
                Map<String, Object> nuevaAplicacion = new HashMap<>();
                nuevaAplicacion.put("nombre", nombre);
                nuevaAplicacion.put("peso_mb", pesoMb);
                aplicacionesInstaladas.add(nuevaAplicacion);
                espacioOcupadoMb += pesoMb;
                System.out.println("-------------------------------------------------");
                System.out.println("Aplicacion '" + nombre + "' instalada correctamente.");

            } else {
                System.out.println("No hay suficiente espacio para instalar '" + nombre + "'.");
            }
        } else {
            System.out.println("Se ha alcanzado el limite de aplicaciones instaladas.");
        }
    }

    public void utilizarAplicacion(String nombreApp, int tiempoUsoMinutos) {
        if (bateria > 0) {
            Map<String, Object> aplicacion = null;
            for (Map<String, Object> app : aplicacionesInstaladas) {
                if (app.get("nombre").equals(nombreApp)) {
                    aplicacion = app;
                    break;
                }
            }

            if (aplicacion != null) {
                int usoEnPeriodos = tiempoUsoMinutos / 10;
                if (usoEnPeriodos > 0) {
                    int pesoMb = (int) aplicacion.get("peso_mb");
                    int bateriaAGastar = 0;
                    if (pesoMb > 250) {
                        bateriaAGastar = 5 * usoEnPeriodos;
                    } else if (pesoMb > 100) {
                        bateriaAGastar = 2 * usoEnPeriodos;
                    } else {
                        bateriaAGastar = 1 * usoEnPeriodos;
                    }

                    if (bateria >= bateriaAGastar) {
                        bateria -= bateriaAGastar;
                        System.out.println("Utilizando '" + nombreApp + "' durante " + tiempoUsoMinutos + " minutos. Bateria restante: " + bateria + "%.");
                    } else {
                        System.out.println("Bateria insuficiente para utilizar la aplicacion.");
                        bateria = 0;
                        System.out.println("Celular apagado.");
                    }
                }
            } else {
                System.out.println("La aplicacion '" + nombreApp + "' no esta instalada.");
            }
        } else {
            System.out.println("Celular apagado.");
        }
    }

    public void mostrarBateria() {
        System.out.println("Bateria restante: " + bateria + "%.");
    }

    public static void main(String[] args) {
        // Crear un celular
        Celular miCelular = new Celular();

        // Instalar algunas aplicaciones
        miCelular.instalarAplicacion("WhatsApp", 80);
        miCelular.instalarAplicacion("Instagram", 150);
        miCelular.instalarAplicacion("JuegoPesado", 300);
        miCelular.instalarAplicacion("TikTok", 90);
        miCelular.instalarAplicacion("OtraApp", 50);
        miCelular.instalarAplicacion("App1", 10);
        miCelular.instalarAplicacion("App2", 10);
        miCelular.instalarAplicacion("App3", 10);
        miCelular.instalarAplicacion("App4", 10);
        miCelular.instalarAplicacion("App5", 10);
        miCelular.instalarAplicacion("App6", 10);
        miCelular.instalarAplicacion("App7", 10);
        miCelular.instalarAplicacion("App8", 10);
        miCelular.instalarAplicacion("App9", 10);
        miCelular.instalarAplicacion("App10", 10);
        miCelular.instalarAplicacion("App11", 10);
        miCelular.instalarAplicacion("App12", 10);
        miCelular.instalarAplicacion("App13", 10);
        miCelular.instalarAplicacion("App14", 10);
        miCelular.instalarAplicacion("App15", 10); // Intentar instalar mas de 20

        // Mostrar bateria inicial
        System.out.println();
        System.out.println();
        miCelular.mostrarBateria();

        // Utilizar algunas aplicaciones
        miCelular.utilizarAplicacion("WhatsApp", 35);
        miCelular.utilizarAplicacion("Instagram", 60);
        miCelular.utilizarAplicacion("JuegoPesado", 20);
        miCelular.utilizarAplicacion("TikTok", 90);

        // Mostrar bateria despues de usar aplicaciones
        miCelular.mostrarBateria();

        // Utilizar una aplicacion hasta que se acabe la bateria
        System.out.println("\nIntentando usar JuegoPesado hasta agotar la bateria:");
        while (miCelular.bateria > 0) {
            miCelular.utilizarAplicacion("JuegoPesado", 10);
        }

        // Intentar usar una aplicacion con la bateria agotada
        System.out.println("\nIntentando usar WhatsApp con la bateria agotada:");
        miCelular.utilizarAplicacion("WhatsApp", 15);
    }
}
