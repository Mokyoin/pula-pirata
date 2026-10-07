#importrações!
from colorama import Fore, init
import random
import os
import sys
import subprocess
init(autoreset=True)


#matrizes de 2 até 4 players
barril_2 = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

barril_3 = [
    [" ", " ", " ", " "],
    [" ", " ", " ", " "],
    [" ", " ", " ", " "]
]

barril_4 = [
    [" ", " ", " ", " "],
    [" ", " ", " ", " "],
    [" ", " ", " ", " "],
    [" ", " ", " ", " "]
]

def limpar_terminal():
    os.system("cls")



def voltar_menu():
        try:
            subprocess.run(
                [sys.executable, "main.py"]
            )


        except ValueError:
            print("Erro! Algo deu errado ao tentar iniciar o menu principal.")

def limpar_barril(barril):
    for i in range(len(barril)):
        for j in range(len(barril[i])):
            barril[i][j] = " "

def retorno():
    input("Pressione Enter para continuar...")


#tabuleiros montados
def mostrar_tabuleiro(barril):
    colunas = len(barril[0])

    print("    ", end="")
    for c in range(1, colunas + 1):
        print(f"{c}   ", end="")
    print()

    for i, linha in enumerate(barril, start=1):
        print(f"{i} |", end="")
        for celula in linha:
            print(f" {celula} |", end="")
        print()



#respeita os limites de quantidade de cada jogador
def pedir_numero(mensagem, minimo, maximo):
    while True:
        valor = input(mensagem)
        if valor.isdigit():
            valor = int(valor)
            if minimo <= valor <= maximo:
                return valor
        print(f"{Fore.RED}Número inválido! Digite um valor entre {minimo} e {maximo}.{Fore.RESET}")


#Opções jogaveis
def jogo():
    limpar_terminal()

    qtd = pedir_numero("Digite a quantidade de jogadores (min: 2 max: 4): ", 2, 4)

    if qtd == 2:
        barril = barril_2
        max_linha = 3
        max_coluna = 3
    elif qtd == 3:
        barril = barril_3
        max_linha = 3
        max_coluna = 4
    else:
        barril = barril_4
        max_linha = 4
        max_coluna = 4

    
    # Cores dos jogadores
    cores = [Fore.RED, Fore.BLUE, Fore.CYAN, Fore.MAGENTA]
    jogadores = []

    for i in range(qtd):
        nome = input(f"Digite o nome do jogador {i + 1}: ").strip()
        if not nome:
            nome = f"Jogador {i + 1}"
        jogadores.append(nome)

    # Mostra os jogadores com cores (estilo do primeiro código)
    print()
    for i in range(qtd):
        print(f"{cores[i]}Jogador {i + 1}: {jogadores[i]}{Fore.RESET}")
    print()

    pontos = [0] * qtd
    vez = 0
    foi_vazio = False
    
    # Gera a posição ramdomica do pirata, a cada partida
    linha_pirata = random.randint(0, max_linha - 1)
    coluna_pirata = random.randint(0, max_coluna - 1)
    
    #print(f"[DEBUG] Pirata está na linha {linha_pirata + 1}, coluna {coluna_pirata + 1}") <-- debug 

    while True:
        print(f"{cores[vez]}Vez de {jogadores[vez]}{Fore.RESET}")

        if foi_vazio:
            print(f"\n{Fore.GREEN}🛢️  Barril vazio!{Fore.RESET}")
            foi_vazio = False

        print()
        mostrar_tabuleiro(barril)
        print()

        #linha e coluna do jogo
        linha = pedir_numero(f"Escolha a linha (1-{max_linha}): ", 1, max_linha)
        coluna = pedir_numero(f"Escolha a coluna (1-{max_coluna}): ", 1, max_coluna)

        # Já foi escolhido?
        if barril[linha - 1][coluna - 1] != " ":
            print(f"{Fore.YELLOW}Esse barril já foi escolhido! Escolha outro.{Fore.RESET}\n")
            continue

        # Acertou o pirata?
        if linha - 1 == linha_pirata and coluna - 1 == coluna_pirata:
            limpar_terminal()
            print(f"\n{Fore.RED}☠️  O PIRATA SALTOU! o jogador {jogadores[vez]} perdeu a rodada!")
            pontos[vez] += 1

            # Placar de quem esta ganhando
            placar = " | ".join([f"{jogadores[i]}: {pontos[i]}" for i in range(qtd)])
            print(f"Placar → {placar}")

            if pontos[vez] >= 5:
                print(f"\n{Fore.RED}💀 {jogadores[vez]} chegou a 5 pontos e perdeu o jogo!{Fore.RESET}")
                break
             
            novamente = input("\nDeseja continuar?\n Digite sim ou s para continuar\n Digite nao ou n para voltar para o menu\n\nInsira sua resposta: ")

            if novamente == "sim" or novamente == "s":
                limpar_barril(barril)

                linha_pirata = random.randint(0, max_linha - 1)
                coluna_pirata = random.randint(0, max_coluna - 1)

                limpar_terminal()
                print(f"\n🔄 Nova rodada! O pirata mudou de lugar...\n{Fore.RED}-- JOGADOR COM MAIS PONTOS PERDE!!--\n")
                vez = (vez + 1) % qtd
                continue

            elif novamente == "nao" or novamente == "n":
                voltar_menu()
                return

        # Barril vazio
        barril[linha - 1][coluna - 1] = "🗡️"
        foi_vazio = True
        limpar_terminal()
        vez = (vez + 1) % qtd


# Inicia o jogo
if __name__ == "__main__":
    jogo()

# cada um fez uma parte do codigo, obs: perdi 3 vezes jogando isso (ass: moky )