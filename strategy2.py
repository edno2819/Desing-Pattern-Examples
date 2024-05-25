from abc import ABC, abstractmethod


class Trader:
    def executar_trade(self, tipo_estrategia, tipo_gerenciamento, dados_mercado):
        if tipo_estrategia == 'estrategia1':
            # Lógica da estratégia 1
            pass
        elif tipo_estrategia == 'estrategia2':
            # Lógica da estratégia 2
            pass
        # ... outras estratégias

        if tipo_gerenciamento == 'gerenciamento1':
            # Lógica do gerenciamento 1
            pass
        elif tipo_gerenciamento == 'gerenciamento2':
            # Lógica do gerenciamento 2
            pass
        # ... outros gerenciamentos


class EstrategiaNegociacao(ABC):
    @abstractmethod
    def executar(self, dados_mercado):
        pass


class EstrategiaMomentum(EstrategiaNegociacao):
    def executar(self, dados_mercado):
        print("Executando estratégia de momentum")
        return "Trade executado com estratégia de momentum"


class EstrategiaReversao(EstrategiaNegociacao):
    def executar(self, dados_mercado):
        print("Executando estratégia de reversão")
        return "Trade executado com estratégia de reversão"


class GerenciamentoBanca(ABC):
    @abstractmethod
    def gerenciar(self, saldo_atual):
        pass


class GerenciamentoFixo(GerenciamentoBanca):
    def gerenciar(self, saldo_atual):
        print("Gerenciando banca com método fixo")
        return saldo_atual * 0.01


class GerenciamentoProporcional(GerenciamentoBanca):
    def gerenciar(self, saldo_atual):
        print("Gerenciando banca com método proporcional")
        return saldo_atual * 0.05


class Trader:
    def __init__(self, estrategia: EstrategiaNegociacao, gerenciamento: GerenciamentoBanca):
        self.estrategia = estrategia
        self.gerenciamento = gerenciamento

    def executar_trade(self, dados_mercado, saldo_atual):
        trade = self.estrategia.executar(dados_mercado)
        novo_saldo = self.gerenciamento.gerenciar(saldo_atual)
        print(f"--------------------------")
        print(f"Resultado do trade: {trade}")
        print(f"Novo saldo: {novo_saldo}")
        print(f"--------------------------")



trader1 = Trader(EstrategiaMomentum(), GerenciamentoFixo())
trader2 = Trader(EstrategiaReversao(), GerenciamentoProporcional())

# Executa um trade com os dados do mercado e o saldo atual
dados_mercado = {"preco_atual": 100, "volume": 500}
saldo_atual = 10000

trader1.executar_trade(dados_mercado, saldo_atual)
trader2.executar_trade(dados_mercado, saldo_atual)

