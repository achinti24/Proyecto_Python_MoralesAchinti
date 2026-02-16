import json

ARCHIVO_CAMPERS = "campers.json"

def cargar_campers():
    try:
        with open(ARCHIVO_CAMPERS, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except:
        return {"campers": []}


def menu_camper(camper):
    while True:
        print("\n===================================")
        print("        MENÚ CAMPER")
        print("===================================")
        print("1. Ver información general")
        print("2. Ver notas")
        print("3. Cerrar sesión")
        print("===================================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ver_info_camper(camper)

        elif opcion == "2":
            ver_notas(camper)

        elif opcion == "3":
            print("Sesión cerrada")
            break

        else:
            print("Opción inválida")


def ver_info_camper(camper):
    print("\n====== INFORMACIÓN GENERAL ======\n")

    print(f"ID: {camper.get('id')}")
    print(f"Nombre: {camper.get('nombre')} {camper.get('apellidos')}")
    print(f"Dirección: {camper.get('direccion')}")
    print(f"Acudiente: {camper.get('acudiente')}")
    print(f"Teléfono: {camper.get('telefono')}")
    print(f"Estado: {camper.get('estado')}")
    print(f"Riesgo: {camper.get('riesgo')}")
    print(f"Ruta: {camper.get('ruta')}")
    print(f"Jornada: {camper.get('jornada')}")
    print(f"Trainer: {camper.get('trainer')}")
    print(f"Salón: {camper.get('salon')}")
    print(f"Horario: {camper.get('horario')}")
    print(f"Fecha inicio: {camper.get('fecha_inicio')}")
    print(f"Fecha fin: {camper.get('fecha_fin')}")
    print(f"Correo: {camper.get('correo')}")



def ver_notas(camper):
    print("\n====== NOTAS DEL CAMPER ======\n")

    print("NOTAS POR MÓDULO")
    notas = camper.get("notas")

    if not notas:
        print("No hay notas registradas.")
    else:
        for modulo, nota in notas.items():
            if nota is None:
                print(f"- {modulo.replace('_', ' ').title()}: No asignada")
            else:
                print(f"- {modulo.replace('_', ' ').title()}: {nota}")

    print("\nEXAMEN INICIAL")
    examen = camper.get("examen_inicial")

    if not examen:
        print("Examen inicial no registrado.")
    else:
        print(f"Teórica: {examen.get('teorica', 'No asignada')}")
        print(f"Práctica: {examen.get('practica', 'No asignada')}")
        print(f"Promedio: {examen.get('promedio', 'No asignado')}")
