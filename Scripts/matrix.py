def matrix(line, column):
    # other way
    # mtx = [([0] * line) for y in range(column)]
    mtx = [[0 for x in range(line)] for y in range(column)]
    return mtx
