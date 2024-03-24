def palindrome_reorder(chain):
    letters_frecuency = {}
    diferences = 0
    palindrome = ""
    aux_letter = ""

    for letter in chain:
        if letter in letters_frecuency:
            letters_frecuency[letter] += 1
        else:
            letters_frecuency[letter] = 1
            
#Corroborar que sea posible formar un palíndromo
    for value in letters_frecuency.values():
        if value % 2 != 0:
            diferences += 1
            if diferences > 1:
                return print("NO SOLUTION")
            
    for letter, count in letters_frecuency.items():
        if count % 2 == 0:
            letters_frecuency[letter] = count // 2
        elif count % 2 != 0 and count != 1:
            letters_frecuency[letter] = count -1
            aux_letter = letter

    for letter in letters_frecuency.keys():
        palindrome += letter

    if aux_letter:
        palindrome += aux_letter
    
    reversed_palindrome = palindrome[::-1]
    palindrome += reversed_palindrome[1:]
    
    return print(palindrome)


palindrome_reorder("aabbc")


def palindrome_reorder(chain):
    # Inicialización de variables
    letter_frequency = {}  # Diccionario para almacenar la frecuencia de cada letra en la cadena
    differences = 0  # Variable para contar las diferencias en la frecuencia de las letras
    palindrome = ""  # Cadena para construir el palíndromo
    aux_letter = ""  # Variable auxiliar para almacenar una letra impar

    # Calcular la frecuencia de cada letra en la cadena
    for letter in chain:
        if letter in letter_frequency:
            letter_frequency[letter] += 1
        else:
            letter_frequency[letter] = 1
            
    # Verificar si es posible formar un palíndromo con las letras proporcionadas
    for value in letter_frequency.values():
        if value % 2 != 0:
            differences += 1
            if differences > 1:
                return print("NO SOLUTION")  # Si hay más de una letra con frecuencia impar, no se puede formar un palíndromo
            
    # Ajustar la frecuencia de las letras para construir la mitad del palíndromo
    for letter, count in letter_frequency.items():
        if count % 2 == 0:
            letter_frequency[letter] = count // 2
        elif count % 2 != 0 and count != 1:
            letter_frequency[letter] = count - 1
            aux_letter = letter

    # Construir la mitad del palíndromo
    for letter in letter_frequency.keys():
        palindrome += letter

    # Agregar la letra impar (si existe) al centro del palíndromo
    if aux_letter:
        palindrome += aux_letter
    
    # Completar el palíndromo agregando su reverso
    reversed_palindrome = palindrome[::-1]
    palindrome += reversed_palindrome[1:]  # Se omite el primer carácter del reverso para evitar duplicar la letra impar
    
    # Imprimir el palíndromo resultante
    return pri
