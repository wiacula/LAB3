def mnoz_macierze(macierz1, macierz2):
    wiersze1 = len(macierz1)
    kolumny1 = len(macierz1[0])
    wiersze2 = len(macierz2)
    kolumny2 = len(macierz2[0]) # przypisuje wymiary macierzy wejsciowych do zmiennych

    if kolumny1 != wiersze2:
        raise ValueError("Nieprawidłowe wymiary macierzy!")

    wynik = [[0 for n in range(kolumny2)] for n in range(wiersze1)] # macierz zerowa

    for i in range(wiersze1):
        for j in range(kolumny2):
            for k in range(kolumny1):
                wynik[i][j] += macierz1[i][k] * macierz2[k][j]

    return wynik


# Przykład użycia
macierz1 = [
    [1, 2, 3],
    [4, 5, 6]
]

macierz2 = [
    [7, 8],
    [9, 10],
    [11, 12]
]

wynik = mnoz_macierze(macierz1, macierz2)

print(wynik[0])
print(wynik[1])