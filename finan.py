# --- Programa de Controle Financeiro ---
import tkinter as tk

print("Abaixo você terá uma conta básica. Essa conta determinará se você está mantendo uma vida financeira estável!. \n")

x = int(input("Digite a soma de todos os valores recebidos mensalmente: \n"))
y = int(input("Digite a soma de todos os seus gastos mensais: \n"))
z = x-y

if x - y < z:
    print("Os seus gastos estão acima de 1/3 da sua renda. \n")
elif x - y == z:
    print("Os seus gastos estão exatamente 1/3 da sua renda. \n")
elif x - y > z:
    print("Os seus gastos estão acima de 1/3 da sua renda, continue assim!. \n")

print("Renda mensal total: ", x)
print("Gastos mensais totais: ", y)
print("Renda menos os Gastos: ", z)

# --- Abaixo o banco de dados. ---

# Primeiro precisa ser criado um Dicionário que armazenará os valores do programa.

#from datetime import date

#x = date.today()
#y = input("Valor: ")
#q = ("15/03/1998")
#z = input("Valor2: ")

#data_base = {y:x, q:z}

#Para imprimir todos os valores
#print(data_base)

#Para puxar a data desejada
#print(data_base.get(input("Escolha a data: ")))





