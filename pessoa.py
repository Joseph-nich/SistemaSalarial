from abc import ABC, abstractmethod

class Calcula(ABC):
  @abstractmethod
  def calculaSalarioLiquido(self):
    pass

class Pessoa:
  def __init__(self, nome, telefone,  endereco, cpf, salarioBruto):
    self._nome = nome
    self._telefone = telefone
    self._endereco = endereco
    self._cpf = cpf
    self._salarioBruto = salarioBruto

    #get
    @property
    def nome(self):
      return self._nome
    
    @property 
    def telefone(self):
      return self._telefone
      
    @property 
    def endereco(self):
      return self._endereco  

    @property
    def cpf(self):
      return self._cpf

    @property
    def salarioBruto(self):
      return self._salarioBruto

    
    @salarioBruto.setter
    def salarioBruto(self, valor):
      if isinstance(valor, (int,float)):
        pass
      else: 
        print("O valor informado não é numérico")
      self._salarioBruto = valor
