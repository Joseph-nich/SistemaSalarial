from pessoa import Pessoa as P

nome = input('Digite seu nome: ')
telefone = int(input('Digite seu telefone EX:83996092198 : '))
cpf = input('Digite seu CPF: ') 
salarioBruto = int(input('Digite o valor do seu salário bruto: '))
while True:
  print ('====================')
  print ('Tipos de Funções ')
  print ('====================')
  print ('opções...:')
  print ('1- Funcionário ')
  print ('2- Secretário')
  print ('3- Secretario Executivo')
  print ('4- Gerente')
  operacao=input('Você faz qual função:')
  if (operacao == '1'):
   desconto = float(input('Digite seu Desconto: '))
   calculaDesconto = desconto / 100
   salario_Liquido = salarioBruto - calculaDesconto 
   bonificacao = float(input("Digite sua bonificação?"))
   salario_final = salario_Liquido + bonificacao
   break
   
  elif(operacao == '2'):
   desconto = float(input('Digite seu desconto: '))
   calculaDesconto = desconto / 100
   salario_Liquido = salarioBruto - calculaDesconto 
   bonificacao = float(input("Digite sua bonificação?"))
   salario_final = salario_Liquido + bonificacao
   break
   

  elif (operacao == '3'):
   desconto = float(input('Digite seu desconto: '))
   calculaDesconto = desconto / 100
   salario_Liquido = salarioBruto - calculaDesconto 
   bonificacao = float(input("Digite sua bonificação?"))
   salario_final = salario_Liquido + bonificacao
   break

  elif (operacao == '4'):
   desconto = float(input('Digite seu desconto: '))
   calculaDesconto = desconto / 100
   salario_Liquido = salarioBruto - calculaDesconto 
   bonificacao = float(input("Digite sua bonificacao ?"))
   comissao = float(input('Digite sua comissão: '))
   calcula_comissao = comissao / 100 + salario_Liquido
   salario_final = salario_Liquido + bonificacao + calcula_comissao
   break
print ('processando...')
print('==============')  
print('Seu resultado')
print('==============')  
print ("Nome:", nome)
print ("Fone:", telefone)
print ("CPF:", cpf)
print ("Seu salário final é:", salario_final)   
  
