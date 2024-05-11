while True:
    salarioAtual=float(input("Digite o valor do seu salário: "))
    salarioAtual = float(salarioAtual)

    if salarioAtual < 280:
        print(f"O valor do salário antes do reajuste era de R$ {salarioAtual} reais")
        print("Foi aplicado 20% no aumento baseado no salário.")

        aumento = (salarioAtual * 20)/100
        print(f"O valor do aumento foi de R$ {aumento} reais.")

        novoSalario = salarioAtual + aumento
        print(f"O novo salário após o aumento é de R$ {novoSalario} reais.")

        salarioReal = salarioAtual - (salarioAtual * 0.038)
        print(f"Valor do salário real, descontando a inflação: {salarioReal}")

    elif salarioAtual >= 280 and salarioAtual < 699:

        print(f"O valor do salário antes do reajuste era de R$ {salarioAtual} reais")
        print("Foi aplicado 15% no aumento baseado no salário.")

        aumento = (salarioAtual * 15)/100
        print(f"O valor do aumento foi de R$ {aumento},00 reais.")

        novoSalario = salarioAtual + aumento
        print(f"O novo salário após o aumento é de R$ {novoSalario} reais.")

        salarioReal = salarioAtual - (salarioAtual * 0.038)
        print(f"Valor do salário real, descontando a inflação: {salarioReal}")

    elif salarioAtual >= 700 and salarioAtual < 1499:
        print(f"O valor do salário antes do reajuste era de R$ {salarioAtual} reais")
        print("Foi aplicado 10% no aumento baseado no salário.")

        aumento = (salarioAtual * 10)/100
        print(f"O valor do aumento foi de R$ {aumento},00 reais.")

        novoSalario = salarioAtual + aumento
        print(f"O novo salário após o aumento é de R$ {novoSalario} reais.")

        salarioReal = salarioAtual - (salarioAtual * 0.038)
        print(f"Valor do salário real, descontando a inflação: {salarioReal}")

    else:
        print(f"O valor do salário antes do reajuste era de R$ {salarioAtual} reais")
        print("Foi aplicado 5% no aumento baseado no salário.")

        aumento = (salarioAtual * 5)/100
        print(f"O valor do aumento foi de R$ {aumento} reais.")

        novoSalario = salarioAtual + aumento
        print(f"O novo salário após o aumento é de R$ {novoSalario} reais.")

        salarioReal = salarioAtual - (salarioAtual * 0.038)
        print(f"Valor do salário real, descontando a inflação: {salarioReal}")

    continuar = input("Gostaria de reajustar o salário novamente?: ")
    if continuar.lower() != 's':
        break
