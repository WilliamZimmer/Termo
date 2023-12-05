from module_reason import load_words, play_game, clear_used_words
from module_clear import wash

def main():
    words = load_words('words.txt')
    used_words = load_words('used_words.txt')

    while True:
        
        print("\033[31m*\033[31m" * 60)
        print("\033[1;37mTERMO\033[1;37m".center(60))
        print("TENTE ADIVINHAR A PALAVRA DE 5 LETRAS.".center(60))
        print("\033[31m*\033[31m" * 60)
        print()
        print("\033[36m1-\033[0m", "\033[35m SELECIONAR O MODO DE JOGO! \033[0m")
        print("\033[36m2-\033[0m", "\033[35m RESETAR LISTA! \033[0m")
        print("\033[36m3-\033[0m", "\033[35m SAIR! \033[0m")
        option = input("Digite a opção desejada: ")

        if option == "1":
            wash()
            while True:
                print("\033[1;36m Selecione o modo de jogo:\033[0m")
                print('\033[36m 1-\033[0m', "\033[35m PADRÂO; Adivinhe uma palavra em 5 tentativas! \033[0m")
                print('\033[36m 2-\033[0m', "\033[35m DUO: Adivinhe duas palavras simultaneamente em 6 tentativas! \033[0m")
                print('\033[36m 3-\033[0m', "\033[35m QUARTETO: Adivinhe quatro palavras simultaneamente em 8 tentativas! \033[0m")
                print('\033[36m 4-\033[0m', "\033[35m VOLTAR: \033[0m")      
                mode_option = input("Digite:").lower()

                if mode_option == "1":
                    play_game(words, used_words, num_words = 1, max_guesses=5)
                elif mode_option == '2':
                    play_game(words, used_words, num_words = 2, max_guesses=6)
                elif mode_option == '3':
                    play_game(words, used_words, num_words = 4, max_guesses=8)
                elif mode_option == "4":
                    break
                else:
                    print("\033[31mOpção inválida. Tente novamente.\033[0m")

        elif option == "2":
            wash()
            print("Resetando palavras salvas...!")
            clear_used_words('used_words.txt')

        else:
            if option == "3":
                wash()
                print("\033[35m*\033[0m" * 60)
                print("Obrigado por jogar!")
                print("\033[35m*\033[0m" * 60)                
                break
            else:
                print("\033[31mOpção inválida. Tente novamente.\033[0m")

main()