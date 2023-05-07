from Banco import Banco
def i():
  print('-'*70)
  print('\n')

#definição do objeto = Banco 1
banco1 = Banco('Agiobank','Conta corrente')

#aprentação inicial
banco1.apresentacao() 
i()

#credito (+)
banco1.credito(1000.50) 
i()
banco1.credito(40.22)
i()

#débito (-)
banco1.saque(0.72)
i()

#apresentação final pós crédito/débito
banco1.apresentacao()
