def palindrome_reorder(chain):
    # Se verifica si la cadena cumple con las condiciones especificadas
    if chain.isalpha() and chain.islower() and 1 <= len(chain) <= 10**6 and "ñ" not in chain:

        letters_frequency = {} 
        differences = 0  
        palindrome = ""  
        aux_letter = ""  

        # Se crea el diccionario con las letras y las veces que se repiten
        for letter in chain:
            if letter in letters_frequency:
                letters_frequency[letter] += 1
            else:
                letters_frequency[letter] = 1
                
        # Se corrobora que sea posible formar un palíndromo
        for value in letters_frequency.values():
            if value % 2 != 0:
                differences += 1
                if differences > 1:
                    return "NO SOLUTION" 
      
        for letter, count in letters_frequency.items():
            if count % 2 == 0:
                letters_frequency[letter] = count // 2
            elif count % 2 != 0 and count != 1:
                letters_frequency[letter] = count - 1
                letters_frequency[letter] = count // 2
                aux_letter = letter

        # Construir la primera mitad del palíndromo
        for letter, count in letters_frequency.items():
            while count > 0:
                palindrome += letter
                count -= 1
        if aux_letter:
            palindrome += aux_letter
        
        # Se construye la segunda mitad del palíndromo invirtiendo la primera mitad y eliminar la letra auxiliar
        reversed_palindrome = palindrome[::-1]
        palindrome += reversed_palindrome[1:]
        
        return palindrome  
    else: 
        #Se devuelve un mensaje de error si las condiciones no se cumplen
        return "La cadena no cumple con las condiciones"  

# Ejemplo de prueba
assert palindrome_reorder("aabbc") == "abcba", "Error en el caso de prueba"
print(palindrome_reorder("aabbc"))
