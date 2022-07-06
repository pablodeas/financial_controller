# --- Uma classe que armazena dados em listas. ---
# DICIONÁRIO PABLO, DICIONÁRIO.

# Primeiro precisa ser criado um Dicionário que armazenará os valores do programa.

from datetime import date

x = date.today()
y = input("Valor: ")
q = ("15/03/1998")
z = input("Valor2: ")

data_base = {y:x, q:z}

#Para imprimir todos os valores
print(data_base)

#Para puxar a data desejada
print(data_base.get(input("Escolha a data: ")))
