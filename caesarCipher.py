def cifra_de_cesar(texto, chave, lado):
    texto_processado = ''
    for char in texto:
        if char.isalpha():  # Verifica se o caractere é uma letra do alfabeto
            if char.islower():
                novo_char = chr((ord(char) - 97 + chave * lado) % 26 + 97)  # Para letras minúsculas
            else:
                novo_char = chr((ord(char) - 65 + chave * lado) % 26 + 65)  # Para letras maiúsculas
        else:
            novo_char = char  # Mantém caracteres não alfabéticos como estão
        texto_processado += novo_char
    return texto_processado

def main():
    print("Bem-vindo à cifra de César!")

    texto = input("Digite o texto a ser cifrado/decifrado: ")
    chave = int(input("Digite o deslocamento (um número inteiro): "))
    lado = input("Digite 'c' para cifrar ou 'd' para decifrar: ")

    if lado.lower() == 'c':
        lado = 1
    elif lado.lower() == 'd':
        lado = -1
    else:
        print("Opção inválida. Por favor, digite 'c' ou 'd'.")
        return

    texto_processado = cifra_de_cesar(texto, chave, lado)
    print("Texto processado:", texto_processado)

if __name__ == "__main__":
    main()
