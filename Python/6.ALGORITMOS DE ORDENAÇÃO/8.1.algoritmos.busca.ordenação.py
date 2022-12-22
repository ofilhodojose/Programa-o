def executar_quicksort_2(lista):
    if len(lista) <= 1: return lista
    pivo = lista[0]
    iguais = [valor for valor in lista if valor == pivo]
    menores = [valor for valor in lista if valor < pivo]
    maiores = [valor for valor in lista if valor > pivo]
    return executar_quicksort_2(menores) + iguais + executar_quicksort_2(maiores)

lista = [10, 9, 5, 8, 11, -1, 3]
executar_quicksort_2(lista)