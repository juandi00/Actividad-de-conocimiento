def calcular_costo_total(productos):
    """
    Función para calcular el costo total de los productos.
    
    Args:
    productos (list): Lista de precios de los productos
    
    Returns:
    float: Costo total antes del IVA
    float: Costo total después del IVA
    """
    costo_total_sin_iva = sum(productos)
    costo_total_con_iva = costo_total_sin_iva * 1.16  # IVA del 16%
    return costo_total_sin_iva, costo_total_con_iva

# Inicialización de la lista de precios de los productos
productos = []

# Captura de los precios de los 10 productos
for i in range(1, 11):
    precio = float(input(f"Ingrese el precio del producto {i}: "))
    productos.append(precio)

# Cálculo del costo total antes y después del IVA
costo_sin_iva, costo_con_iva = calcular_costo_total(productos)

# Mostrar el resultado
print(f"El costo total antes del IVA es: ${costo_sin_iva:.2f}")
print(f"El costo total después del IVA (16%) es: ${costo_con_iva:.2f}")
