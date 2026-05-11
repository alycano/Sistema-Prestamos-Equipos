import datetime
import os

inventario = {
    "Laptop HP": {"disponible": True, "prestamos": []},
    "Tablet Samsung": {"disponible": True, "prestamos": []}
}

def limpiar_pantalla():
    # Esto limpia la consola dependiendo si usas Windows o Linux/Mac
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_equipos():
    print("\n-INVENTARIO DE EQUIPOS-")
    for equipo, info in inventario.items():
        estado = "Disponible" if info["disponible"] else "Prestado"
        print(f"Equipo: {equipo} | Estado: {estado}")

def registrar_prestamo():
    mostrar_equipos()
    # Usamos .strip() para quitar espacios vacios al inicio o final
    nombre_entrada = input("\nNombre del equipo: ").strip()
    
    # Buscamos el equipo sin importar mayusculas/minusculas
    equipo_encontrado = None
    for nombre in inventario:
        if nombre.lower() == nombre_entrada.lower():
            equipo_encontrado = nombre
            break

    if equipo_encontrado:
        if inventario[equipo_encontrado]["disponible"]:
            usuario = input("Nombre del usuario: ")
            fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            
            inventario[equipo_encontrado]["prestamos"].append((usuario, fecha))
            inventario[equipo_encontrado]["disponible"] = False
            print(f"Registro exitoso para {equipo_encontrado}.")
        else:
            print("El equipo ya esta ocupado.")
    else:
        print("Ese equipo no existe en el sistema.")

def devolver_equipo():
    nombre_entrada = input("Nombre del equipo a devolver: ").strip()
    
    equipo_encontrado = None
    for nombre in inventario:
        if nombre.lower() == nombre_entrada.lower():
            equipo_encontrado = nombre
            break

    if equipo_encontrado:
        if not inventario[equipo_encontrado]["disponible"]:
            inventario[equipo_encontrado]["disponible"] = True
            print(f"Devolucion de '{equipo_encontrado}' realizada.")
        else:
            print("El equipo ya estaba marcado como disponible.")
    else:
        print("Equipo no encontrado.")

def ver_historial():
    print("\n--- HISTORIAL DE MOVIMIENTOS ---")
    for equipo, info in inventario.items():
        print(f"\nEquipo: {equipo}")
        if not info["prestamos"]:
            print("Sin prestamos registrados.")
        else:
            for p in info["prestamos"]:
                user, date = p
                print(f"- Usuario: {user} | Fecha: {date}")
    input("\nPresiona Enter para volver al menu...")

def agregar_equipo():
    nombre = input("Nombre del nuevo equipo: ").strip()
    # Validacion para no repetir nombres (insensible a mayusculas)
    existe = any(n.lower() == nombre.lower() for n in inventario)
    
    if existe:
        print("Ese equipo ya esta registrado.")
    else:
        inventario[nombre] = {"disponible": True, "prestamos": []}
        print(f"Equipo '{nombre}' agregado al sistema.")

def menu():
    while True:
        limpiar_pantalla()
        print("SISTEMA DE PRESTAMOS ADSO")
        print("1. Ver equipos")
        print("2. Registrar prestamo")
        print("3. Devolver equipo")
        print("4. Ver historial")
        print("5. Agregar equipo")
        print("6. Salir")
        
        opcion = input("\nSeleccione una opcion: ")
        
        if opcion == "1":
            mostrar_equipos()
            input("\nPresiona Enter para continuar...")
        elif opcion == "2":
            registrar_prestamo()
            input("\nPresiona Enter para continuar...")
        elif opcion == "3":
            devolver_equipo()
            input("\nPresiona Enter para continuar...")
        elif opcion == "4":
            ver_historial()
        elif opcion == "5":
            agregar_equipo()
            input("\nPresiona Enter para continuar...")
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion no valida.")
            input("\nPresiona Enter para intentar de nuevo...")

if __name__ == "__main__":
    menu()