def missing_number(n, numbers):
    # Calcula la suma total esperada de los números de 1 a n
    expected_sum = n * (n + 1) // 2
    
    # Calcula la suma real de los números dados
    actual_sum = sum(numbers)
    
    # El número faltante es la diferencia entre la suma esperada y la suma real
    missing = expected_sum - actual_sum
    
    return missing

# Prueba del caso de prueba dado
assert missing_number(5, [1, 2, 4, 5]) == 3, "Error en el caso de prueba"


