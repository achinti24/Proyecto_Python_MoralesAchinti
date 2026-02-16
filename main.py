import json
from coordinador import menu_coordinador
from trainer import menu_trainer
from camper import menu_camper
from registrarse import registrar_camper

def cargar_usuarios():
    try:
        with open("usuarios.json", "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

def cargar_campers():
    try:
        with open("campers.json", "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []


def main():
    while True:
        print("\n----------------------------------------")
        print("   BIENVENIDO A CAMPUSLANDS")
        print("----------------------------------------")
        print("1. Iniciar sesión")
        print("2. Registrarse como camper")
        print("3. Salir")
        print("----------------------------------------")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            usuarios = cargar_usuarios()
            datos_campers = cargar_campers()

            correo = input("Correo electrónico: ")
            password = input("Contraseña: ")

            # ===== LOGIN USUARIOS (COORDINADOR / TRAINER) =====
            usuario_encontrado = False

            for usuario in usuarios:
                if usuario["correo"] == correo and usuario["password"] == password:
                    usuario_encontrado = True
                    print("Inicio de sesión exitoso")

                    if usuario["rol"] == "coordinador":
                        menu_coordinador()

                    elif usuario["rol"] == "trainer":
                        nombre_trainer = usuario.get("nombre", "Trainer")
                        menu_trainer(nombre_trainer)

                    break

            if usuario_encontrado:
                continue

            # ===== LOGIN CAMPER =====
            camper_logueado = None

            for camper in datos_campers["campers"]:
                if camper.get("correo") == correo and camper.get("password") == password:
                    camper_logueado = camper
                    break

            if camper_logueado:
                print(f"\n Bienvenido {camper_logueado['nombre']} {camper_logueado['apellidos']}")
                menu_camper(camper_logueado)
            else:
                print(" Correo o contraseña incorrectos")

        elif opcion == "2":
            registrar_camper()

        elif opcion == "3":
            print("Hasta luego ")
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()