import json

ARCHIVO_TRAINERS = "TRAINERS.json"
ARCHIVO_CAMPERS = "campers.json"
ARCHIVO_RUTAS = "rutas.json"

# ==================== FUNCIONES AUXILIARES ====================

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

def guardar_trainers(datos):
    with open(ARCHIVO_TRAINERS, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

# ==================== CRUD TRAINERS ====================

def crud_trainers():
    datos = cargar_trainers()
    opcion = ""

    while opcion != "5":
        print("====== CRUD TRAINERS ======")
        print("1. Crear trainer")
        print("2. Mostrar trainers")
        print("3. Actualizar trainer")
        print("4. Eliminar trainer")
        print("5. Volver")

        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre del trainer: ")
            horario = input("Horario (ej: 6am a 2pm): ")
            rutas = input("Rutas (separadas por coma, ej: NodeJS, Java): ").split(",")

            # Generar ID automático
            if len(datos["profesores"]) > 0:
                ultimo_id = max([t["id"] for t in datos["profesores"]])
                nuevo_id = ultimo_id + 1
            else:
                nuevo_id = 1

            nuevo = {
                "id": nuevo_id,
                "nombre": nombre,
                "horario": horario,
                "rutas": [r.strip() for r in rutas]
            }

            datos["profesores"].append(nuevo)
            guardar_trainers(datos)
            print("Trainer creado correctamente")
            
        elif opcion == "2":
            if not datos["profesores"]:
                print("No hay trainers registrados")
            else:
                print("--- LISTADO DE TRAINERS ---")
                for t in datos["profesores"]:
                    print(f"ID: {t['id']}")
                    print(f"Nombre: {t['nombre']}")
                    print(f"Horario: {t['horario']}")
                    print(f"Rutas: {', '.join(t['rutas'])}")
                    
        elif opcion == "3":
            nombre_buscar = input("Nombre del trainer a actualizar: ").lower()
            encontrado = False

            for t in datos["profesores"]:
                if t["nombre"].lower() == nombre_buscar:
                    encontrado = True
                    print("Trainer encontrado")

                    while True:
                        print(f"¿Qué desea actualizar de {t['nombre']}?")
                        print("1. Cambiar nombre")
                        print("2. Cambiar horario")
                        print("3. Cambiar rutas")
                        print("4. Salir")

                        opcion_edit = input("Seleccione una opción: ")

                        if opcion_edit == "1":
                            t["nombre"] = input("Nuevo nombre: ")
                        elif opcion_edit == "2":
                            t["horario"] = input("Nuevo horario: ")
                        elif opcion_edit == "3":
                            nuevas_rutas = input("Nuevas rutas (separadas por coma): ")
                            t["rutas"] = [r.strip() for r in nuevas_rutas.split(",")]
                        elif opcion_edit == "4":
                            print("Saliendo de edición...")
                            break
                        else:
                            print("Opción no válida")
                            continue
                            
                        guardar_trainers(datos)
                        print(" Trainer actualizado correctamente")
                    break

            if not encontrado:
                print(" Trainer no encontrado")

        elif opcion == "4":
            nombre_eliminar = input("Nombre del trainer a eliminar: ").lower()
            nuevos = [t for t in datos["profesores"] if t["nombre"].lower() != nombre_eliminar]

            if len(nuevos) == len(datos["profesores"]):
                print(" Trainer no encontrado")
            else:
                datos["profesores"] = nuevos
                guardar_trainers(datos)
                print(" Trainer eliminado correctamente")

# ==================== CRUD CAMPERS ====================

def crud_campers():
    datos = cargar_campers()
    opcion = ""

    while opcion != "4":
        print("====== CRUD CAMPERS ======")
        print("1. Mostrar campers")
        print("2. Actualizar camper")
        print("3. Eliminar camper")
        print("4. Volver")

        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            if not datos["campers"]:
                print("No hay campers registrados")
            else:
                print("--- LISTADO DE CAMPERS ---")
                for c in datos["campers"]:
                    print(f"\nID: {c['id']}")
                    print(f"Nombre: {c['nombre']} {c['apellidos']}")
                    print(f"Dirección: {c['direccion']}")
                    print(f"Teléfono: {c['telefono']}")
                    print(f"Acudiente: {c['acudiente']}")
                    print(f"Estado: {c['estado']}")
                    print(f"Riesgo: {c['riesgo']}")
                    print(f"Ruta: {c['ruta']}")
                    
        elif opcion == "2":
            id_buscar = input("ID del camper a actualizar: ")
            encontrado = False

            for c in datos["campers"]:
                if c["id"] == id_buscar:
                    encontrado = True
                    print("Camper encontrado")

                    while True:
                        print(f"¿QUÉ DESEA ACTUALIZAR DE {c['nombre']}?")
                        print("1. Cambiar nombre y apellido")
                        print("2. Cambiar dirección")
                        print("3. Cambiar acudiente")
                        print("4. Cambiar número telefónico")
                        print("5. Cambiar estado")
                        print("6. Cambiar riesgo")
                        print("7. Salir")

                        opcion_edit = input("Seleccione una opción: ")

                        if opcion_edit == "1":
                            c["nombre"] = input("Nuevo nombre: ")
                            c["apellidos"] = input("Nuevos apellidos: ")
                        elif opcion_edit == "2":
                            c["direccion"] = input("Nueva dirección: ")
                        elif opcion_edit == "3":
                            c["acudiente"] = input("Nuevo acudiente: ")
                        elif opcion_edit == "4":
                            c["telefono"] = input("Nuevo teléfono: ")
                        elif opcion_edit == "5":
                            c["estado"] = input("Nuevo estado: ")
                        elif opcion_edit == "6":
                            c["riesgo"] = input("Nuevo riesgo: ")
                        elif opcion_edit == "7":
                            print("Saliendo de edición...")
                            break
                        else:
                            print("Opción no válida")
                            continue
                            
                        guardar_campers(datos)
                        print("Camper actualizado correctamente")
                    break

            if not encontrado:
                print(" Camper no encontrado")
                
        elif opcion == "3":
            id_eliminar = input("ID del camper a eliminar: ")
            nuevos = [c for c in datos["campers"] if c["id"] != id_eliminar]

            if len(nuevos) == len(datos["campers"]):
                print(" Camper no encontrado")
            else:
                datos["campers"] = nuevos
                guardar_campers(datos)
                print("Camper eliminado correctamente")

# ==================== MÓDULO EXAMEN INICIAL ====================

def registrar_examen_inicial():
    print("====== REGISTRAR EXAMEN INICIAL ======")
    
    datos = cargar_campers()
    
    if not datos["campers"]:
        print("No hay campers registrados")
        return
    
    # Mostrar solo campers en proceso de ingreso
    campers_disponibles = []
    for c in datos["campers"]:
        if c["estado"].lower() == "en proceso de ingreso":
            campers_disponibles.append(c)
    
    if not campers_disponibles:
        print("No hay campers en proceso de ingreso para evaluar")
        return
    
    print("Campers disponibles para examen:")
    for c in campers_disponibles:
        print(f"ID: {c['id']} - Nombre: {c['nombre']} {c['apellidos']}")
    
    id_camper = input("Ingrese el ID del camper: ")
    
    # Buscar el camper
    camper_encontrado = None
    for c in datos["campers"]:
        if c["id"] == id_camper:
            camper_encontrado = c
            break
    
    if not camper_encontrado:
        print(" Camper no encontrado")
        return
    
    if camper_encontrado["estado"].lower() != "en proceso de ingreso":
        print(" Este camper no está en proceso de ingreso")
        return
    
    print(f"Registrando examen para: {camper_encontrado['nombre']} {camper_encontrado['apellidos']}")
    
    # Pedir notas
    while True:
        try:
            nota_teorica = float(input("Nota teórica (0-100): "))
            if 0 <= nota_teorica <= 100:
                break
            else:
                print("La nota debe estar entre 0 y 100")
        except:
            print("Por favor ingrese un número válido")
    
    while True:
        try:
            nota_practica = float(input("Nota práctica (0-100): "))
            if 0 <= nota_practica <= 100:
                break
            else:
                print("La nota debe estar entre 0 y 100")
        except:
            print("Por favor ingrese un número válido")
    
    # Calcular promedio
    promedio = (nota_teorica + nota_practica) / 2
    
    print(f"--- RESULTADO ---")
    print(f"Nota teórica: {nota_teorica}")
    print(f"Nota práctica: {nota_practica}")
    print(f"Promedio: {promedio}")
    
    # Guardar notas en el camper
    if "examen_inicial" not in camper_encontrado:
        camper_encontrado["examen_inicial"] = {}
    
    camper_encontrado["examen_inicial"]["teorica"] = nota_teorica
    camper_encontrado["examen_inicial"]["practica"] = nota_practica
    camper_encontrado["examen_inicial"]["promedio"] = promedio
    
    # Cambiar estado según resultado
    if promedio >= 60:
        camper_encontrado["estado"] = "Aprobado"
        print(" ¡APROBADO! El camper puede matricularse")
    else:
        camper_encontrado["estado"] = "Reprobado"
        print(" REPROBADO. El camper no aprobó el examen inicial")
    
    guardar_campers(datos)
    print("Examen registrado correctamente")

def ver_resultados_examenes():
    print("====== RESULTADOS DE EXÁMENES ======")
    
    datos = cargar_campers()
    
    if not datos["campers"]:
        print("No hay campers registrados")
        return
    
    campers_con_examen = []
    for c in datos["campers"]:
        if "examen_inicial" in c:
            campers_con_examen.append(c)
    
    if not campers_con_examen:
        print("No hay exámenes registrados")
        return
    
    for c in campers_con_examen:
        print(f"--- {c['nombre']} {c['apellidos']} ---")
        print(f"ID: {c['id']}")
        print(f"Nota teórica: {c['examen_inicial']['teorica']}")
        print(f"Nota práctica: {c['examen_inicial']['practica']}")
        print(f"Promedio: {c['examen_inicial']['promedio']}")
        print(f"Estado: {c['estado']}")

def menu_examen_inicial():
    opcion = ""
    
    while opcion != "3":
        print("====== MENÚ EXAMEN INICIAL ======")
        print("1. Registrar examen inicial")
        print("2. Ver resultados de exámenes")
        print("3. Volver")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_examen_inicial()
        elif opcion == "2":
            ver_resultados_examenes()
        elif opcion == "3":
            print("Volviendo al menú principal...")
        else:
            print("Opción inválida")

# ==================== MÓDULO MATRÍCULA ====================

def calcular_fecha_fin(fecha_inicio):
    """Calcula la fecha de fin sumando exactamente 10 meses a la fecha de inicio"""
    try:
        partes = fecha_inicio.split("/")
        dia = int(partes[0])
        mes = int(partes[1])
        anio = int(partes[2])
        
        # Sumar 10 meses
        mes += 10
        
        # Ajustar año si los meses pasan de 12
        while mes > 12:
            mes -= 12
            anio += 1
        
        # Formatear fecha
        return f"{dia:02d}/{mes:02d}/{anio}"
    except:
        return "Error en fecha"

def obtener_salones_disponibles():
    """Retorna lista de salones disponibles"""
    return ["Apolo", "Artemis", "Sputnik"]

def obtener_horarios_por_jornada(jornada):
    """Retorna los horarios disponibles según la jornada"""
    if jornada.lower() == "mañana" or jornada.lower() == "manana":
        return ["6am-10am", "10am-2pm"]
    elif jornada.lower() == "tarde":
        return ["2pm-6pm", "6pm-10pm"]
    else:
        return []

def verificar_disponibilidad_trainer(trainer, salon, horario, datos_rutas):
    """Verifica si un trainer está disponible en ese salón y horario"""
    for ruta in datos_rutas["rutas"]:
        if ruta["trainer_asignado"] == trainer["nombre"]:
            if ruta["salon"] == salon and ruta["horario"] == horario:
                return False
    return True

def matricular_camper():
    print("====== MATRICULAR CAMPER ======")
    
    import random
    
    datos_campers = cargar_campers()
    datos_rutas = cargar_rutas()
    datos_trainers = cargar_trainers()
    
    # Mostrar campers aprobados
    campers_aprobados = []
    for c in datos_campers["campers"]:
        if c["estado"] == "Aprobado" and c["ruta"] is None:
            campers_aprobados.append(c)
    
    if not campers_aprobados:
        print("No hay campers aprobados disponibles para matricular")
        return
    
    print("Campers aprobados disponibles:")
    for c in campers_aprobados:
        print(f"ID: {c['id']} - {c['nombre']} {c['apellidos']}")
    
    id_camper = input("Ingrese el ID del camper a matricular: ")
    
    # Buscar camper
    camper = None
    for c in datos_campers["campers"]:
        if c["id"] == id_camper:
            camper = c
            break
    
    if not camper:
        print(" Camper no encontrado")
        return
    
    if camper["estado"] != "Aprobado":
        print(" Este camper no está aprobado")
        return
    
    if camper["ruta"] is not None:
        print(" Este camper ya está matriculado")
        return
    
    # Preguntar jornada
    print("--- JORNADA ---")
    print("1. Mañana (6am-10am / 10am-2pm)")
    print("2. Tarde (2pm-6pm / 6pm-10pm)")
    
    opcion_jornada = input("Seleccione la jornada: ")
    
    if opcion_jornada == "1":
        jornada = "mañana"
    elif opcion_jornada == "2":
        jornada = "tarde"
    else:
        print(" Jornada inválida")
        return
    
    # Obtener horarios disponibles para la jornada
    horarios_disponibles = obtener_horarios_por_jornada(jornada)
    
    # Preguntar fecha de inicio
    print("Ingrese la fecha de inicio (formato: DD/MM/YYYY)")
    fecha_inicio = input("Fecha: ")
    
    # Calcular fecha de fin (10 meses después)
    fecha_fin = calcular_fecha_fin(fecha_inicio)
    
    # Buscar rutas con cupos disponibles
    rutas_con_cupos = []
    for ruta in datos_rutas["rutas"]:
        if len(ruta["campers_asignados"]) < ruta["capacidad_maxima"]:
            rutas_con_cupos.append(ruta)
    
    if not rutas_con_cupos:
        print("No hay rutas con cupos disponibles")
        return
    
    # Obtener salones disponibles
    salones = obtener_salones_disponibles()
    
    # Intentar asignar automáticamente
    asignacion_exitosa = False
    intentos = 0
    max_intentos = 100
    
    while not asignacion_exitosa and intentos < max_intentos:
        intentos += 1
        
        # Seleccionar aleatoriamente: ruta, horario, salón
        ruta_random = random.choice(rutas_con_cupos)
        horario_random = random.choice(horarios_disponibles)
        salon_random = random.choice(salones)
        
        # Buscar trainers que enseñen esta ruta
        trainers_disponibles = []
        for trainer in datos_trainers["profesores"]:
            tiene_ruta = False
            for r in trainer["rutas"]:
                if r.lower() == ruta_random["nombre"].lower():
                    tiene_ruta = True
                    break
            
            if tiene_ruta:
                # Verificar disponibilidad (que no esté en ese salón y horario)
                if verificar_disponibilidad_trainer(trainer, salon_random, horario_random, datos_rutas):
                    trainers_disponibles.append(trainer)
        
        # Si hay trainers disponibles, asignar
        if trainers_disponibles:
            trainer_seleccionado = random.choice(trainers_disponibles)
            
            # Asignar camper a la ruta
            ruta_random["campers_asignados"].append(id_camper)
            ruta_random["trainer_asignado"] = trainer_seleccionado["nombre"]
            ruta_random["salon"] = salon_random
            ruta_random["horario"] = horario_random
            ruta_random["fecha_inicio"] = fecha_inicio
            ruta_random["fecha_fin"] = fecha_fin
            
            # Actualizar camper
            camper["ruta"] = ruta_random["nombre"]
            camper["estado"] = "Cursando"
            camper["jornada"] = jornada
            
            # Inicializar notas por módulo
            camper["notas"] = {
                "fundamentos": None,
                "web": None,
                "programacion_formal": None,
                "bases_datos": None,
                "backend": None
            }
            
            # Guardar cambios
            guardar_rutas(datos_rutas)
            guardar_campers(datos_campers)
            
            print(" MATRÍCULA EXITOSA (ASIGNACIÓN AUTOMÁTICA)")
            print(f"Camper: {camper['nombre']} {camper['apellidos']}")
            print(f"Ruta: {ruta_random['nombre']}")
            print(f"Trainer: {trainer_seleccionado['nombre']}")
            print(f"Salón: {salon_random}")
            print(f"Jornada: {jornada.capitalize()}")
            print(f"Horario: {horario_random}")
            print(f"Fecha inicio: {fecha_inicio}")
            print(f"Fecha fin: {fecha_fin} (10 meses después)")
            
            asignacion_exitosa = True
    
    if not asignacion_exitosa:
        print("No se pudo asignar automáticamente.")
        print("No hay trainers disponibles en los salones y horarios de la jornada seleccionada.")
        print("Intenta con otra jornada o verifica la disponibilidad de trainers.")

def ver_matriculados():
    print("====== CAMPERS MATRICULADOS ======")
    
    datos_campers = cargar_campers()
    
    campers_matriculados = []
    for c in datos_campers["campers"]:
        if c["ruta"] is not None:
            campers_matriculados.append(c)
    
    if not campers_matriculados:
        print("No hay campers matriculados")
        return
    
    for c in campers_matriculados:
        print(f"--- {c['nombre']} {c['apellidos']} ---")
        print(f"ID: {c['id']}")
        print(f"Ruta: {c['ruta']}")
        print(f"Estado: {c['estado']}")
        print(f"Riesgo: {c['riesgo']}")

def ver_rutas_y_cupos():
    print("====== RUTAS Y CUPOS DISPONIBLES ======")
    
    datos_rutas = cargar_rutas()
    
    for ruta in datos_rutas["rutas"]:
        cupos_ocupados = len(ruta["campers_asignados"])
        cupos_disponibles = ruta["capacidad_maxima"] - cupos_ocupados
        
        print(f"--- {ruta['nombre']} ({ruta['id']}) ---")
        print(f"Capacidad máxima: {ruta['capacidad_maxima']}")
        print(f"Cupos ocupados: {cupos_ocupados}")
        print(f"Cupos disponibles: {cupos_disponibles}")
        
        if ruta["trainer_asignado"]:
            print(f"Trainer: {ruta['trainer_asignado']}")
            print(f"Salón: {ruta['salon']}")
            print(f"Horario: {ruta['horario']}")
        
        if ruta["campers_asignados"]:
            print("Campers asignados:")
            datos_campers = cargar_campers()
            for id_camper in ruta["campers_asignados"]:
                for c in datos_campers["campers"]:
                    if c["id"] == id_camper:
                        print(f"  - {c['nombre']} {c['apellidos']}")

def menu_matricula():
    opcion = ""
    
    while opcion != "4":
        print("====== MENÚ MATRÍCULA ======")
        print("1. Matricular camper")
        print("2. Ver campers matriculados")
        print("3. Ver rutas y cupos disponibles")
        print("4. Volver")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            matricular_camper()
        elif opcion == "2":
            ver_matriculados()
        elif opcion == "3":
            ver_rutas_y_cupos()
        elif opcion == "4":
            print("Volviendo al menú principal...")
        else:
            print("Opción inválida")

# ==================== MÓDULO REPORTES ====================

def reporte_inscritos():
    print("====== REPORTE DE INSCRITOS ======")
    
    datos = cargar_campers()
    
    inscritos = []
    for c in datos["campers"]:
        if c["estado"].lower() == "en proceso de ingreso" or c["estado"].lower() == "inscrito":
            inscritos.append(c)
    
    if not inscritos:
        print("No hay campers inscritos")
        return
    
    print(f"Total de inscritos: {len(inscritos)}")
    print("--- LISTADO ---")
    
    for c in inscritos:
        print(f"ID: {c['id']}")
        print(f"Nombre: {c['nombre']} {c['apellidos']}")
        print(f"Dirección: {c['direccion']}")
        print(f"Teléfono: {c['telefono']}")
        print(f"Acudiente: {c['acudiente']}")
        print(f"Estado: {c['estado']}")

def reporte_aprobados():
    print("====== REPORTE DE APROBADOS ======")
    
    datos = cargar_campers()
    
    aprobados = []
    for c in datos["campers"]:
        if c["estado"] == "Aprobado":
            aprobados.append(c)
    
    if not aprobados:
        print("No hay campers aprobados")
        return
    
    print(f"Total de aprobados: {len(aprobados)}")
    print("--- LISTADO ---")
    
    for c in aprobados:
        print(f"ID: {c['id']}")
        print(f"Nombre: {c['nombre']} {c['apellidos']}")
        if "examen_inicial" in c:
            print(f"Promedio examen: {c['examen_inicial']['promedio']}")

def reporte_bajo_rendimiento():
    print("====== REPORTE DE CAMPERS CON BAJO RENDIMIENTO ======")
    
    datos = cargar_campers()
    
    bajo_rendimiento = []
    for c in datos["campers"]:
        if c["riesgo"].lower() == "alto":
            bajo_rendimiento.append(c)
    
    if not bajo_rendimiento:
        print("No hay campers con bajo rendimiento")
        return
    
    print(f"Total en riesgo alto: {len(bajo_rendimiento)}")
    print("--- LISTADO ---")
    
    for c in bajo_rendimiento:
        print(f"\n--- {c['nombre']} {c['apellidos']} ---")
        print(f"ID: {c['id']}")
        print(f"Ruta: {c['ruta']}")
        print(f"Estado: {c['estado']}")
        
        if "notas" in c:
            print("Módulos con problemas:")
            for modulo, notas in c["notas"].items():
                if notas is not None and not notas['aprobado']:
                    print(f"  ✗ {modulo}: {notas['nota_final']} - REPROBADO")

def reporte_por_ruta():
    print("====== REPORTE POR RUTA ======")
    
    datos_campers = cargar_campers()
    datos_rutas = cargar_rutas()
    
    print("Rutas disponibles:")
    for ruta in datos_rutas["rutas"]:
        print(f"{ruta['id']} - {ruta['nombre']}")
    
    id_ruta = input("Ingrese el ID de la ruta (ej: R1): ").upper()
    
    ruta_seleccionada = None
    for ruta in datos_rutas["rutas"]:
        if ruta["id"] == id_ruta:
            ruta_seleccionada = ruta
            break
    
    if not ruta_seleccionada:
        print(" Ruta no encontrada")
        return
    
    print(f"====== REPORTE RUTA {ruta_seleccionada['nombre']} ======")
    
    # Información general
    cupos_ocupados = len(ruta_seleccionada["campers_asignados"])
    cupos_disponibles = ruta_seleccionada["capacidad_maxima"] - cupos_ocupados
    
    print(f"--- INFORMACIÓN GENERAL ---")
    print(f"Capacidad máxima: {ruta_seleccionada['capacidad_maxima']}")
    print(f"Campers asignados: {cupos_ocupados}")
    print(f"Cupos disponibles: {cupos_disponibles}")
    
    if ruta_seleccionada["trainer_asignado"]:
        print(f"Trainer: {ruta_seleccionada['trainer_asignado']}")
        print(f"Salón: {ruta_seleccionada['salon']}")
        print(f"Horario: {ruta_seleccionada['horario']}")
        print(f"Fecha inicio: {ruta_seleccionada['fecha_inicio']}")
        print(f"Fecha fin: {ruta_seleccionada['fecha_fin']}")
    
    # Campers en esta ruta
    if ruta_seleccionada["campers_asignados"]:
        print(f"--- CAMPERS EN ESTA RUTA ---")
        for id_camper in ruta_seleccionada["campers_asignados"]:
            for c in datos_campers["campers"]:
                if c["id"] == id_camper:
                    print(f"\n{c['nombre']} {c['apellidos']} (ID: {c['id']})")
                    print(f"  Estado: {c['estado']}")
                    print(f"  Riesgo: {c['riesgo']}")
    
    # Estadísticas por módulo
    print(f"--- ESTADÍSTICAS POR MÓDULO ---")
    
    modulos_nombres = {
        "fundamentos": "Fundamentos",
        "web": "Web",
        "programacion_formal": "Programación Formal",
        "bases_datos": "Bases de Datos",
        "backend": "Backend"
    }
    
    for modulo_key, modulo_nombre in modulos_nombres.items():
        if modulo_key in ruta_seleccionada["modulos"]:
            stats = ruta_seleccionada["modulos"][modulo_key]["estadisticas"]
            total = stats["aprobados"] + stats["reprobados"]
            
            print(f"{modulo_nombre}:")
            print(f"  Aprobados: {stats['aprobados']}")
            print(f"  Reprobados: {stats['reprobados']}")
            print(f"  Total evaluados: {total}")
            
            if total > 0:
                porcentaje = (stats['aprobados'] / total) * 100
                print(f"  Porcentaje de aprobación: {porcentaje:.1f}%")

def reporte_general():
    print("====== REPORTE GENERAL DEL SISTEMA ======")
    
    datos_campers = cargar_campers()
    datos_rutas = cargar_rutas()
    datos_trainers = cargar_trainers()
    
    # Contar por estado
    total_campers = len(datos_campers["campers"])
    
    conteo_estados = {
        "En proceso de ingreso": 0,
        "Aprobado": 0,
        "Reprobado": 0,
        "Cursando": 0
    }
    
    conteo_riesgo = {
        "Bajo": 0,
        "Alto": 0
    }
    
    for c in datos_campers["campers"]:
        if c["estado"] in conteo_estados:
            conteo_estados[c["estado"]] += 1
        
        riesgo = c["riesgo"].capitalize()
        if riesgo in conteo_riesgo:
            conteo_riesgo[riesgo] += 1
    
    print(f"--- ESTADÍSTICAS GENERALES ---")
    print(f"Total de campers: {total_campers}")
    print(f"Por estado:")
    for estado, cantidad in conteo_estados.items():
        print(f"  {estado}: {cantidad}")
    
    print(f"Por riesgo:")
    for riesgo, cantidad in conteo_riesgo.items():
        print(f"  {riesgo}: {cantidad}")
    
    # Información de rutas
    print(f"--- RUTAS ---")
    print(f"Total de rutas: {len(datos_rutas['rutas'])}")
    
    for ruta in datos_rutas["rutas"]:
        cupos_ocupados = len(ruta["campers_asignados"])
        print(f"{ruta['nombre']}:")
        print(f"  Campers: {cupos_ocupados}/{ruta['capacidad_maxima']}")
    
    # Información de trainers
    print(f"--- TRAINERS ---")
    print(f"Total de trainers: {len(datos_trainers['profesores'])}")

def menu_reportes():
    opcion = ""
    
    while opcion != "6":
        print("====== MENÚ REPORTES ======")
        print("1. Listar inscritos")
        print("2. Listar aprobados")
        print("3. Listar campers con bajo rendimiento")
        print("4. Reporte por ruta")
        print("5. Reporte general del sistema")
        print("6. Volver")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            reporte_inscritos()
        elif opcion == "2":
            reporte_aprobados()
        elif opcion == "3":
            reporte_bajo_rendimiento()
        elif opcion == "4":
            reporte_por_ruta()
        elif opcion == "5":
            reporte_general()
        elif opcion == "6":
            print("Volviendo al menú principal...")
        else:
            print("Opción inválida")

# ==================== MENÚ PRINCIPAL COORDINADOR ====================

def menu_coordinador():
    opcion = ""

    while opcion != "7":
        print("========================================")
        print("     MENÚ COORDINADOR")
        print("========================================")
        print("1. CRUD Campers")
        print("2. CRUD Trainers")
        print("3. Examen Inicial")
        print("4. Matrícula")
        print("5. Reportes")
        print("6. Ver campers en riesgo alto")
        print("7. Salir")
        print("========================================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crud_campers()
        elif opcion == "2":
            crud_trainers()
        elif opcion == "3":
            menu_examen_inicial()
        elif opcion == "4":
            menu_matricula()
        elif opcion == "5":
            menu_reportes()
        elif opcion == "6":
            reporte_bajo_rendimiento()
        elif opcion == "7":
            print("Saliendo del módulo coordinador...")
        else:
            print("Opción inválida")