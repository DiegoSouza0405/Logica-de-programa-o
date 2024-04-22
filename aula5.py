"""
Desenvolva um programa que calcule o reajuste salarial, conforme o salario do funcionario
1)salario de até R$2000: aumento de 20%
2)salario entre R$2000 e R$3500: aumento de 15%
3)salario entre R$3500 e R$5000: aumento de 10%
4)salario maior que R$5000: aumento de 5%.
O que precisa aparecer com resultado:
-salario atual
-percentual de aumento
-valor em R$ do aumento
-Novo salario (incluindo aumento)
"""
salario_atual = float(input("Informe o seu salário atual:"))

if salario_atual < 2000:
    print("Salário atual:",salario_atual)
    print("O seu salário receberá um aumento 20%")
    novo_salario = salario_atual*1.2
    valor_do_aumento_em_real = novo_salario - salario_atual
    print("Valor do aumento em R$:", valor_do_aumento_em_real)
    print("O seu novo salário é R$ ", novo_salario)
elif 2000 <= salario_atual < 3500:
    print("Salário atual:" ,salario_atual)
    print("O seu salário receberá um aumento 15%")
    novo_salario = salario_atual*1.15
    valor_do_aumento_em_real = novo_salario - salario_atual
    print("Valor do aumento em R$:", valor_do_aumento_em_real)
    print("O seu novo salário é R$", novo_salario)
elif 3500 <= salario_atual < 5000:
    novo_salario = salario_atual * 1.0
    valor_do_aumento_em_real = novo_salario - salario_atual
    print("Valor do aumento em R$:", valor_do_aumento_em_real)
    print("O seu salário é R$", novo_salario)
else:
    print("Salário atual:", salario_atual)
    novo_salario = salario_atual * 1.05
    valor_do_aumento_em_real = novo_salario - salario_atual
    print("Valor do aumento em R$:", valor_do_aumento_em_real)
    print("O seu salário é R$ ", novo_salario)


