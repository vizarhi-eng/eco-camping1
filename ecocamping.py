print("gestion de Eco-Camping 'Bosque Vivo")
capacidad_maxima = 15
sitios_ocupados = 0
ejecutando = True
while ejecutando:
    print("\n=== MENU DE CONTROL DE REGISTROS")
    print("1.- Ver sitios disponibles")
    print("2.- Registro de nuevos vehiculos en el sitio(Entrada)")
    print("3.- Registro de salida de vehiculos(Salida)")
    print("5.- Salir")
    try:
        opcion = int(input("Seleccione una opcion (1-5):"))
    except ValueError:
        print("Opcion no valida, por favor seleccione entre 1-5")
        continue
    #Despliegue de opciones
    if opcion == 1:
        disponibles = capacidad_maxima - sitios_ocupados
        print(f"\n[INFO] Sitios libres para recibir vehiculos: {disponibles}")
    else:
        print("Opcion fuera de rango")