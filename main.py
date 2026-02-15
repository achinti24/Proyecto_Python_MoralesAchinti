import json
from coordinador import menu_coordinador
from registrarse import registrar_camper
from trainer import menu_trainer

def cargar_usuarios():
    try:
        with open("usuarios.json", "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

def main():
    while True:
        print("----------------------------------------")
        print("   BIENVENIDO A CAMPUSLANDS")
        print("----------------------------------------")
        print("1. Iniciar sesion")
        print("2. Registrarse como camper")
        print("3. Salir")
        print("----------------------------------------")
        
        try:
            opcion = input("Seleccione una opcion: ")
        except:
            print("Opcion invalida")
            continue
        
        if opcion == "1":
            usuarios = cargar_usuarios()
            
            correo = input("Correo electronico: ")
            contraseña = input("Contraseña: ")
            
            encontrado = False
            
            for usuario in usuarios:
                if usuario["correo"] == correo and usuario["password"] == contraseña:
                    print("Inicio de sesion exitoso")
                    
                    if usuario["rol"] == "coordinador":
                        print(f"Bienvenido, {usuario.get('nombre', 'Coordinador')}")
                        menu_coordinador()
                    elif usuario["rol"] == "trainer":
                        if "nombre" in usuario:
                            nombre_trainer = usuario["nombre"]
                            print(f"Bienvenido, {nombre_trainer}")
                        else:
                            nombre_trainer = input("Ingrese su nombre completo: ")
                        
                        menu_trainer(nombre_trainer)
                    
                    encontrado = True
                    break
            
            if not encontrado:
                print("Correo o contraseña incorrectos")
                
        elif opcion == "2":
            registrar_camper()
            
        elif opcion == "3":
            print("Hasta luego!")
            break
            
        else:
            print("Opcion invalida")

if __name__ == "__main__":
    main()