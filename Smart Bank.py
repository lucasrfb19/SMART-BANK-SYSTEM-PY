bem_vindo = f"""
    -------Bem-Vindo ao Smart Bank-------
"""

print(bem_vindo)

opcao = int(input("""
    -------INFORME A OPÇÃO DESEJADA:
                  
           [1] - DEPÓSITO 
           [2] - SAQUE               
           [3] - EXTRATO: 
  """))

if opcao == 2:
   print("ERRO 421: É necessário ter saldo em conta para sacar!!!")
   opcao = int(input("""
    -------INFORME A OPÇÃO DESEJADA:
                  
           [1] - DEPÓSITO 
           [2] - SAQUE               
           [3] - EXTRATO: 
  """))

if opcao == 3:
   print("ERRO 422: É necessário ter saldo em conta para exibir o extrato!!!")
   opcao = int(input("""
    -------INFORME A OPÇÃO DESEJADA:
                  
           [1] - DEPÓSITO 
           [2] - SAQUE               
           [3] - EXTRATO: 
  """))

if opcao == 1:
   deposito = float(input("Informe o valor a ser depositado: R$ "))
   
if deposito >= 1:
   opcao = int(input("""
    -------DEPÓSITO REALIZADO COM SUCESSO! INFORME A OPÇÃO DESEJADA:
                  
           [1] - DEPÓSITO 
           [2] - SAQUE               
           [3] - EXTRATO: 
  """))
      
  
if opcao == 2:
   saque = float(input("Informe o valor a ser sacado: R$ "))

elif opcao == 3:
   extrato = deposito 
   print(extrato)


if saque >= 1:
   opcao = int(input("""
    -------SAQUE REALIZADO COM SUCESSO, DESEJA REALIZAR OUTRA OPERAÇÃO?:
                  
           [1] - DEPÓSITO 
           [2] - SAQUE               
           [3] - EXTRATO: 
  """))

if opcao == 3:
   extrato = deposito - saque
   print(extrato)




   