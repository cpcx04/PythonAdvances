def carga_palabras():
    palabras = []
    with open('palabras.txt', 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            palabras.append(linea.strip())
    return palabras

texto = []

while True:
    print("\nMenú:")
    print("1.Importar palabras claves")
    print("2.Leer palabras claves")
    print("0.Salir")

    eleccion = input("Seleccione uno: \n")

    if eleccion == "1":
        texto = carga_palabras()
        print("fichero importado")
    elif eleccion == "2":
        if not texto:
            print("Aún no has importado palabras clave. Utiliza la opción 1.")
        else:
            for i in range(0, len(texto), 20):
                print("\n".join(texto[i:i + 20]))
                if i + 20 < len(texto):
                    input("Presiona Enter para mostrar las siguientes 20 palabras clave...")
    elif eleccion == "0":
        print("Saliendo,gracias por usar nuestro programa")
        break
    else:
        print("Opcion no valida intentelo de nuevo")
