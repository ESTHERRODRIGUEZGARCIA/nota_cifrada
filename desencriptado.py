import codecs

file_path = 'Nota..txt'

# Leer el contenido del archivo
with open(file_path, 'r', encoding='utf-8') as file:
    encrypted_text = file.read()

# Aplicar ROT13 al texto cifrado
decrypted_text = codecs.decode(encrypted_text, 'rot_13')

# Imprimir el texto descifrado
print(decrypted_text)
