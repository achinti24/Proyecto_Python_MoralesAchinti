import json

ARCHIVO_TRAINERS = "TRAINERS.json"
ARCHIVO_CAMPERS = "campers.json"

def cargar_trainers():
    try:
        with open(ARCHIVO_TRAINERS, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except:
        return []

def guardar_trainers(datos):
    with open(ARCHIVO_TRAINERS, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

def crear_trainer():
    datos = cargar_trainers()

    nombre = input("Nombre del trainer: ")
    horario = input("Horario: ")
    rutas = input("Rutas (separadas por coma): ").split(",")

    nuevo_trainer = {
        "nombre": nombre,
        "horario": horario,
        "rutas": [r.strip() for r in rutas]
    }

    datos.append(nuevo_trainer)
    guardar_trainers(datos)

    print("Trainer creado correctamente")

def mostrar_trainers():
    datos = cargar_trainers()

    if not datos:
        print("No hay trainers disponibles")
        return

    print("=== TRAINERS DISPONIBLES ===")
    for t in datos:
        print(t)

def actualizar_trainer():
    datos = cargar_trainers()
    nombre_buscar = input("Nombre del trainer a actualizar: ").lower()

    for t in datos:
        if t["nombre"].lower() == nombre_buscar:
            print("Trainer encontrado")

            t["nombre"] = input("Nuevo nombre: ")
            t["horario"] = input("Nuevo horario: ")
            t["rutas"] = input("Nuevas rutas (separadas por coma): ").split(",")

            guardar_trainers(datos)
            print("Trainer actualizado correctamente")
            return

    print("Trainer no encontrado")

def eliminar_trainer():
    datos = cargar_trainers()
    nombre_eliminar = input("Nombre del trainer a eliminar: ").lower()

    nuevos = [t for t in datos if t["nombre"].lower() != nombre_eliminar]

    if len(nuevos) == len(datos):
        print("Trainer no encontrado")
        return

    guardar_trainers(nuevos)
    print("Trainer eliminado correctamente")

def cargar_campers():
    try:
        with open(ARCHIVO_CAMPERS, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except:
        return []

def guardar_campers(datos):
    with open(ARCHIVO_CAMPERS, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

def mostrar_campers():
    datos = cargar_campers()

    if not datos["campers"]:
        print("No hay campers registrados")
        return

    print("=== CAMPERS ===")
    for c in datos["campers"]:
        print(f"""
ID: {c["id"]}
Nombre: {c["nombre"]}
Apellidos: {c["apellidos"]}
Dirección: {c["direccion"]}
Acudiente: {c["acudiente"]}
Teléfono: {c["telefono"]}
Estado: {c["estado"]}
Riesgo: {c["riesgo"]}
Ruta: {c["ruta"]}
----------------------------
""")

def actualizar_camper():
    datos = cargar_campers()
    id_buscar = input("ID del camper a actualizar: ")

    for c in datos:
        if c["id"] == id_buscar:
            print("Camper encontrado")

            c["nombre"] = input("Nuevo nombre: ")
            c["apellidos"] = input("Nuevos apellidos: ")
            c["direccion"] = input("Nueva direccion: ")
            c["acudiente"] = input("Nuevo acudiente: ")
            c["telefono"] = input("Nuevo telefono: ")
            c["estado"] = input("Nuevo estado: ")
            c["riesgo"] = input("Nuevo riesgo: ")

            guardar_campers(datos)
            print("Camper actualizado correctamente")
            return

    print("Camper no encontrado")

def eliminar_camper():
    datos = cargar_campers()
    id_eliminar = input("ID del camper a eliminar: ")

    nuevos = [c for c in datos if c["id"] != id_eliminar]

    if len(nuevos) == len(datos):
        print("Camper no encontrado")
        return

    guardar_campers(nuevos)
    print("Camper eliminado correctamente")

def menu_coordinador():

    opcion = ""

    while opcion != "3":

        print("====== MENÚ COORDINADOR ======")
        print("1. Gestionar Trainers")
        print("2. Gestionar Campers")
        print("3. Salir")
        print("===============================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_trainers()

        elif opcion == "2":
            menu_campers()

        elif opcion == "3":
            print("Saliendo del sistema...")

        else:
            print("Opción inválida")


def menu_trainers():
    opcion = ""
    while opcion != "5":
        print("====== MENÚ TRAINERS ======")
        print("1. Crear trainer")
        print("2. Mostrar trainers")
        print("3. Actualizar trainer")
        print("4. Eliminar trainer")
        print("5. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_trainer()
        elif opcion == "2":
            mostrar_trainers()
        elif opcion == "3":
            actualizar_trainer()
        elif opcion == "4":
            eliminar_trainer()


def menu_campers():
    opcion = ""
    while opcion != "4":
        print("====== MENÚ CAMPERS ======")
        print("1. Mostrar campers")
        print("2. Actualizar camper")
        print("3. Eliminar camper")
        print("4. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_campers()
        elif opcion == "2":
            actualizar_camper()
        elif opcion == "3":
            eliminar_camper()
