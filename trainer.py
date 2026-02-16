import json

ARCHIVO_CAMPERS = "campers.json"
ARCHIVO_RUTAS = "rutas.json"
ARCHIVO_TRAINERS = "TRAINERS.json"

# --------------------------------- FUNCIONES AUXILIARES ---------------------------------

def cargar_campers():
    try:
        with open(ARCHIVO_CAMPERS, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except:
        return {"campers": []}

def guardar_campers(datos):
    with open(ARCHIVO_CAMPERS, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

def cargar_rutas():
    try:
        with open(ARCHIVO_RUTAS, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except:
        return {"rutas": []}

def guardar_rutas(datos):
    with open(ARCHIVO_RUTAS, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

def cargar_trainers():
    try:
        with open(ARCHIVO_TRAINERS, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except:
        return {"profesores": []}

def calcular_nota_final(teoria, practica, quizes):
    nota_final = (teoria * 0.3) + (practica * 0.6) + (quizes * 0.1)
    return round(nota_final, 2)

# --------------------------------- MENU PRINCIPAL TRAINER ---------------------------------

def menu_trainer(nombre_trainer):
    opcion = ""
    
    while opcion != "6":
        print("----------------------------------------")
        print(f"     MENU TRAINER - {nombre_trainer}")
        print("----------------------------------------")
        print("1. Ver mis rutas y campers")
        print("2. Ver mi horario de clases")
        print("3. Registrar notas de modulo")
        print("4. Ver notas de un camper")
        print("5. Ver campers en riesgo alto")
        print("6. Salir")
        print("----------------------------------------")
        
        opcion = input("Seleccione una opcion: ")
        
        if opcion == "1":
            ver_mis_rutas(nombre_trainer)
        elif opcion == "2":
            ver_horario_clases(nombre_trainer)
        elif opcion == "3":
            registrar_notas_modulo(nombre_trainer)
        elif opcion == "4":
            ver_notas_camper()
        elif opcion == "5":
            listar_campers_riesgo_alto(nombre_trainer)
        elif opcion == "6":
            print("Saliendo del modulo trainer...")
        else:
            print("Opcion invalida")

# --------------------------------- 1. VER MIS RUTAS Y CAMPERS ---------------------------------

def ver_mis_rutas(nombre_trainer):
    print("------ MIS RUTAS Y CAMPERS ------")
    
    datos_trainers = cargar_trainers()
    datos_campers = cargar_campers()
    datos_rutas = cargar_rutas()
    
    trainer_encontrado = None
    for t in datos_trainers["profesores"]:
        if t["nombre"].lower() == nombre_trainer.lower():
            trainer_encontrado = t
            break
    
    if not trainer_encontrado:
        print("Trainer no encontrado")
        return
    
    print(f"Trainer: {trainer_encontrado['nombre']}")
    print(f"Horario: {trainer_encontrado['horario']}")
    print(f"Rutas asignadas: {', '.join(trainer_encontrado['rutas'])}")
    
    # Buscar campers que tengan este trainer asignado
    mis_campers = []
    for c in datos_campers["campers"]:
        if c.get('trainer') == trainer_encontrado["nombre"] and c["estado"] == "Cursando":
            mis_campers.append(c)
    
    if not mis_campers:
        print("No tienes campers asignados actualmente")
        return
    
    # Agrupar campers por salon y horario
    clases = {}
    for c in mis_campers:
        salon = c.get('salon', 'Sin asignar')
        horario = c.get('horario', 'Sin asignar')
        jornada = c.get('jornada', 'Sin asignar')
        ruta = c.get('ruta', 'Sin asignar')
        
        clave = f"{salon}|{horario}|{jornada}|{ruta}"
        
        if clave not in clases:
            clases[clave] = []
        clases[clave].append(c)
    
    print(f"\nTienes {len(mis_campers)} campers en total")
    print("Agrupados por salon y horario:")
    
    for clave, campers in clases.items():
        partes = clave.split('|')
        salon = partes[0]
        horario = partes[1]
        jornada = partes[2]
        ruta = partes[3]
        
        print(f"\n--- CLASE: {ruta} ---")
        print(f"Salon: {salon}")
        print(f"Horario: {horario}")
        print(f"Jornada: {jornada}")
        print(f"Campers en esta clase: {len(campers)}")
        
        for c in campers:
            print(f"  - {c['nombre']} {c['apellidos']} (ID: {c['id']}) - Riesgo: {c['riesgo']}")
            if c.get('fecha_inicio') and c.get('fecha_fin'):
                print(f"    Periodo: {c['fecha_inicio']} a {c['fecha_fin']}")

def ver_horario_clases(nombre_trainer):
    print("------ MI HORARIO DE CLASES ------")
    
    datos_trainers = cargar_trainers()
    datos_campers = cargar_campers()
    
    trainer_encontrado = None
    for t in datos_trainers["profesores"]:
        if t["nombre"].lower() == nombre_trainer.lower():
            trainer_encontrado = t
            break
    
    if not trainer_encontrado:
        print("Trainer no encontrado")
        return
    
    # Buscar todas las clases del trainer
    mis_clases = []
    for c in datos_campers["campers"]:
        if c.get('trainer') == trainer_encontrado["nombre"] and c["estado"] == "Cursando":
            clase_info = {
                'salon': c.get('salon', 'N/A'),
                'horario': c.get('horario', 'N/A'),
                'jornada': c.get('jornada', 'N/A'),
                'ruta': c.get('ruta', 'N/A'),
                'fecha_inicio': c.get('fecha_inicio', 'N/A'),
                'fecha_fin': c.get('fecha_fin', 'N/A')
            }
            
            # Evitar duplicados
            if clase_info not in mis_clases:
                mis_clases.append(clase_info)
    
    if not mis_clases:
        print("No tienes clases asignadas actualmente")
        return
    
    # Separar por jornada
    clases_manana = [c for c in mis_clases if c['jornada'].lower() == 'manana']
    clases_tarde = [c for c in mis_clases if c['jornada'].lower() == 'tarde']
    
    if clases_manana:
        print("\n--- JORNADA MANANA ---")
        for clase in clases_manana:
            print(f"Ruta: {clase['ruta']}")
            print(f"  Salon: {clase['salon']}")
            print(f"  Horario: {clase['horario']}")
            print(f"  Periodo: {clase['fecha_inicio']} a {clase['fecha_fin']}")
            
            # Contar campers en esta clase
            num_campers = 0
            for c in datos_campers["campers"]:
                if (c.get('trainer') == trainer_encontrado["nombre"] and 
                    c.get('salon') == clase['salon'] and 
                    c.get('horario') == clase['horario'] and
                    c.get('ruta') == clase['ruta']):
                    num_campers += 1
            print(f"  Campers: {num_campers}")
            print()
    
    if clases_tarde:
        print("--- JORNADA TARDE ---")
        for clase in clases_tarde:
            print(f"Ruta: {clase['ruta']}")
            print(f"  Salon: {clase['salon']}")
            print(f"  Horario: {clase['horario']}")
            print(f"  Periodo: {clase['fecha_inicio']} a {clase['fecha_fin']}")
            
            # Contar campers en esta clase
            num_campers = 0
            for c in datos_campers["campers"]:
                if (c.get('trainer') == trainer_encontrado["nombre"] and 
                    c.get('salon') == clase['salon'] and 
                    c.get('horario') == clase['horario'] and
                    c.get('ruta') == clase['ruta']):
                    num_campers += 1
            print(f"  Campers: {num_campers}")
            print()

# --------------------------------- 2. REGISTRAR NOTAS DE MODULO ---------------------------------

def registrar_notas_modulo(nombre_trainer):
    print("------ REGISTRAR NOTAS POR MODULO ------")
    
    datos_campers = cargar_campers()
    datos_rutas = cargar_rutas()
    datos_trainers = cargar_trainers()
    
    trainer_encontrado = None
    for t in datos_trainers["profesores"]:
        if t["nombre"].lower() == nombre_trainer.lower():
            trainer_encontrado = t
            break
    
    if not trainer_encontrado:
        print("Trainer no encontrado")
        return
    
    rutas_del_trainer = []
    for ruta in datos_rutas["rutas"]:
        if ruta["trainer_asignado"] == trainer_encontrado["nombre"]:
            rutas_del_trainer.append(ruta)
    
    if not rutas_del_trainer:
        print("No tienes rutas activas con campers")
        return
    
    campers_disponibles = []
    for ruta in rutas_del_trainer:
        for id_camper in ruta["campers_asignados"]:
            for c in datos_campers["campers"]:
                if c["id"] == id_camper and c["estado"] == "Cursando":
                    campers_disponibles.append(c)
    
    if not campers_disponibles:
        print("No hay campers cursando en tus rutas")
        return
    
    print("Campers cursando en tus rutas:")
    for c in campers_disponibles:
        print(f"ID: {c['id']} - {c['nombre']} {c['apellidos']} - Ruta: {c['ruta']}")
    
    id_camper = input("Ingrese el ID del camper: ")
    
    camper = None
    for c in campers_disponibles:
        if c["id"] == id_camper:
            camper = c
            break
    
    if not camper:
        print("Camper no encontrado o no esta en tus rutas")
        return
    
    print("--- MODULOS DISPONIBLES ---")
    print("1. Fundamentos (Algoritmia, PSeInt y Python)")
    print("2. Web (HTML, CSS y Bootstrap)")
    print("3. Programacion Formal (JavaScript/Java/C#)")
    print("4. Bases de Datos (MongoDB/PostgreSQL/SQL Server)")
    print("5. Backend (NodeJS/Spring Boot/NetCore)")
    
    opcion_modulo = input("Seleccione el modulo: ")
    
    modulos = {
        "1": "fundamentos",
        "2": "web",
        "3": "programacion_formal",
        "4": "bases_datos",
        "5": "backend"
    }
    
    if opcion_modulo not in modulos:
        print("Opcion invalida")
        return
    
    modulo_seleccionado = modulos[opcion_modulo]
    
    if camper["notas"][modulo_seleccionado] is not None:
        print(f"Este camper ya tiene nota registrada en {modulo_seleccionado}")
        print(f"Nota actual: {camper['notas'][modulo_seleccionado]['nota_final']}")
        confirmar = input("Desea sobrescribir? (s/n): ").lower()
        if confirmar != "s":
            return
    
    print(f"--- REGISTRANDO NOTAS DE {modulo_seleccionado.upper()} ---")
    print(f"Camper: {camper['nombre']} {camper['apellidos']}")
    print(f"Ruta: {camper['ruta']}")
    print("Recuerda: La nota final se calcula como:")
    print("  30% Teoria + 60% Practica + 10% Quizes/Trabajos")
    
    while True:
        try:
            nota_teoria = float(input("Nota teorica (0-100): "))
            if 0 <= nota_teoria <= 100:
                break
            else:
                print("La nota debe estar entre 0 y 100")
        except:
            print("Por favor ingrese un numero valido")
    
    while True:
        try:
            nota_practica = float(input("Nota practica (0-100): "))
            if 0 <= nota_practica <= 100:
                break
            else:
                print("La nota debe estar entre 0 y 100")
        except:
            print("Por favor ingrese un numero valido")
    
    while True:
        try:
            nota_quizes = float(input("Nota quizes/trabajos (0-100): "))
            if 0 <= nota_quizes <= 100:
                break
            else:
                print("La nota debe estar entre 0 y 100")
        except:
            print("Por favor ingrese un numero valido")
    
    nota_final = calcular_nota_final(nota_teoria, nota_practica, nota_quizes)
    
    print("--- RESULTADO ---")
    print(f"Nota teorica (30%): {nota_teoria}")
    print(f"Nota practica (60%): {nota_practica}")
    print(f"Nota quizes (10%): {nota_quizes}")
    print(f"NOTA FINAL: {nota_final}")
    
    aprobo = nota_final >= 60
    
    if aprobo:
        print("APROBADO")
    else:
        print("REPROBADO - Rendimiento bajo")
    
    camper["notas"][modulo_seleccionado] = {
        "teoria": nota_teoria,
        "practica": nota_practica,
        "quizes": nota_quizes,
        "nota_final": nota_final,
        "aprobado": aprobo
    }
    
    if not aprobo:
        camper["riesgo"] = "Alto"
        print("ALERTA: Camper marcado como riesgo ALTO")
    
    for ruta in datos_rutas["rutas"]:
        if ruta["nombre"] == camper["ruta"]:
            if modulo_seleccionado in ruta["modulos"]:
                if aprobo:
                    ruta["modulos"][modulo_seleccionado]["estadisticas"]["aprobados"] += 1
                else:
                    ruta["modulos"][modulo_seleccionado]["estadisticas"]["reprobados"] += 1
            break
    
    guardar_campers(datos_campers)
    guardar_rutas(datos_rutas)
    
    print("Notas registradas correctamente")

# --------------------------------- 3. VER NOTAS DE CAMPER ---------------------------------

def ver_notas_camper():
    print("------ VER NOTAS DE CAMPER ------")
    
    datos_campers = cargar_campers()
    
    id_camper = input("Ingrese el ID del camper: ")
    
    camper = None
    for c in datos_campers["campers"]:
        if c["id"] == id_camper:
            camper = c
            break
    
    if not camper:
        print("Camper no encontrado")
        return
    
    print(f"--- NOTAS DE {camper['nombre']} {camper['apellidos']} ---")
    print(f"Ruta: {camper['ruta']}")
    print(f"Estado: {camper['estado']}")
    print(f"Riesgo: {camper['riesgo']}")
    
    if "notas" not in camper:
        print("No tiene notas registradas")
        return
    
    print("--- MODULOS ---")
    
    modulos_nombres = {
        "fundamentos": "Fundamentos",
        "web": "Web",
        "programacion_formal": "Programacion Formal",
        "bases_datos": "Bases de Datos",
        "backend": "Backend"
    }
    
    for modulo, nombre in modulos_nombres.items():
        print(f"{nombre}:")
        if camper["notas"][modulo] is None:
            print("  Sin evaluar")
        else:
            notas = camper["notas"][modulo]
            print(f"  Teoria: {notas['teoria']}")
            print(f"  Practica: {notas['practica']}")
            print(f"  Quizes: {notas['quizes']}")
            print(f"  NOTA FINAL: {notas['nota_final']}")
            if notas['aprobado']:
                print("  Estado: APROBADO")
            else:
                print("  Estado: REPROBADO")

# --------------------------------- 4. VER CAMPERS EN RIESGO ALTO ---------------------------------

def listar_campers_riesgo_alto(nombre_trainer):
    print("------ CAMPERS EN RIESGO ALTO (MIS RUTAS) ------")
    
    datos_campers = cargar_campers()
    datos_rutas = cargar_rutas()
    datos_trainers = cargar_trainers()
    
    trainer_encontrado = None
    for t in datos_trainers["profesores"]:
        if t["nombre"].lower() == nombre_trainer.lower():
            trainer_encontrado = t
            break
    
    if not trainer_encontrado:
        print("Trainer no encontrado")
        return
    
    rutas_del_trainer = []
    for ruta in datos_rutas["rutas"]:
        if ruta["trainer_asignado"] == trainer_encontrado["nombre"]:
            rutas_del_trainer.append(ruta)
    
    if not rutas_del_trainer:
        print("No tienes rutas activas")
        return
    
    ids_campers_trainer = []
    for ruta in rutas_del_trainer:
        ids_campers_trainer.extend(ruta["campers_asignados"])
    
    campers_riesgo = []
    for c in datos_campers["campers"]:
        if c["id"] in ids_campers_trainer and c["riesgo"].lower() == "alto":
            campers_riesgo.append(c)
    
    if not campers_riesgo:
        print("No hay campers en riesgo alto en tus rutas")
        return
    
    print(f"Total en riesgo alto: {len(campers_riesgo)}")
    
    for c in campers_riesgo:
        print(f"--- {c['nombre']} {c['apellidos']} ---")
        print(f"ID: {c['id']}")
        print(f"Ruta: {c['ruta']}")
        print(f"Estado: {c['estado']}")
        
        if "notas" in c:
            print("Modulos reprobados:")
            for modulo, notas in c["notas"].items():
                if notas is not None and not notas['aprobado']:
                    print(f"  {modulo}: {notas['nota_final']}")