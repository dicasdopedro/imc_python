def calcular_imc(peso, altura):
    # FUNÇÃO que calcula o  IMC usando a fórmula: peso / altura^2
    imc = peso / (altura ** 2)
    return imc

# O usuário deve digitar o peso e a altura
peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

# FÓRMULA que calcula o IMC
imc_resultado = calcular_imc(peso, altura)

# Esta é a situação do Paciente de acordo com as CONDIÇÕES apresentadas
if imc_resultado < 18.5: # SE Menor que 18.5
    categoria = "Abaixo do peso"
elif 18.5 <= imc_resultado < 25: # OU ENTÃO Maior ou igual a 18.5 e Menor que 25
    categoria = "Normal"
elif 25 <= imc_resultado < 30: # OU ENTÃO Maior ou igual a 25 e Menor que 30
    categoria = "Sobrepeso"
else:
    categoria = "Obesidade" # CASO CONTRÁRIO, ou seja, a partir de 30

# Apresenta o resultado na tela do computador
print(f"Seu IMC é {imc_resultado:.1f}, e a sua situação é: {categoria}")