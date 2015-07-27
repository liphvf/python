"""Doc."""


def matrix(line, column):
    """Matrix.

    Convert em matrix
    toma como base linhas e colunas
    """
    # other way
    # mtx = [([0] * line) for y in range(column)]
    mtx = [[0 for x in range(line)] for y in range(column)]
    return mtx
