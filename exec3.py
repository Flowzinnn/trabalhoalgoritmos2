from functools import reduce
sumAllNumbers = reduce(lambda x, y: x + y, [1, 2, 3, 4])
print(sumAllNumbers) # Saída: 10