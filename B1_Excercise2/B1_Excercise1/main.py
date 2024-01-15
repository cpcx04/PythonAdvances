def carga_palabras():
    frecuencias = {}
    with open('palabras.txt', 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            palabra = linea.strip()
            frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    return frecuencias

frecuencias_palabras = {}

while True:
    print("\nMenú:")
    print("1. Importar palabras claves")
    print("2. Mostrar palabras claves y frecuencias")
    print("0. Salir")

    eleccion = input("Seleccione una opción: ")

    if eleccion == "1":
        frecuencias_palabras = carga_palabras()
        print("Fichero importado.")
    elif eleccion == "2":
        if not frecuencias_palabras:
            print("Aún no has importado palabras clave. Utiliza la opción 1.")
        else:
            for palabra, frecuencia in frecuencias_palabras.items():
                print(f"{palabra}: {frecuencia} veces")
    elif eleccion == "0":
        print("Saliendo. Gracias por usar nuestro programa.")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")
