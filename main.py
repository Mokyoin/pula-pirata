#importações
import colorama
import sys
import subprocess
import os

colorama.init()


# Ao ser chamado limpa o terminal
def limpar_terminal():
    """Limpa o terminal."""
    os.system("cls" if os.name == "nt" else "clear")

# Mostra o nome dos integrantes ao ser chamado, creditos de quem fez 
def mostrar_creditos():
    """Mostra os integrantes do grupo."""
    print("\n==============================")
    print("           CRÉDITOS")
    print("==============================")
    print("Gabriela do Rozario")
    print("Henrique Luiz da Cruz")
    print("Lucas Alberto Salvador")
    print("Milenna de Moraes")
    print("==============================")
    input("\nPressione ENTER para voltar ao menu...")

#Inicia o jogo ao ser chamado
def iniciar_jogo():


    #executa outro programa usando o python, o jogo py que é outro arquivo
    while True:
        try:
            subprocess.run(
                [sys.executable, "Jogo.py"]
            )
            break

        except ValueError:
            print("Erro! Algo deu errado ao iniciar o jogo.")


def main():
    """Função principal do programa."""

    while True:
        limpar_terminal()

        print(colorama.Fore.BLUE + "================================")
        print("          M2G PIRATE"        )
        print("================================" + colorama.Style.RESET_ALL)

        print("\n1 - Iniciar Jogo")
        print("2 - Créditos")
        print("3 - Sair")

        try:
            opcao = int(input("\nEscolha uma opção: "))

            if opcao == 1:
                iniciar_jogo()

            elif opcao == 2:
                mostrar_creditos()

            elif opcao == 3:
                print("\nObrigado por jogar M2G Pirate!")
                break

            else:
                print("\nOpção inválida!")
                input("Pressione ENTER para continuar...")

        except ValueError:
            print("\nErro! Digite apenas 1, 2 ou 3.")
            input("Pressione ENTER para continuar...")


# Início do programa
if __name__ == "__main__":
    main()


