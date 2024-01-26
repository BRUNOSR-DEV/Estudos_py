from random import randint
v_estrelas = 50 * '*'
class Calcular:
    

    def __init__(self: object, dificuldade: int) -> None:

        self.__dificuldade = dificuldade
        self.__valor1: int = self._gerar_valor
        self.__valor2: int = self._gerar_valor
        self.__operacao: int = randint(1,3) # 1 somar, 2 = diminuir, 3 = multiplicar
        self.__resultado: int = self._gerar_resultado
        
    @property
    def dificuldade(self: object) ->int:
        return self.__dificuldade 
    
    @property
    def valor1(self: object) -> int:
        return self.__valor1
    
    @property
    def valor2(self: object) -> int:
        return self.__valor2
    
    @property
    def operacao(self: object) -> int:
        return self.__operacao
    
    @property
    def resultado(self: object) -> int:
        return self.__resultado
    
    
    @property
    def str_dificuldade(self: object) -> str:
        '''Retorna a dificuldade em String'''

        if self.dificuldade == 1:
            return 'Fácil (bêbe)'
        elif self.dificuldade == 2:
            return 'Médio (okay)'
        else:
            return 'Díficil (Monstro do mangue)'
        
        
        
    def __str__(self: object) -> str:
            op: str = ''
            if self.operacao == 1:
                op = 'Somar'
            elif self.operacao == 2:
                op = 'Diminuir'
            elif self.operacao == 3:
                op = 'Multiplicar'
            else:
                op = 'Operação desconhecida'
            return f'\n{v_estrelas} \nDifilculdade {self.str_dificuldade} \nOperacao: {op} \nValor 1: {self.valor1} \nValor 2: {self.valor2} '
        
    @property
    def _gerar_valor(self: object) -> int:
            if self.dificuldade == 1:
                return randint(1,10)
            elif self.dificuldade == 2:
                return randint(1,50)
            elif self.dificuldade == 3:
                return randint(1,100) 

    @property
    def _gerar_resultado(self: object) -> int:
        resultado_corr: int = 0
        if self.operacao == 1:
            resultado_corr = self.valor1 + self.valor2
        elif self.operacao == 2:
            resultado_corr = self.valor1 - self.valor2
        elif self.operacao == 3:
            resultado_corr = self.valor1 * self.valor2
        return resultado_corr
    @property
    def _op_simbolo(self: object)-> str:
        if self.operacao == 1:
            return '+'
        elif self.operacao == 2:
            return '-'
        elif self.operacao == 3:
            return '*'

    def checar_resultado(self: object, resposta) -> bool:
        certo: bool = False

        if self.resultado == resposta:
            print('            Resposta correta!')
            certo = True   
        else:
            print('            Resposta errada!')
        print(f'               {self.valor1} {self._op_simbolo} {self.valor2} = {self.resultado}')
        return certo

    @property
    def mostra_operacao(self: object) -> None:
        return f'{self.valor1} {self._op_simbolo} {self.valor2} = '