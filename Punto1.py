def factorial(n):
    """
    Función para calcular el factorial de un número entero positivo n.
    
    Args:
    n (int): Número entero positivo
    
    Returns:
    int: Factorial de n
    """
    if n < 0:
        return None  # No se puede calcular el factorial de números negativos
    elif n == 0:
        return 1  # El factorial de 0 es 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Pruebas de escritorio
print(factorial(5))  # El factorial de 5 es 120
print(factorial(0))  # El factorial de 0 es 1
print(factorial(-3))  # No se puede calcular el factorial de números negativos
