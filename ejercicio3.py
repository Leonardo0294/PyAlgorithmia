def number_spiral(rows, columns):
    if rows > columns: 
        prev_area = (rows - 1) * (rows - 1)
        if rows % 2 != 0: 
            column_increment = columns
        else:
            column_increment = 2 * rows - columns
        return prev_area + column_increment
    else:
      
        prev_area = (columns - 1) * (columns - 1)

        if columns % 2 == 0: 
            row_increment = rows
        else:
            row_increment = 2 * columns - rows
            
        return prev_area + row_increment


assert number_spiral(2, 2) == 3, "Error en el caso de prueba"
print(number_spiral(4, 5))
