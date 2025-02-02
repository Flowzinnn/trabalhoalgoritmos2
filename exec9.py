tupleList = [(9, 6, 5, 5), (10, 6, 1), (10, 4, 3, 5), (4, 3), (10, 6, 10, 4)]
verifyMedia5 = list(filter(lambda x: sum(x) / len(x) > 5, tupleList))
print(f" As tuplas com médias maiores que 5 são: ",verifyMedia5) # Saída: [(9, 6, 5, 5), (10, 6, 1), (10, 4, 3, 5), (10, 6, 10, 4)]
