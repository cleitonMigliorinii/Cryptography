import tkinter as tk
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Função para gerar um novo par de chaves RSA
def generate_keys():
    key = RSA.generate(2048)  # Gera uma chave RSA de 2048 bits
    private_key = key.export_key()  # Exporta a chave privada
    public_key = key.publickey().export_key()  # Exporta a chave pública
    private_key_entry.delete(0, tk.END)  # Limpa o campo de entrada da chave privada
    private_key_entry.insert(tk.END, private_key.decode())  # Insere a chave privada no campo de entrada
    public_key_entry.delete(0, tk.END)  # Limpa o campo de entrada da chave pública
    public_key_entry.insert(tk.END, public_key.decode())  # Insere a chave pública no campo de entrada

# Função para criptografar uma mensagem
def encrypt_message():
    recipient_key = RSA.import_key(public_key_entry.get())  # Importa a chave pública do destinatário
    cipher = PKCS1_OAEP.new(recipient_key)  # Cria um objeto de cifra RSA com enchimento PKCS1 OAEP
    ciphertext = cipher.encrypt(message_entry.get().encode())  # Criptografa a mensagem
    encrypted_entry.delete(0, tk.END)  # Limpa o campo de entrada da mensagem criptografada
    encrypted_entry.insert(tk.END, ciphertext.hex())  # Insere a mensagem criptografada no campo de entrada

# Função para descriptografar uma mensagem
def decrypt_message():
    private_key = RSA.import_key(private_key_entry.get())  # Importa a chave privada do usuário
    cipher = PKCS1_OAEP.new(private_key)  # Cria um objeto de cifra RSA com enchimento PKCS1 OAEP
    ciphertext = bytes.fromhex(encrypted_entry.get())  # Converte a mensagem criptografada de hexadecimal para bytes
    decrypted = cipher.decrypt(ciphertext).decode()  # Descriptografa a mensagem e decodifica para texto
    decrypted_entry.delete(0, tk.END)  # Limpa o campo de entrada da mensagem descriptografada
    decrypted_entry.insert(tk.END, decrypted)  # Insere a mensagem descriptografada no campo de entrada

# Criação da interface gráfica
root = tk.Tk()  # Cria uma nova janela principal
root.title("RSA Criptografia Assimétrica")  # Define o título da janela

# Botões e campos de entrada
generate_keys_button = tk.Button(root, text="Gerar Par de Chaves", command=generate_keys)
generate_keys_button.pack()  # Adiciona o botão à janela

private_key_label = tk.Label(root, text="Chave Privada:")  # Rótulo para a chave privada
private_key_label.pack()  # Adiciona o rótulo à janela
private_key_entry = tk.Entry(root, width=50)  # Campo de entrada para a chave privada
private_key_entry.pack()  # Adiciona o campo de entrada à janela

public_key_label = tk.Label(root, text="Chave Pública:")  # Rótulo para a chave pública
public_key_label.pack()  # Adiciona o rótulo à janela
public_key_entry = tk.Entry(root, width=50)  # Campo de entrada para a chave pública
public_key_entry.pack()  # Adiciona o campo de entrada à janela

message_label = tk.Label(root, text="Mensagem:")  # Rótulo para a mensagem
message_label.pack()  # Adiciona o rótulo à janela
message_entry = tk.Entry(root, width=50)  # Campo de entrada para a mensagem
message_entry.pack()  # Adiciona o campo de entrada à janela

encrypt_button = tk.Button(root, text="Criptografar", command=encrypt_message)
encrypt_button.pack()  # Adiciona o botão à janela

encrypted_label = tk.Label(root, text="Mensagem Criptografada:")  # Rótulo para a mensagem criptografada
encrypted_label.pack()  # Adiciona o rótulo à janela
encrypted_entry = tk.Entry(root, width=50)  # Campo de entrada para a mensagem criptografada
encrypted_entry.pack()  # Adiciona o campo de entrada à janela

decrypt_button = tk.Button(root, text="Descriptografar", command=decrypt_message)
decrypt_button.pack()  # Adiciona o botão à janela

decrypted_label = tk.Label(root, text="Mensagem Descriptografada:")  # Rótulo para a mensagem descriptografada
decrypted_label.pack()  # Adiciona o rótulo à janela
decrypted_entry = tk.Entry(root, width=50)  # Campo de entrada para a mensagem descriptografada
decrypted_entry.pack()  # Adiciona o campo de entrada à janela

root.mainloop()  # Inicia o loop principal da interface gráfica
