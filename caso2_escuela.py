# ============================================================
#   CASO DE ESTUDIO 2: SISTEMA DE ESCUELA
# ------------------------------------------------------------
#   Temas aplicados:
#   - Variables y tipos de datos
#   - Operadores aritméticos
#   - Estructuras de control (if, elif, else, for)
#   - Funciones con parámetros y retorno
#   - Listas y diccionarios
#   - Manejo de errores (try/except)
#   - Buenas prácticas (main, comentarios, modularización)
# ============================================================

# Lista global donde guardamos todos los estudiantes
estudiantes = []


# ============================================================
# FUNCIÓN: determinar el estado según el promedio
# ============================================================
def obtener_estado(promedio):
    if promedio >= 90:
        return "Excelente"
    elif promedio >= 80:
        return "Sobresaliente"
    elif promedio >= 70:
        return "Aprobado"
    elif promedio >= 60:
        return "En riesgo"
    else:
        return "Reprobado"


# ============================================================
# FUNCIÓN: calcular el promedio de tres notas
# ============================================================
def calcular_promedio(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3


# ============================================================
# FUNCIÓN: registrar un estudiante con sus notas
# ============================================================
def registrar_estudiante(nombre, nota1, nota2, nota3):
    promedio = calcular_promedio(nota1, nota2, nota3)
    estado   = obtener_estado(promedio)

    # Guardamos toda la info del estudiante en un diccionario
    estudiante = {
        "nombre":   nombre,
        "nota1":    nota1,
        "nota2":    nota2,
        "nota3":    nota3,
        "promedio": promedio,
        "estado":   estado
    }
    estudiantes.append(estudiante)
    print(f"  ✔ '{nombre}' registrado. Promedio: {promedio:.1f} → {estado}")


# ============================================================
# FUNCIÓN: calcular el promedio general del salón
# ============================================================
def promedio_salon():
    if len(estudiantes) == 0:
        return 0
    suma = 0
    for est in estudiantes:
        suma += est["promedio"]
    return suma / len(estudiantes)


# ============================================================
# FUNCIÓN: mostrar el reporte completo del salón
# ============================================================
def mostrar_reporte():
    if len(estudiantes) == 0:
        print("  No hay estudiantes registrados.")
        return

    print("\n--- REPORTE DEL SALÓN ---")

    # Contadores para estadísticas
    aprobados  = 0
    reprobados = 0

    for est in estudiantes:
        print(f"  Estudiante: {est['nombre']}")
        print(f"  Notas     : {est['nota1']} | {est['nota2']} | {est['nota3']}")
        print(f"  Promedio  : {est['promedio']:.1f}")
        print(f"  Estado    : {est['estado']}")
        print("  " + "-" * 30)

        # Contamos aprobados y reprobados
        if est["promedio"] >= 70:
            aprobados += 1
        else:
            reprobados += 1

    # Mostramos estadísticas generales
    print(f"\n  📊 Total estudiantes : {len(estudiantes)}")
    print(f"  ✅ Aprobados         : {aprobados}")
    print(f"  ❌ Reprobados        : {reprobados}")
    print(f"  📈 Promedio del salón: {promedio_salon():.2f}")


# ============================================================
# FUNCIÓN PRINCIPAL: controla todo el flujo del programa
# ============================================================
def main():
    print("=" * 50)
    print("   SISTEMA DE NOTAS - ESCUELA RIWI")
    print("=" * 50)

    # Pedimos cuántos estudiantes se van a registrar
    try:
        cantidad = int(input("\n¿Cuántos estudiantes vas a registrar? "))
    except ValueError:
        print("Error: ingresa un número válido.")
        return

    # Bucle para registrar cada estudiante
    for i in range(cantidad):
        print(f"\n--- Estudiante {i + 1} ---")
        nombre = input("Nombre del estudiante: ")

        # Pedimos las 3 notas con manejo de error para cada una
        try:
            nota1 = float(input("Nota 1 (0-100): "))
            nota2 = float(input("Nota 2 (0-100): "))
            nota3 = float(input("Nota 3 (0-100): "))
        except ValueError:
            print("Nota inválida. Se asignarán 0 en las notas incorrectas.")
            nota1 = nota2 = nota3 = 0

        registrar_estudiante(nombre, nota1, nota2, nota3)

    # Mostramos el reporte final del salón
    mostrar_reporte()


# Punto de entrada del programa
main()
