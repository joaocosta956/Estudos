import os


# Falta bastante acabamento e melhora do código, porem funciona


def funcao_cls(*args):
    os.system("cls")

def check(player1, player2):
    
    if player1 and player2 == "pedra" or "tesoura" or "papel":
        if player1 == "pedra":
            print(f'{Player1} jogou pedra')
            if player2 == "tesoura":
                print(f'{player1} ganhou!')
            else:
                print(f'{Player2} ganhou! ')
        elif player1 == 'tesoura':
            print(f'{Player1} jogou tesoura')
            if player2 == "pedra":
                print(f'{Player2} jogou pedra')
                print(f"{Player2} venceu")
            else:
                print(f'{Player2} jogou papel')
                print(f"{Player1} venceu")
        else:
            if player2 == "tesoura":
                print(f'{Player2} venceu')
            else:
                print(f'{Player1} venceu ')
    else:
        print("Valores errados!")


funcao_cls()

Player1 = input("Qual o nome do Player 1?")
Player2 = input("Qual o nome do Player 2?")

funcao_cls()

print(f"{Player1} contra {Player2}")
print()


print("Escolham entre: Pedra, Papel, Tesoura ")
print()
input_player1 = input(f'{Player1} começa: \n').lower()
funcao_cls()
input_player2 = input(f'{Player2} sua vez: \n').lower()
funcao_cls()

check(input_player1, input_player2)

