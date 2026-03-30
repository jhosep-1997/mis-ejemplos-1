# ============================================================
#   CASO DE ESTUDIO COMPLETO - SISTEMA DE TIENDA
# ------------------------------------------------------------
#   Temas aplicados:
#   ✅ Variables y tipos de datos
#   ✅ Operadores aritméticos y lógicos
#   ✅ Entrada y salida de datos (input, print)
#   ✅ Estructuras de control (if, elif, else)
#   ✅ Ciclos (for, while, break, continue)
#   ✅ Funciones (def, parámetros, return)
#   ✅ Funciones lambda
#   ✅ Manejo de errores (try, except)
#   ✅ Listas
#   ✅ Tuplas
#   ✅ Diccionarios
#   ✅ Módulos e importaciones
#   ✅ JSON básico
#   ✅ CRUD (Crear, Leer, Actualizar, Eliminar)
# ============================================================


# ============================================================
# MÓDULOS E IMPORTACIONES
# ------------------------------------------------------------
# Python tiene módulos (archivos con funciones listas para usar)
# Se importan con la palabra 'import' al inicio del archivo.
# 'json'   → sirve para guardar y leer datos en formato JSON
# 'os'     → sirve para trabajar con archivos del sistema
# ============================================================

import json   # módulo para trabajar con JSON
import os     # módulo para verificar si un archivo existe


# ============================================================
# VARIABLES GLOBALES Y TIPOS DE DATOS
# ------------------------------------------------------------
# Las variables globales se definen fuera de las funciones
# para que todo el programa pueda usarlas.
#
# Tipos usados aquí:
#   str   → texto entre comillas
#   int   → número entero
#   list  → lista vacía []
# ============================================================

ARCHIVO_JSON    = "productos.json"   # str  → nombre del archivo donde guardamos datos
IMPUESTO        = 0.19               # float → 19% de IVA
productos       = []                 # list  → aquí guardamos todos los productos


# ============================================================
# TUPLA DE CATEGORÍAS PERMITIDAS
# ------------------------------------------------------------
# Una TUPLA es como una lista pero NO se puede modificar.
# Usamos tupla aquí porque las categorías son fijas,
# no queremos que nadie las cambie accidentalmente.
# ============================================================

CATEGORIAS = ("electronico", "ropa", "alimento", "hogar", "otro")
# Acceso por índice (igual que lista): CATEGORIAS[0] → "electronico"


# ============================================================
# FUNCIONES LAMBDA
# ------------------------------------------------------------
# Una lambda es una función corta escrita en una sola línea.
# Formato: lambda parametro: operacion
# Úsalas cuando la operación es simple y no necesita nombre largo.
# ============================================================

# Lambda que calcula el precio con IVA incluido
precio_con_iva = lambda precio: round(precio * (1 + IMPUESTO), 2)

# Lambda que convierte un texto a minúsculas sin espacios extra
limpiar_texto = lambda texto: texto.strip().lower()


# ============================================================
# MÓDULO JSON - GUARDAR DATOS EN ARCHIVO
# ------------------------------------------------------------
# JSON (JavaScript Object Notation) es un formato de texto
# para guardar y transportar datos.
# Se parece mucho a los diccionarios de Python.
#
# json.dump()  → convierte lista/dict de Python a JSON y lo guarda en archivo
# json.load()  → lee el archivo JSON y lo convierte a lista/dict de Python
# ============================================================

def guardar_en_json():
    """Guarda la lista de productos en el archivo JSON."""
    try:
        # Abrimos el archivo en modo escritura ("w")
        # 'ensure_ascii=False' permite guardar tildes y ñ
        # 'indent=4' hace el archivo legible con sangría de 4 espacios
        with open(ARCHIVO_JSON, "w", encoding="utf-8") as archivo:
            json.dump(productos, archivo, ensure_ascii=False, indent=4)
        print("  💾 Datos guardados correctamente en", ARCHIVO_JSON)
    except Exception as error:
        print("  ✘ Error al guardar:", error)


def cargar_desde_json():
    """Carga los productos desde el archivo JSON al iniciar el programa."""
    # Verificamos si el archivo existe antes de intentar abrirlo
    # os.path.exists() retorna True si el archivo existe
    if os.path.exists(ARCHIVO_JSON):
        try:
            with open(ARCHIVO_JSON, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)   # convierte JSON → lista Python
                # Agregamos cada producto cargado a nuestra lista global
                for producto in datos:
                    productos.append(producto)
            print(f"  📂 {len(productos)} productos cargados desde {ARCHIVO_JSON}")
        except Exception as error:
            print("  ✘ Error al cargar datos:", error)
    else:
        print("  📂 No hay archivo previo. Empezando con lista vacía.")


# ============================================================
# CRUD - CREAR (Create)
# ------------------------------------------------------------
# CRUD son las 4 operaciones básicas sobre datos:
#   C → Create  (Crear)
#   R → Read    (Leer)
#   U → Update  (Actualizar)
#   D → Delete  (Eliminar)
#
# Esta función CREA un nuevo producto y lo agrega a la lista.
# ============================================================

def crear_producto():
    print("\n--- CREAR PRODUCTO ---")

    # --- Entrada de datos con input() ---
    # input() siempre retorna un STRING, aunque el usuario escriba números
    nombre = input("Nombre del producto: ")

    # Usamos la lambda 'limpiar_texto' para quitar espacios y pasar a minúsculas
    nombre = limpiar_texto(nombre)

    # Validamos que el nombre no esté vacío
    if nombre == "":
        print("  ✘ El nombre no puede estar vacío.")
        return

    # Verificamos que no exista ya un producto con ese nombre
    # Usamos un for con una variable bandera (encontrado)
    encontrado = False
    for p in productos:
        if p["nombre"] == nombre:
            encontrado = True
            break   # break: dejamos de buscar en cuanto encontramos uno igual

    # Operador lógico: si encontrado es True, no continuamos
    if encontrado:
        print(f"  ✘ Ya existe un producto con el nombre '{nombre}'.")
        return

    # --- Entrada con manejo de errores ---
    # try/except evita que el programa se caiga si el usuario escribe texto
    try:
        precio = float(input("Precio del producto (sin IVA): "))
        stock  = int(input("Cantidad en stock: "))
    except ValueError:
        # ValueError: ocurre cuando no se puede convertir el texto a número
        print("  ✘ Precio o stock inválido. Deben ser números.")
        return

    # Validamos que precio y stock sean positivos (operador lógico 'or')
    if precio <= 0 or stock < 0:
        print("  ✘ El precio debe ser mayor a 0 y el stock no puede ser negativo.")
        return

    # Mostramos las categorías disponibles (recorremos la TUPLA con for)
    print("  Categorías disponibles:")
    for i in range(len(CATEGORIAS)):
        print(f"    {i + 1}. {CATEGORIAS[i]}")

    categoria = limpiar_texto(input("Escribe la categoría: "))

    # Verificamos que la categoría esté en la tupla
    # 'in' verifica si un valor existe dentro de una tupla o lista
    if categoria not in CATEGORIAS:
        print(f"  ✘ Categoría inválida. Opciones: {CATEGORIAS}")
        return

    # --- Creamos el producto como DICCIONARIO ---
    # Un diccionario guarda datos con clave:valor
    nuevo_producto = {
        "nombre":    nombre,           # str
        "precio":    precio,           # float
        "precio_iva": precio_con_iva(precio),  # float (usando lambda)
        "stock":     stock,            # int
        "categoria": categoria         # str
    }

    # Agregamos el diccionario a la lista global
    productos.append(nuevo_producto)

    # Guardamos automáticamente en JSON después de cada cambio
    guardar_en_json()

    print(f"  ✔ Producto '{nombre}' creado. Precio con IVA: ${precio_con_iva(precio):,}")


# ============================================================
# CRUD - LEER (Read)
# ------------------------------------------------------------
# Esta función MUESTRA todos los productos registrados.
# ============================================================

def leer_productos():
    print("\n--- LISTA DE PRODUCTOS ---")

    # Verificamos si la lista está vacía con len()
    # len() retorna la cantidad de elementos de una lista
    if len(productos) == 0:
        print("  No hay productos registrados.")
        return

    # Recorremos la lista con for
    # 'enumerate' nos da el índice y el valor al mismo tiempo
    for indice, producto in enumerate(productos):
        print(f"\n  [{indice + 1}] {producto['nombre'].upper()}")
        print(f"       Categoría  : {producto['categoria']}")
        print(f"       Precio     : ${producto['precio']:,}")
        print(f"       Precio+IVA : ${producto['precio_iva']:,}")
        print(f"       Stock      : {producto['stock']} unidades")

    print(f"\n  📦 Total de productos: {len(productos)}")


# ============================================================
# CRUD - ACTUALIZAR (Update)
# ------------------------------------------------------------
# Esta función MODIFICA los datos de un producto existente.
# ============================================================

def actualizar_producto():
    print("\n--- ACTUALIZAR PRODUCTO ---")

    if len(productos) == 0:
        print("  No hay productos para actualizar.")
        return

    nombre_buscar = limpiar_texto(input("Nombre del producto a actualizar: "))

    # Buscamos el producto en la lista
    # Guardamos la posición (índice) del producto encontrado
    indice_encontrado = -1   # -1 significa "no encontrado"

    for i in range(len(productos)):
        if productos[i]["nombre"] == nombre_buscar:
            indice_encontrado = i
            break   # dejamos de buscar en cuanto lo encontramos

    # Si sigue siendo -1, no lo encontramos
    if indice_encontrado == -1:
        print(f"  ✘ No se encontró el producto '{nombre_buscar}'.")
        return

    # Mostramos el producto actual antes de modificarlo
    producto_actual = productos[indice_encontrado]
    print(f"\n  Producto encontrado: {producto_actual['nombre']}")
    print(f"  Precio actual      : ${producto_actual['precio']:,}")
    print(f"  Stock actual       : {producto_actual['stock']}")

    # Pedimos los nuevos valores
    try:
        nuevo_precio = float(input("Nuevo precio (Enter para no cambiar): ") or producto_actual["precio"])
        nuevo_stock  = int(input("Nuevo stock  (Enter para no cambiar): ")  or producto_actual["stock"])
    except ValueError:
        print("  ✘ Valores inválidos. No se realizaron cambios.")
        return

    # Actualizamos los valores en el diccionario
    productos[indice_encontrado]["precio"]     = nuevo_precio
    productos[indice_encontrado]["precio_iva"] = precio_con_iva(nuevo_precio)
    productos[indice_encontrado]["stock"]      = nuevo_stock

    guardar_en_json()
    print(f"  ✔ Producto '{nombre_buscar}' actualizado correctamente.")


# ============================================================
# CRUD - ELIMINAR (Delete)
# ------------------------------------------------------------
# Esta función ELIMINA un producto de la lista.
# ============================================================

def eliminar_producto():
    print("\n--- ELIMINAR PRODUCTO ---")

    if len(productos) == 0:
        print("  No hay productos para eliminar.")
        return

    nombre_buscar = limpiar_texto(input("Nombre del producto a eliminar: "))

    # Buscamos el producto
    producto_a_eliminar = None   # None = "vacío" en Python

    for p in productos:
        if p["nombre"] == nombre_buscar:
            producto_a_eliminar = p
            break

    # Si producto_a_eliminar sigue siendo None, no lo encontramos
    if producto_a_eliminar is None:
        print(f"  ✘ No se encontró el producto '{nombre_buscar}'.")
        return

    # Pedimos confirmación antes de eliminar
    confirmacion = input(f"  ¿Seguro que quieres eliminar '{nombre_buscar}'? (si/no): ").lower()

    if confirmacion == "si":
        productos.remove(producto_a_eliminar)  # remove() elimina el elemento de la lista
        guardar_en_json()
        print(f"  ✔ Producto '{nombre_buscar}' eliminado.")
    else:
        print("  Eliminación cancelada.")


# ============================================================
# FUNCIÓN EXTRA: buscar productos por categoría
# ------------------------------------------------------------
# Muestra solo los productos de una categoría específica.
# Usamos 'continue' para saltar los que no coinciden.
# ============================================================

def buscar_por_categoria():
    print("\n--- BUSCAR POR CATEGORÍA ---")

    # Mostramos las categorías disponibles (recorremos la tupla)
    print("  Categorías:", CATEGORIAS)
    categoria_buscar = limpiar_texto(input("¿Qué categoría quieres ver? "))

    print(f"\n  Productos en '{categoria_buscar}':")
    encontrados = 0

    for producto in productos:
        # continue: si la categoría no coincide, saltamos este producto
        if producto["categoria"] != categoria_buscar:
            continue

        # Si llegamos aquí, el producto SÍ es de esa categoría
        print(f"  - {producto['nombre']} | Stock: {producto['stock']} | Precio+IVA: ${producto['precio_iva']:,}")
        encontrados += 1

    if encontrados == 0:
        print("  No se encontraron productos en esa categoría.")
    else:
        print(f"\n  Total encontrados: {encontrados}")


# ============================================================
# FUNCIÓN PRINCIPAL: menú interactivo con while
# ------------------------------------------------------------
# El while True mantiene el menú activo hasta que el usuario
# elija salir. Cada opción llama a una función diferente.
# ============================================================

def main():
    print("=" * 50)
    print("   SISTEMA DE TIENDA - RIWI STORE")
    print("=" * 50)

    # Cargamos los datos del archivo JSON al iniciar
    cargar_desde_json()

    # Menú principal con while True (loop infinito controlado con break)
    while True:
        print("\n¿Qué deseas hacer?")
        print("  1. Crear producto       (Create)")
        print("  2. Ver todos            (Read)")
        print("  3. Actualizar producto  (Update)")
        print("  4. Eliminar producto    (Delete)")
        print("  5. Buscar por categoría")
        print("  6. Salir")

        opcion = input("\nElige una opción (1-6): ")

        # Estructuras de control: if / elif / else
        if opcion == "1":
            crear_producto()

        elif opcion == "2":
            leer_productos()

        elif opcion == "3":
            actualizar_producto()

        elif opcion == "4":
            eliminar_producto()

        elif opcion == "5":
            buscar_por_categoria()

        elif opcion == "6":
            print("\n¡Hasta luego! Cerrando el sistema.")
            break   # break: sale del while y termina el programa

        else:
            # Si el usuario escribe algo que no es 1-6
            print("  ✘ Opción inválida. Elige un número del 1 al 6.")


# ============================================================
# PUNTO DE ENTRADA DEL PROGRAMA
# ------------------------------------------------------------
# Esta línea llama a main() para arrancar todo el programa.
# ============================================================

main()
