import json

ARCHIVO = "campers.json"

def registrar_camper():

    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
    except:
        datos = {"campers": []}

    print("--------- Bienvenido al registro de Campus --------------")
    print("Por favor escribe los siguientes datos")

    identificacion = input("Digite su numero de identificación: ")
    nombre = input("Escribe tu nombre: ")
    apellidos = input("Escribe tus apellidos: ")
    direccion = input("Escribe tu direccion: ")
    acudiente = input("Escribe el nombre de tu acudiente: ")
    telefono = input("Escribe tu numero de telefono: ")

    nuevo_camper = {
        "id": identificacion,
        "nombre": nombre,
        "apellidos": apellidos,
        "direccion": direccion,
        "acudiente": acudiente,
        "telefono": telefono,
        "estado": "En proceso de ingreso",
        "riesgo": "Bajo",
        "ruta": None,
        "notas": {}
    }

    datos["campers"].append(nuevo_camper)

    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

    print("Camper registrado correctamente")
