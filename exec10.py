from functools import reduce

meuDict = {
    'João': [8, 5, 6, 3],
    'Ana': [7, 9, 7, 3],
    'Carlos': [9, 6, 10, 3],
    'Beatriz': [5, 8, 6, 2],
    'Lucas': [5, 5, 8, 3]
}

# def calcMedia(dicionario):
#     notas = dicionario[:-1]
#     peso = dicionario[-1]
    
#     media = reduce(lambda ac, nota: ac + nota * peso, notas, 0) / (peso * len(notas))
#     return media

# medias = {aluno: calcMedia(notas) for aluno, notas in meuDict.items()}

medias = {aluno: reduce(lambda ac, nota: ac + nota * notas[-1], notas[:-1], 0) / (notas[-1] * len(notas[:-1])) for aluno, notas in meuDict.items()}
    
for aluno, media in medias.items():
    print(f"Média ponderada de {aluno}: {media:.2f}")

