from itertools import permutations


def nQueen(queens):
    # Quantidade de resultados achados
    Rs = 0

    cols = range(queens)
    for vec in permutations(cols):
        if queens == len(set(vec[i] + i for i in cols)) == len(set(vec[i] - i for i in cols)):
            Rs += 1
            print("\n \n".join(' # ' * i + ' Q ' + ' # ' * (queens - i - 1)
                               for i in vec) + "\n=== " + str(Rs) + '\n')

nQueen(8)
