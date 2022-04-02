# Conjunto é em chaves
numeroConjunto = {1, 3, 7, 4, 2}
print(numeroConjunto)

# Adicionar ao conjunto
numeroConjunto.add(9)
# Remover em conjunto
numeroConjunto.discard(3)

numeroConjuntoDois = {1, 3, 7, 10, 11, 14, 15}

conjuntoUniao = numeroConjunto.union(numeroConjuntoDois)
print(conjuntoUniao)

conjuntoInterseccao = numeroConjunto.intersection(numeroConjuntoDois)
print(conjuntoInterseccao)

conjuntoDiferencaUm = numeroConjunto.difference(numeroConjuntoDois)
conjuntoDiferencaDois = numeroConjuntoDois.difference(numeroConjunto)
print(f"diferença entre 1 e 2 {conjuntoDiferencaUm}")
print(f"diferença entre 2 e 1 {conjuntoDiferencaDois}")

# Diferença simétrica
conjuntoDiffSimetria = numeroConjunto.symmetric_difference(numeroConjuntoDois)

# issubset e issuperset para verificar subconjunto e superconjunto: retorna valores bolenos
# para converter lista em conjunto que não existe duplicidade set(lista)


