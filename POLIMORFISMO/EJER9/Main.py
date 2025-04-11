def main():
    cofre1 = BloqueCofre(200, 60, "Diamante")
    cofre2 = BloqueCofre(120, 70, "Madera")

    tnt1 = BloqueTnt("Explosiva", 75)
    tnt2 = BloqueTnt("Ultra", 150)

    horno1 = BloqueHorno("Gris", 3)
    horno2 = BloqueHorno("Azul", 8)

    print("\n--- ACCION BLOQUES ---")
    cofre1.accion()
    cofre2.accion()
    tnt1.accion()
    tnt2.accion()
    horno1.accion()
    horno2.accion()

    print("\n--- COLOCAR BLOQUES ---")
    cofre1.colocar("esquina")
    tnt1.colocar("centro")
    horno1.colocar("pared lateral")

    print("\n--- ROMPER BLOQUES ---")
    cofre2.romper()
    tnt2.romper()
    horno2.romper()


if __name__ == "__main__":
    main()
