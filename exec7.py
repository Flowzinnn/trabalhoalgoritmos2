numbers = [1, 3, -2, 5, 19, 0, 3, -15, 0, 19, -8, 7]
result = {
    "Positivos": list(filter(lambda x: x > 0, numbers)),
    "Negativos": list(filter(lambda x: x < 0, numbers)),
    "Zeros": list(filter(lambda x: x == 0, numbers))
}
print(result) # Saída: {'Positivos': [1, 3, 5, 19, 3, 19, 7], 'Negativos': [-2, -15, -8], 'Zeros': [0, 0]}