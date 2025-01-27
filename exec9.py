tupleList = [(9, 6, 5, 5), (10, 6, 1), (10, 4, 3, 5), (4, 3), (10, 6, 10, 4)]
verifyMedia5 = list(filter(lambda x: x > 5,(map(lambda x: sum(x) / len(x), tupleList))))
print(f" As médias maiores que 5 são: ",verifyMedia5) # Saída: [6.25, 5.666666666666667, 5.5, 7.5]
