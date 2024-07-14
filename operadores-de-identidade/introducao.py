# Exemplo
curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

curso is nome_curso # True

curso is not nome_curso # False

saldo is limite # True

# Video aula
saldo = 1000
limite = 1000

print(saldo is limite) #Resultado: True
print(saldo is not limite) # Resultado: False