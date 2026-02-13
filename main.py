import json
from coordinador import menu_coordinador
from registrarse import registrar_camper


def cargar_usuarios():
    try:
        with open("usuarios.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

print("------BIENVENIDO A CAMPUSLAND--------")
print("1. iniciar sesion")
print("2. registrarse")
print("3. salir")

opcion = int(input("seleccione una opcion: "))

if opcion == 1:
    usuarios = cargar_usuarios()

    correo = input("escriba su correo electronico: ")
    contraseña = input("escriba su contraseña: ")

    encontrado = False

    for usuario in usuarios:
        if usuario["correo"] == correo and usuario["password"] == contraseña:
            print("Inicio de sesión exitoso")
            if usuario["rol"] == "coordinador":
                menu_coordinador()

        encontrado = True
        break
    if not encontrado:
        print("Correo o contraseña incorrectos")
elif opcion == 2:
    registrar_camper()
