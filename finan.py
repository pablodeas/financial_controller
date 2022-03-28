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

print("Renda mensal: ", x)
print("Gastos mensais: ", y)
print("Renda menos os Gastos: ", z)
