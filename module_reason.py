import random
from module_clear import wash, clear_used_words


def load_words(filename):
    with open(filename, 'r') as file:
        words = file.readlines()
    return [word.strip().lower() for word in words]


def save_used_words(used_words, filename):
    with open(filename, 'w') as file:
        for word in used_words:
            file.write(word + '\n')

def get_random_words(words, used_words, num_words):
    available_words = list(set(words) - set(used_words))
    if len(available_words) < num_words:
        return None
    return random.sample(available_words, num_words)

def display_word_with_hints(secret_word, guess):
    hint = ''
    for i in range(len(secret_word)):
        if secret_word[i] == guess[i]:
            hint += f' \033[92m{secret_word[i]}\033[0m '
        elif guess[i] in secret_word:
            hint += f' \033[93m{guess[i]}\033[0m '
        else:
            hint += f' {guess[i]} '
    return ''.join(hint)

def play_game(words, used_words, num_words, max_guesses):
    while True:
        secret_words = get_random_words(words, used_words, num_words)
        if secret_words is None:
            print("Você já usou todas as palavras disponíveis!")
            reset = input("Deseja resetar as palavras disponiveis? (s/n):")
            try:
                if reset == 's':
                    wash()
                    print("Resetando palavras salvas...!")
                    clear_used_words('used_words.txt') 
                elif reset == 'n':
                    break

                else:
                    if reset not in ('s', 'n'):
                        raise ValueError("Por favor, digite um caractere válido!")

                    
            except ValueError as e:
                print("\n" + "Erro:".center(60))
                print(f"{e}".center(60))
                print("!" * 60)
                continue

        used_words.extend(secret_words)
        save_used_words(used_words, 'used_words.txt')

        guesses = max_guesses
        guessed_words = [''] * num_words  # Lista para armazenar palavras já adivinhadas

        while guesses > 0:
            try:
                print("\n" + "-" * 60)
                guesses_left = f"\nTentativas restantes: {guesses}".center(60)
                print(guesses_left)

                user_guesses = input("\nDigite suas tentativas separadas por espaço: ").lower().split()

                if len(user_guesses) != num_words:
                    raise ValueError(f"\033[31mPor favor, insira\033[0m", "{num_words}" "\033[31mpalavras separadas por espaço!\033[0m")

                for i, guess in enumerate(user_guesses):
                    if len(guess) != 5 or not guess.isalpha():
                        raise ValueError("\033[31mPor favor, insira palavras válidas de 5 letras!\033[0m")

                    if not guess.islower():
                        raise ValueError("\033[31mApenas letras minúsculas são permitidas!\033[0m")

                    if guess == secret_words[i]:
                        guessed_words[i] = secret_words[i]  # Atualiza a palavra adivinhada na lista
                    else:
                        hints = display_word_with_hints(secret_words[i], guess)
                        print(f"\nDicas para a palavra {i + 1}:".center(60))
                        print(hints.center(60))
                        guesses -= 1

                print("\nPalavras corretamente adivinhadas:")
                for idx, word in enumerate(guessed_words):
                    if word:
                        print(f"Palavra {idx + 1}: \033[92m{word}\033[0m")
                        
                if all(guess == secret_word for guess, secret_word in zip(user_guesses, secret_words)):
                    print("\n" + "#" * 60)
                    print("\nParabéns! Você acertou todas as palavras!".center(60))
                    print("#" * 60)
                    break

            except ValueError as e:
                print("\n" + "Erro:".center(60))
                print(f"{e}".center(60))
                print("!" * 60)
                continue

        if guesses == 0:
            print("\n" + "-" * 60)
            print(f"\n \033[31mSuas tentativas acabaram. As palavras eram:\033[0m {secret_words}".center(60))

        play_again = input("\ \033[92mnDeseja jogar novamente? (S/N): \033[0m").lower()
        if play_again != 's':
            break






