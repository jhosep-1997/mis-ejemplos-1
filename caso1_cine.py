# ============================================================
#   CASO DE ESTUDIO 1: SISTEMA DE CINE
# ------------------------------------------------------------
#   Temas aplicados:
#   - Variables y tipos de datos
#   - Operadores aritméticos
#   - Estructuras de control (if, for, while)
#   - Funciones con parámetros y retorno
#   - Listas y diccionarios
#   - Manejo de errores (try/except)
#   - Buenas prácticas (main, comentarios, modularización)
# ============================================================

# Lista global donde se guardan las reservas del cine
reservas = []

# Precios según el tipo de tiquete
PRECIO_ADULTO = 15000
PRECIO_NINO   = 9000
PRECIO_SENIOR = 7000


# ============================================================
# FUNCIÓN: calcular el precio según el tipo de tiquete
# ============================================================
def calcular_precio(tipo):
    if tipo == "adulto":
        return PRECIO_ADULTO
    elif tipo == "niño":
        return PRECIO_NINO
    elif tipo == "senior":
        return PRECIO_SENIOR
    else:
        # Si el tipo no es válido, retornamos -1 como señal de error
        return -1


# ============================================================
# FUNCIÓN: registrar una reserva en la lista global
# ============================================================
def registrar_reserva(nombre, pelicula, tipo, cantidad):
    precio_unitario = calcular_precio(tipo)

    # Validamos que el tipo de tiquete sea válido
    if precio_unitario == -1:
        print("  ✘ Tipo de tiquete inválido. Use: adulto, niño o senior.")
        return

    total = precio_unitario * cantidad

    # Guardamos la reserva como diccionario
    reserva = {
        "nombre":    nombre,
        "pelicula":  pelicula,
        "tipo":      tipo,
        "cantidad":  cantidad,
        "total":     total
    }
    reservas.append(reserva)
    print(f"  ✔ Reserva de {nombre} registrada. Total: ${total:,}")


# ============================================================
# FUNCIÓN: mostrar todas las reservas registradas
# ============================================================
def mostrar_reservas():
    if len(reservas) == 0:
        print("  No hay reservas registradas.")
        return

    print("\n--- RESERVAS DEL CINE ---")
    total_recaudado = 0

    for reserva in reservas:
        print(f"  Cliente : {reserva['nombre']}")
        print(f"  Película: {reserva['pelicula']}")
        print(f"  Tipo    : {reserva['tipo']} x{reserva['cantidad']}")
        print(f"  Total   : ${reserva['total']:,}")
        print("  " + "-" * 30)
        total_recaudado += reserva["total"]

    print(f"  💰 Total recaudado: ${total_recaudado:,}")


# ============================================================
# FUNCIÓN PRINCIPAL: controla todo el flujo del programa
# ============================================================
def main():
    print("=" * 50)
    print("   SISTEMA DE RESERVAS - CINE RIWI")
    print("=" * 50)

    # Pedimos cuántas reservas se van a hacer
    try:
        cantidad_reservas = int(input("\n¿Cuántas reservas vas a registrar? "))
    except ValueError:
        print("Error: ingresa un número válido.")
        return

    # Bucle para registrar cada reserva
    for i in range(cantidad_reservas):
        print(f"\n--- Reserva {i + 1} ---")
        nombre   = input("Nombre del cliente: ")
        pelicula = input("Película a ver: ")
        tipo     = input("Tipo de tiquete (adulto / niño / senior): ").lower()

        try:
            cantidad = int(input("¿Cuántas entradas? "))
        except ValueError:
            print("Cantidad inválida. Se asignará 1 entrada.")
            cantidad = 1

        registrar_reserva(nombre, pelicula, tipo, cantidad)

    # Mostramos el resumen final
    mostrar_reservas()


# Punto de entrada del programa
main()
