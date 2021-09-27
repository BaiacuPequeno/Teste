from time import sleep
from random import choice, randint, sample

alfa = tuple('abcdefghijklmnopqrstuvwxyzç')
alfam = tuple('ABCDEFGHIJKLMNOPQRSTUVWXYZÇ')
simb = tuple('*-+./,/?°]}º[{ª´~^-_=+')
nuns = tuple('1234567890')

senha = []
temp = randint(1, 4)

print('\033[34m-\033[m' * 85)
print("  Esse é um gerador de senhas simples feito por Miguel Augusto no dia (25/09/2021)")
print('\033[34m-\033[m' * 85)
print(

)
print("Carregando.", end="")
for tempo in range(0, temp):
    sleep(0.6)
    print(".", end="")
print(

)
#                       **TIPO DAS LETRAS**
alfabet = int(input("""Voce quer sua senha com:
[1] Apenas maiusculas
[2] Apenas minusculas
[3] Maiusculas e minusculas"""))
print(

)

while alfabet not in (1, 2, 3):
    print("Informação inválida. Digite novamente.")
    alfabet = int(input("""[1] Apenas maiusculas
[2] Apenas minusculas
[3] Maiusculas e minusculas"""))
print(

)


lets = randint(4, 7)

if alfabet == 1:
    for let in range(0, lets):
        senha.append(choice(alfam))

elif alfabet == 2:
    for let in range(0, lets):
        senha.append(choice(alfa))

elif alfabet == 3:
    for let in range(0, lets):
        senha.append(choice(alfam))
        senha.append(choice(alfa))


#                       **SIMBOLOS**
simbo = input("Quer que sua senha contenha simbolos como: *  -  ?  /\n[S]im\n[N]ão\n").lower()
print(

)

while simbo not in ('s', 'n'):
    print("Informação inválida. Digite novamente.")
    simbo = input("[S]im\n[N]ão\n")
print(

)

if simbo == 's':
    simbs = randint(1, 5)
    for sinbo in range(0, simbs):
        senha.append(choice(simb))
elif simbo == 'n':
    print('ok.')


#                       **NUMEROS**
nun = input("Quer que sua senha contenha números?\n[S]im\n[N]ão\n").lower()
print(

)
while num not in ('s', 'n'):
    print("Informação inválida. Digite novamente.")
    nun = input("[S]im\n[N]ão\n")
    print(

    )

if nun == 's':
    nunss = randint(3, 7)
    for nume in range(0, nunss):
        senha.append(choice(nuns))

elif nun == 'n':
    print('ok.')

#                       **RESULTADO**
print("Sua senha ficou assim:   ", *sample(senha, len(senha)), sep='')
