import datetime

inventario = {
    "Laptop HP": {"disponible": True, "prestamos": []},
    "Tablet Samsung": {"disponible": True, "prestamos": []}
}

def mostrar_equipos():
    print("\n--- INVENTARIO ---")
    for equipo, info in inventario.items():
        estado = "Disponible" if info["disponible"] else "Prestado"
        print(f"Equipo: {equipo} | Estado: {estado}")

def registrar_prestamo():
    mostrar_equipos()
    nombre = input("\nNombre del equipo: ")
    
    if nombre in inventario:
        if inventario[nombre]["disponible"]:
            usuario = input("Nombre del usuario: ")
            fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            
            inventario[nombre]["prestamos"].append((usuario, fecha))
            inventario[nombre]["disponible"] = False
            print("Registro exitoso.")
        else:
            print("El equipo no esta disponible.")
    else:
        print("El equipo no existe.")

def devolver_equipo():
    nombre = input("Nombre del equipo a devolver: ")
    if nombre in inventario:
        if not inventario[nombre]["disponible"]:
            inventario[nombre]["disponible"] = True
            print("Devolucion exitosa.")
        else:
            print("El equipo ya estaba disponible.")
    else:
        print("El equipo no existe.")

def ver_historial():
    print("\n--- HISTORIAL ---")
    for equipo, info in inventario.items():
        print(f"\nEquipo: {equipo}")
        if not info["prestamos"]:
            print("Sin prestamos registrados.")
        else:
            for p in info["prestamos"]:
                user, date = p
                print(f"- Usuario: {user} | Fecha: {date}")

def agregar_equipo():
    nombre = input("Nombre del nuevo equipo: ")
    if nombre in inventario:
        print("El equipo ya existe.")
    else:
        inventario[nombre] = {"disponible": True, "prestamos": []}
        print("Equipo agregado.")

def menu():
    while True:
        print("\nSISTEMA DE PRESTAMOS")
        print("1. Ver equipos")
        print("2. Registrar prestamo")
        print("3. Devolver equipo")
        print("4. Ver historial")
        print("5. Agregar equipo")
        print("6. Salir")
        
        opcion = input("Opcion: ")
        
        if opcion == "1":
            mostrar_equipos()
        elif opcion == "2":
            registrar_prestamo()
        elif opcion == "3":
            devolver_equipo()
        elif opcion == "4":
            ver_historial()
        elif opcion == "5":
            agregar_equipo()
        elif opcion == "6":
            break
        else:
            print("Opcion invalida.")

if __name__ == "__main__":
    menu()