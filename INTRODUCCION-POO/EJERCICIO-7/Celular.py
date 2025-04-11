class Celular:
    def __init__(self, espacio_total_mb=1024):
        self.espacio_total_mb = espacio_total_mb
        self.espacio_ocupado_mb = 0
        self.aplicaciones_instaladas = []
        self.max_aplicaciones = 20
        self.bateria = 100

    def instalar_aplicacion(self, nombre, peso_mb):
        if len(self.aplicaciones_instaladas) < self.max_aplicaciones:
            if self.espacio_ocupado_mb + peso_mb <= self.espacio_total_mb:
                self.aplicaciones_instaladas.append({"nombre": nombre, "peso_mb": peso_mb})
                self.espacio_ocupado_mb += peso_mb
                print("-------------------------------------------------")
                print(f"Aplicación '{nombre}' instalada correctamente.")
                
            else:
                print(f"No hay suficiente espacio para instalar '{nombre}'.")
        else:
            print("Se ha alcanzado el límite de aplicaciones instaladas.")

    def utilizar_aplicacion(self, nombre_app, tiempo_uso_minutos):
        
        if self.bateria > 0:
            aplicacion = next((app for app in self.aplicaciones_instaladas if app["nombre"] == nombre_app), None)
            if aplicacion:
                uso_en_periodos = tiempo_uso_minutos // 10
                if uso_en_periodos > 0:
                    peso_mb = aplicacion["peso_mb"]
                    bateria_a_gastar = 0
                    if peso_mb > 250:
                        bateria_a_gastar = 5 * uso_en_periodos
                    elif peso_mb > 100:
                        bateria_a_gastar = 2 * uso_en_periodos
                    else:
                        bateria_a_gastar = 1 * uso_en_periodos

                    if self.bateria >= bateria_a_gastar:
                        self.bateria -= bateria_a_gastar
                        print(f"Utilizando '{nombre_app}' durante {tiempo_uso_minutos} minutos. Batería restante: {self.bateria}%.")
                    else:
                        print("Batería insuficiente para utilizar la aplicación.")
                        self.bateria = 0
                        print("Celular apagado.")
            else:
                print(f"La aplicación '{nombre_app}' no está instalada.")
        else:
            print("Celular apagado.")

    def mostrar_bateria(self):
        print(f"Batería restante: {self.bateria}%.")

# Crear un celular
mi_celular = Celular()

# Instalar algunas aplicaciones
mi_celular.instalar_aplicacion("WhatsApp", 80)
mi_celular.instalar_aplicacion("Instagram", 150)
mi_celular.instalar_aplicacion("JuegoPesado", 300)
mi_celular.instalar_aplicacion("TikTok", 90)
mi_celular.instalar_aplicacion("OtraApp", 50)
mi_celular.instalar_aplicacion("App1", 10)
mi_celular.instalar_aplicacion("App2", 10)
mi_celular.instalar_aplicacion("App3", 10)
mi_celular.instalar_aplicacion("App4", 10)
mi_celular.instalar_aplicacion("App5", 10)
mi_celular.instalar_aplicacion("App6", 10)
mi_celular.instalar_aplicacion("App7", 10)
mi_celular.instalar_aplicacion("App8", 10)
mi_celular.instalar_aplicacion("App9", 10)
mi_celular.instalar_aplicacion("App10", 10)
mi_celular.instalar_aplicacion("App11", 10)
mi_celular.instalar_aplicacion("App12", 10)
mi_celular.instalar_aplicacion("App13", 10)
mi_celular.instalar_aplicacion("App14", 10)
mi_celular.instalar_aplicacion("App15", 10) # Intentar instalar más de 20

# Mostrar batería inicial
print()
print()
mi_celular.mostrar_bateria()

# Utilizar algunas aplicaciones
mi_celular.utilizar_aplicacion("WhatsApp", 35)
mi_celular.utilizar_aplicacion("Instagram", 60)
mi_celular.utilizar_aplicacion("JuegoPesado", 20)
mi_celular.utilizar_aplicacion("TikTok", 90)

# Mostrar batería después de usar aplicaciones
mi_celular.mostrar_bateria()

# Utilizar una aplicación hasta que se acabe la batería
print("\nIntentando usar JuegoPesado hasta agotar la batería:")
while mi_celular.bateria > 0:
    mi_celular.utilizar_aplicacion("JuegoPesado", 10)

# Intentar usar una aplicación con la batería agotada
print("\nIntentando usar WhatsApp con la batería agotada:")
mi_celular.utilizar_aplicacion("WhatsApp", 15)
