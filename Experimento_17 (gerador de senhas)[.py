from time import sleep
from random import choice, randint, sample

alfa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z', 'ç']
alfam = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z', 'Ç']
simb = ['*', '-', '+', '.', '/', ',', '/', '?', '°', ']', '}', 'º', '[', '{', 'ª', '´', '~', '^', '-', '_', '=', '+']
nuns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

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
if alfabet != 1 and alfabet != 2 and alfabet != 3:
    while True:
        print("Informação inválida. Digite novamente.")
        alfabet = int(input("""[1] Apenas maiusculas
[2] Apenas minusculas
[3] Maiusculas e minusculas"""))
        print(

        )
        if alfabet == 1 or alfabet == 2 or alfabet == 3:
            break

if alfabet == 1:
    lets = randint(4, 7)
    for let in range(0, lets):
        senha.append(choice(alfam))

elif alfabet == 2:
    lets = randint(4, 7)
    for let in range(0, lets):
        senha.append(choice(alfa))

elif alfabet == 3:
    lets = randint(4, 7)
    for let in range(0, lets):
        senha.append(choice(alfam))
        senha.append(choice(alfa))


#                       **SIMBOLOS**
simbo = input("Quer que sua senha contenha simbolos como: *  -  ?  /\n[S]im\n[N]ão\n").lower()
print(

)
if simbo != 's' and simbo != 'n':
    while True:
        print("Informação inválida. Digite novamente.")
        simbo = input("[S]im\n[N]ão\n")
        print(

        )
        if simbo == 's' or simbo == 'n':
            break

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
if nun != 's' and nun != 'n':
    while True:
        print("Informação inválida. Digite novamente.")
        nun = input("[S]im\n[N]ão\n")
        print(

        )
        if nun == 's' or nun == 'n':
            break

elif nun == 's':
    nunss = randint(3, 7)
    for nume in range(0, nunss):
        senha.append(choice(nuns))

elif nun == 'n':
    print('ok.')

#                       **RESULTADO**
print("Sua senha ficou assim:   ", *sample(senha, len(senha)), sep='')
