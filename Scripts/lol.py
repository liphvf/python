def RPcalculator():
    """Com base na faixa de preço, caulcula o custo de um heroi."""
    rp = {10: 650, 20: 1380, 40: 2800, 70: 5000, 100: 7200, 200: 15000}
    for k, v in rp.items():
        print('R$', float(k), '  ', 'RP:', int(v))

    rcompra = float(input('Digite o Valor em RP da compra: '))

    rpin = float(
        input('Digite o valor em Reais do pacote com base na tabela: '))

    rpfinal = (rpin * rcompra) / float(rp[rpin])

    print('Valor %.2f' % (rpfinal))


RPcalculator()
