def solicitar_informacion():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    codigo_seccion = input("Código-sección: ")
    sede = input("Sede: ")

    if codigo_seccion == "DRY7122-003V":
        sede = input("Sede: ")
        print("Información del alumno:")
        print(f"Nombre: {nombre}")
        print(f"Apellido: {apellido}")
        print(f"Código-sección: {codigo_seccion}")
        print(f"Sede: {sede}")
    else:
        print("Error: El alumno no pertenece a esta sección.")

solicitar_informacion()
