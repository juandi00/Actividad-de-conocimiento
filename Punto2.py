def calcular_rangos_de_edad(edades):
    """
    Función para calcular el total de personas por rango de edades.
    
    Args:
    edades (list): Lista de edades de las personas
    
    Returns:
    dict: Diccionario con el total de personas por rango de edades
    """
    rangos = {
        "0-20": 0,
        "21-30": 0,
        "31-40": 0,
        "41-60": 0,
        "mayores de 60": 0
    }
    
    for edad in edades:
        if edad <= 20:
            rangos["0-20"] += 1
        elif 21 <= edad <= 30:
            rangos["21-30"] += 1
        elif 31 <= edad <= 40:
            rangos["31-40"] += 1
        elif 41 <= edad <= 60:
            rangos["41-60"] += 1
        else:
            rangos["mayores de 60"] += 1
    
    return rangos

# Prueba de escritorio
edades = [18, 25, 35, 42, 55, 63, 17, 29, 47, 70]

# Llamada a la función para calcular los rangos de edad
resultado = calcular_rangos_de_edad(edades)

# Mostrar los resultados
for rango, total in resultado.items():
    print(f"Personas en el rango de edad {rango}: {total}")
