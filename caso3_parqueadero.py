# ============================================================
#   CASO DE ESTUDIO 3: SISTEMA DE PARQUEADERO
# ------------------------------------------------------------
#   Temas aplicados:
#   - Variables y tipos de datos
#   - Operadores aritméticos
#   - Estructuras de control (if, elif, else, for, while)
#   - Funciones con parámetros y retorno
#   - Listas y diccionarios
#   - Manejo de errores (try/except)
#   - Buenas prácticas (main, comentarios, modularización)
# ============================================================

# Configuración del parqueadero
CAPACIDAD_TOTAL = 10     # cupos disponibles en total
TARIFA_CARRO    = 3000   # precio por hora para carros
TARIFA_MOTO     = 1500   # precio por hora para motos

# Lista global de vehículos actualmente en el parqueadero
vehiculos_en_parqueadero = []


# ============================================================
# FUNCIÓN: verificar si hay cupos disponibles
# ============================================================
def hay_cupo():
    # Comparamos cuántos vehículos hay con la capacidad total
    return len(vehiculos_en_parqueadero) < CAPACIDAD_TOTAL


# ============================================================
# FUNCIÓN: calcular el valor a pagar según tipo y horas
# ============================================================
def calcular_cobro(tipo, horas):
    if tipo == "carro":
        return TARIFA_CARRO * horas
    elif tipo == "moto":
        return TARIFA_MOTO * horas
    else:
        # Tipo de vehículo no reconocido
        return -1


# ============================================================
# FUNCIÓN: registrar la entrada de un vehículo
# ============================================================
def registrar_entrada(placa, tipo):
    # Verificamos si hay cupo disponible
    if not hay_cupo():
        print("  ✘ Parqueadero lleno. No hay cupos disponibles.")
        return

    # Verificamos que el tipo sea válido
    if tipo not in ["carro", "moto"]:
        print("  ✘ Tipo inválido. Use: carro o moto.")
        return

    # Verificamos que la placa no esté ya registrada
    for v in vehiculos_en_parqueadero:
        if v["placa"] == placa.upper():
            print(f"  ✘ La placa {placa.upper()} ya está en el parqueadero.")
            return

    # Registramos el vehículo como diccionario
    vehiculo = {
        "placa": placa.upper(),
        "tipo":  tipo
    }
    vehiculos_en_parqueadero.append(vehiculo)

    cupos_libres = CAPACIDAD_TOTAL - len(vehiculos_en_parqueadero)
    print(f"  ✔ {tipo.capitalize()} {placa.upper()} ingresado.")
    print(f"     Cupos disponibles restantes: {cupos_libres}")


# ============================================================
# FUNCIÓN: registrar la salida y cobrar al vehículo
# ============================================================
def registrar_salida(placa, horas):
    placa = placa.upper()

    # Buscamos el vehículo en la lista
    for v in vehiculos_en_parqueadero:
        if v["placa"] == placa:
            cobro = calcular_cobro(v["tipo"], horas)
            vehiculos_en_parqueadero.remove(v)  # lo sacamos de la lista

            print(f"  ✔ {v['tipo'].capitalize()} {placa} salió.")
            print(f"     Horas estacionado : {horas}")
            print(f"     Total a pagar     : ${cobro:,}")
            return

    # Si no encontramos la placa, avisamos
    print(f"  ✘ La placa {placa} no está registrada en el parqueadero.")


# ============================================================
# FUNCIÓN: mostrar los vehículos actualmente dentro
# ============================================================
def mostrar_parqueadero():
    print("\n--- VEHÍCULOS EN EL PARQUEADERO ---")

    if len(vehiculos_en_parqueadero) == 0:
        print("  El parqueadero está vacío.")
        return

    for v in vehiculos_en_parqueadero:
        print(f"  Placa: {v['placa']}  |  Tipo: {v['tipo']}")

    print(f"\n  Ocupados : {len(vehiculos_en_parqueadero)} / {CAPACIDAD_TOTAL}")
    print(f"  Libres   : {CAPACIDAD_TOTAL - len(vehiculos_en_parqueadero)}")


# ============================================================
# FUNCIÓN PRINCIPAL: menú interactivo del parqueadero
# ============================================================
def main():
    print("=" * 50)
    print("   SISTEMA DE PARQUEADERO - RIWI PARKING")
    print("=" * 50)

    # Menú con while: sigue mostrando opciones hasta que el usuario salga
    while True:
        print("\n¿Qué deseas hacer?")
        print("  1. Registrar entrada de vehículo")
        print("  2. Registrar salida de vehículo")
        print("  3. Ver vehículos en el parqueadero")
        print("  4. Salir del sistema")

        opcion = input("\nElige una opción (1-4): ")

        if opcion == "1":
            # --- ENTRADA ---
            placa = input("Placa del vehículo: ")
            tipo  = input("Tipo (carro / moto): ").lower()
            registrar_entrada(placa, tipo)

        elif opcion == "2":
            # --- SALIDA ---
            placa = input("Placa del vehículo que sale: ")
            try:
                horas = int(input("¿Cuántas horas estuvo? "))
            except ValueError:
                print("Horas inválidas. Se cobrarán 0 horas.")
                horas = 0
            registrar_salida(placa, horas)

        elif opcion == "3":
            # --- VER PARQUEADERO ---
            mostrar_parqueadero()

        elif opcion == "4":
            # --- SALIR ---
            print("\n¡Hasta luego! Sistema cerrado.")
            break  # Sale del while y termina el programa

        else:
            # Opción no válida
            print("  Opción inválida. Elige entre 1 y 4.")


# Punto de entrada del programa
main()
