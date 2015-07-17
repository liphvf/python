"""so we can test D100."""


def move_disc(qtd_discs, src, dest, aux):
    """Explicação.
    quantidade de peças = qtd_discs
    origem = src
    destino = dest
    auxiliar = aux
    """
    if qtd_discs == 0:
        pass

    else:

        move_disc(qtd_discs - 1, src, aux, dest)
        print('Move o Disco ' + str(qtd_discs) +
              ' de ' + src + ' para ' + dest)

        move_disc(qtd_discs - 1, aux, dest, src)


move_disc(3, 'A', 'C', 'B')
