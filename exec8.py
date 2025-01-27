from functools import reduce
words = ["casa", "python", "lambda"]
counterWords = reduce(lambda x, y: x + y, map(len, words), 0)
print(counterWords)