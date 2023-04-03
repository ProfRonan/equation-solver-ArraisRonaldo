decisao = int(input("Digite o tipo de equação: "))

if decisao < 1 or decisao > 2:
    print("Grau inválido")
elif decisao == 1:
    print("A equação é do primeiro grau")
    a = int(input("Digite o valor de a: "))
    b = int(input("Digite o valor de b: "))
    if a == 0:
      print("Valor de a inválido")
    elif a !=0:
       print(f"{a}x + {b} = 0")  
elif decisao == 2:
   print("A equação é do segundo grau")
   a = int(input("Digite o valor de a: "))
   b = int(input("Digite o valor de b: "))
   c = int(input("Digite o valor de a: "))
   if a == 0:
      print("Valor de a inválido")
   elif a !=0:
       print(f"{a}x² + {b}x + {c} = 0")  
       if (b*b) - 4*a*c < 0:
          print("A equação não possui raízes reais")
       elif (b*b) - 4*a*c == 0:
          print("A equação possui apenas uma raiz real")
       elif (b*b) - 4*a*c > 0:
           print("A equação possui duas raízes reais")