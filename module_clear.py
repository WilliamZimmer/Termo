import os

def wash():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[92mTela limpa.\033[0m")

def clear_used_words(filename):
    with open(filename, 'w') as file:
        file.write('')


    