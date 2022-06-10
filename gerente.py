from funcionario import Funcionario as F

class Gerente(F):
  pass
  def __init__(self, comissao, calcula_Comissao):
    self.comissao = comissao 
    self.calcula_Comissa = calcula_Comissao
