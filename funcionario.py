from pessoa import Pessoa as P

class Funcionario(P):
  pass
  def __init__(self, desconto, bonificacao, salario_Liquido):
    self.desconto = desconto
    self.bonificacao = bonificacao
    self.salario_Liquido = salario_Liquido

  @property 
  def desconto(self):
    return self.desconto

  @property 
  def bonificacao(self):
    return self.bonificacao

  @property 
  def salario_Liquido(self):
    return self.salario_Liquido 
  

  @salario_Liquido.setter
  def salario_Liquido(self, valor):
    if isinstance(valor, (int, float)):
      pass
    else: 
      print("O valor informado não é numérico")
    self.salario_Liquido = valor
