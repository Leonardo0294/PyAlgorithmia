def missing_number(limit, array = []): 
    if len(array) == limit - 1:

        for position in array:  
            if not isinstance(position, int):
                return print("Los elementos del array deben ser enteros")
        for number in range(1, limit):
            if number not in array:
                return print(number)

missing_number(10, [1, 2, 3, 4, 6, 7, 8, 9, 10]) 