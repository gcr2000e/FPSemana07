class Pagamento():
    def __init__(self, valor):
        self.valor = valor
    
    def processar_pagamento(self, valor):
        self.valor = valor

class CartaoCredito(Pagamento):
    def __init__(self, num_cartao, nome, val, ccv):
        self.num_cartao = num_cartao
        self.nome = nome
        self.val = val
        self.ccv = ccv
    
    def processar_pagamento(self, valor):
        print(f"€{valor:0.2f} com Cartão de Crédito ({self.num_cartao})")

class PayPal(Pagamento):
    def __init__(self, email):
        self.email = email

    def processar_pagamento(self, valor):
        print(f"€{valor:.2f} com PayPal (e-mail: {self.email})")

class TransferenciaBancaria(Pagamento):
    def __init__(self, banco, agencia, conta):
        self.banco = banco
        self.agencia = agencia
        self.conta = conta

    def processar_pagamento(self, valor):
        print(f"€{valor:.2f} com Transferência Bancária banco: ({self.banco}, conta: {self.conta})")

def realizar_pagamento(pagamento, valor):
    pagamento.processar_pagamento(valor)

cartao_credito = CartaoCredito(num_cartao = "1234 5678 9012 3456", nome="João Silva", val = "12/25", ccv = "123") 
paypal = PayPal(email = "joao.silva@email.com")
transferencia = TransferenciaBancaria(banco = "Banco Central", agencia = "1234", conta = "12345678")

realizar_pagamento(cartao_credito, 150.00) 
realizar_pagamento(paypal, 200.00) 
realizar_pagamento(transferencia, 300.00)