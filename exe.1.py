salario=float(input("Digite o salário que você tem: "))
if salario<500:
    print("O novo salário é de", salario+0.15*salario, "Reais.")
elif salario>=500 and salario<1000:
    print("O novo salário é de", salario+0.1*salario, "Reais.")
elif salario >1000:
    print("O novo salário é de", salario+0.05*salario, "Reais.")