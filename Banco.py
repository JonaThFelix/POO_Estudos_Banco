valor = 0

class Banco:
  def __init__(self,nome,tipo):
    self.nome = nome
    self.tipo = tipo
    self.saldo = 0 #definição, sem necessidade do mét.construtor, porém chamado sempre que necessário

  def apresentacao(self):
    print(f'Nome do banco: {self.nome}\nTipo: {self.tipo}\nSaldo atual: R${self.saldo}.')
  
  def credito(self,valor): #valor sem está na class, sempre necessário chama-lo com o produto
    self.saldo += valor
    print(f'Foi acrescentado na sua conta R$ {valor}, Saldo atual: R$ {self.saldo}')

  def saque(self,valor): #valor sem está na class, sempre necessário chama-lo com o produto
    self.saldo -= valor
    print(f'Foi retirado na sua conta R$ {valor}, Saldo atual: R$ {self.saldo}')
    
