def tabla_de_multiplicar(numero):
    """
    Función para generar las tablas de multiplicar del 1 al 100 de un número dado.
    
    Args:
    numero (int): El número para el cual se generarán las tablas de multiplicar
    
    Returns:
    dict: Diccionario donde las claves son los números del 1 al 100 y los valores son los resultados de la multiplicación
    """
    tabla = {}
    for i in range(1, 101):
        tabla[i] = numero * i
    return tabla

# Prueba de escritorio
numero_ingresado = int(input("Ingrese un número para generar sus tablas de multiplicar del 1 al 100: "))

# Llamada a la función para generar las tablas de multiplicar
resultado = tabla_de_multiplicar(numero_ingresado)

# Mostrar los resultados
print(f"Tablas de multiplicar del número {numero_ingresado} del 1 al 100:")
for i in range(1, 101):
    print(f"{numero_ingresado} x {i} = {resultado[i]}")


