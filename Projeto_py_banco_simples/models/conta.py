from models.cliente import Cliente

from utils.helper import formata_float_str_moeda

class Conta:

    codigo = int = 1001

    def __init__(self:object, cliente: Cliente) -> None:
        self.__numero: int = Conta.codigo
        self.__cliente: Cliente = cliente
        self.__saldo: float = 200.0
        self.__limite: float = 100.0
        self.__saldo_total: float = self._calcula_saldo_total
        Conta.codigo += 1

    @property
    def numero(self)-> int:
        return self.__numero
    
    @property
    def cliente(self)-> Cliente:
        return self.__cliente
    
    @property
    def saldo_total(self):
        return self.__saldo_total
    
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self:object, valor: float) -> None:
        self.__saldo = valor

    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self:object, valor: float) -> None:
        self.__limite = valor
    
    @property
    def _calcula_saldo_total(self) -> float:
        return self.saldo + self.limite
    
    @saldo_total.setter
    def saldo_total(self:object, valor:float) -> None:
        self.__saldo_total = valor

    def __str__(self:object) -> str:
        return f'Número da conta: {self.numero} \nCliente: {self.cliente.nome} \nSaldo total: {formata_float_str_moeda(self.saldo_total)}'


    def depositar(self,valor:float) -> str:
        if valor > 0:
            self.saldo = self.saldo + valor
            self.saldo_total = self._calcula_saldo_total

            return f'Operação bem sucedida!\nSaldo total da conta: {formata_float_str_moeda(self.saldo_total)}'
        else:
            print('Erro! Tente novamente!')


    def sacar(self,valor:float) -> str:

        if valor > 0 and self.saldo_total >= valor:

            if self.saldo >= valor:
                self.saldo = self.saldo - valor
                self.saldo_total = self._calcula_saldo_total

                return f'Saque realizado com sucesso.\n Valor total da conta {formata_float_str_moeda(self.saldo_total)}'
            else:
                restante: float = self.saldo - valor
                verifica_limite = self.limite + restante

                if verifica_limite >= 0:
                    self.saldo = 0
                    self.limite = self.limite + restante
                    self.saldo_total = self._calcula_saldo_total
                    return (f'Saque realizado! Valor total da conta: {formata_float_str_moeda(self.saldo_total)}')
                else:
                    return (f'Erro! Valor do limite insuficiente! \n Valor total da conta: {formata_float_str_moeda(self.saldo_total)}')
        else:
            return ('Saque não realizado.\nTente novamente!')


    def tranferir(self: object ,destino:object, valor: float) -> str:

        if valor > 0 and self.saldo_total >= valor:
            if self.saldo > valor:
                destino.depositar(valor)
                self.saldo = self.saldo - valor
                self.saldo_total = self._calcula_saldo_total

                return f' O valor de {formata_float_str_moeda(valor)} foi tranferido com sucesso\n Seu saldo em conta: {formata_float_str_moeda(self.saldo_total)}'
            else:
                restante: float = self.saldo - valor
                self.saldo = 0
                self.limite = self.limite + restante
                destino.depositar(valor)
                self.saldo_total = self._calcula_saldo_total

                return f' O valor de {formata_float_str_moeda(valor)} foi tranferido com sucesso\n Seu saldo em conta: {formata_float_str_moeda(self.saldo_total)} '
        else:
            print('Erro! Tente novamente!')