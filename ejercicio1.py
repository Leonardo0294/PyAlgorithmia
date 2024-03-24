def weird_algorithm(n):
    secuencia = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = (n * 3) + 1
        secuencia.append(n)
    return secuencia

num = int(input(" Imprime un axel aleatorio: "))

print("")
print(*weird_algorithm(num))
