import random
import string
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def cabecalho():
    print("=" * 50)
    print(" " * 15 + "GERADOR DE SENHAS")
    print("=" * 50)

def gerar_senha(comprimento, incluir_maiusculas, incluir_numeros, incluir_especiais):
    caracteres = string.ascii_lowercase
    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_especiais:
        caracteres += string.punctuation

    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

def main():
    limpar_tela()
    cabecalho()
    print("Bem-vindo ao Gerador de Senhas Personalizadas!")
    print("Configure sua senha abaixo:")
    
    comprimento = int(input("\nDigite o comprimento desejado da senha (mínimo 6): "))
    while comprimento < 6:
        print("⚠️ O comprimento deve ser pelo menos 6 caracteres!")
        comprimento = int(input("Tente novamente: "))
    
    incluir_maiusculas = input("Incluir letras maiúsculas? (S/N): ").strip().lower() == 's'
    incluir_numeros = input("Incluir números? (S/N): ").strip().lower() == 's'
    incluir_especiais = input("Incluir caracteres especiais? (S/N): ").strip().lower() == 's'

    limpar_tela()
    cabecalho()
    print("\nGerando sua senha...\n")
    senha = gerar_senha(comprimento, incluir_maiusculas, incluir_numeros, incluir_especiais)
    print(f"Sua senha gerada é: \033[1;32m{senha}\033[0m")
    print("\nDica: Salve sua senha em um gerenciador de senhas para mais segurança.")
    print("=" * 50)

if __name__ == "__main__":
    main()
