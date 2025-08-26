# 3. Verificação de senha padrão
# Percorra a string "123456" e mostre cada caractere, simulando a verificação da senha padrão

senha = str(input("Digite sua senha : "))
n1 = (len(senha))
print(f"sua senha tem {n1} caracteres ")
print('='* 35)
print("Verificando seu tamanho...")

if len(senha) == 6:
    print('Sua senha tem o tamanho válido')
else:
    print('Senha inválida pois não tem o tamanho adequado ')
print('='* 35)
print('='* 35)
print("verificando se a senha está correta...")

senha1 = int (senha)
if senha1 == 123456:
    print('Senha correta,acesso permitido')
else: 
    print('Senha incorreta')
print('='* 35)