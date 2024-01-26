from models.calcular import Calcular

def main()-> None:
    pontos: int = 0
    jogar(pontos)

def jogar(pontos: int) -> None:
    try:
        ob = True
        while ob == True:
            escolha_dificuldade: int = int(input('Escolha seu nível de dificuldade: \n[1] Facil \n[2] Médio \n[3] Díficil \nDigite: '))
            if escolha_dificuldade > 0 and escolha_dificuldade < 4:
                nv_dificuldade = escolha_dificuldade
                break
            else:
                print('Tente colocar um número correspondente. TENTE NOVAMENTE!')
    except(ValueError) as err:
        print('Valor invalido!, tente novamente com os números 1,2 ou 3 ')

    jogo1: Calcular = Calcular(nv_dificuldade)
    print(jogo1)
    print(jogo1.mostra_operacao)

    resposta = int(input('Digite a resposta: '))

    
    if jogo1.checar_resultado(resposta):
        pontos = pontos + 1
        print(f'           Sua pontuação é: {pontos}')

    try:
        res = input('Deseja continuar ? \n[sS] Sim \n[nN] Não \nDigite:')

        if res== 's':
            jogar(pontos)
        else:
            print(f'Seus pontos: {pontos}')

    except(ValueError) as err:
        print('O valor esperado é [S] sim, ou [N] Não - \nTente Novamente! ')


if __name__ == '__main__':
    main()






    