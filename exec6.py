numbers = [1, 2, 3, 4, 5, 6, 7 , 8, 9, 10]
result = {
    "Pares": list(filter(lambda x: x % 2 == 0, numbers)),
    "Ímpares": list(filter(lambda x: x % 2 == 1, numbers))
}
print(result)   # Sáida: {'Pares': [2, 4, 6, 8, 10], 'Ímpares': [1, 3, 5, 7, 9]}