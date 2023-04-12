def encrypt(message, shift):
    cipher_text = ""
    for char in message:
        if char.isalpha():
            if char == 'ç': # Tratamento especial para o caractere 'ç'
                cipher_text += 'ç'
            else:
                # Obter o código Unicode do caractere e adicionar o deslocamento
                char_code = ord(char) + shift

                # Verificar se o caractere está além do intervalo Unicode de letras maiúsculas ou minúsculas
                if char.isupper():
                    if char_code > ord('Z'):
                        char_code -= 26
                    elif char_code < ord('A'):
                        char_code += 26
                else:
                    if char_code > ord('z'):
                        char_code -= 26
                    elif char_code < ord('a'):
                        char_code += 26

                # Adicionar o caractere cifrado à mensagem cifrada
                cipher_text += chr(char_code)
        else:
            cipher_text += char
    return cipher_text

def decrypt(cipher_text, shift):
    return encrypt(cipher_text, -shift)

# Exemplo de uso
message = "A epistemologia e um ramo da filosofia que se dedica ao estudo dos fundamentos, das condiçoes e dos limites do conhecimento humano. Ela busca entender como e possivel adquirir, justificar e utilizar o conhecimento sobre a realidade, bem como as implicaçoes eticas, politicas e sociais do conhecimento produzido. Dentre as varias correntes da epistemologia, destacam-se o empirismo, que enfatiza a importancia da experiencia sensorial na formaçao do conhecimento, e o racionalismo, que valoriza o papel da razao e da deduçao logica na construçao do conhecimento. Alem disso, a epistemologia contemporanea se debruça sobre questoes como a natureza da verdade, a objetividade do conhecimento e a relaçao entre linguagem e realidade"
shift = 12
cipher_text = encrypt(message, shift)
print("Mensagem cifrada: ", cipher_text)

decrypted_message = decrypt(cipher_text, shift)
print("Mensagem decifrada: ", decrypted_message)
