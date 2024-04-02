import tkinter as tk
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    key_entry.delete(0, tk.END)
    key_entry.insert(tk.END, key.decode())

def encrypt_data(data, key):
    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(data.encode())
    return encrypted_data

def decrypt_data(encrypted_data, key):
    cipher = Fernet(key)
    decrypted_data = cipher.decrypt(encrypted_data).decode()
    return decrypted_data

def encrypt():
    # Obter a chave do campo de entrada
    key = key_entry.get()

    # Obter os dados do campo de entrada
    data_to_encrypt = data_entry.get()

    # Criptografar os dados
    encrypted_data = encrypt_data(data_to_encrypt, key)

    # Exibir os dados criptografados
    encrypted_entry.delete(0, tk.END)
    encrypted_entry.insert(tk.END, encrypted_data)

def decrypt():
    # Obter a chave do campo de entrada
    key = key_entry.get()

    # Obter os dados criptografados do campo de entrada
    encrypted_data = encrypted_entry.get()

    # Descriptografar os dados
    decrypted_data = decrypt_data(encrypted_data.encode(), key)

    # Exibir os dados descriptografados
    decrypted_entry.delete(0, tk.END)
    decrypted_entry.insert(tk.END, decrypted_data)

# Criação da interface gráfica
root = tk.Tk()
root.title("Criptografia com Fernet")

# Rótulo e campo de entrada para a chave
key_label = tk.Label(root, text="Chave:")
key_label.grid(row=0, column=0, padx=10, pady=5)
key_entry = tk.Entry(root, width=50)
key_entry.grid(row=0, column=1, padx=10, pady=5)

# Botão para gerar a chave
generate_key_button = tk.Button(root, text="Gerar Chave", command=generate_key)
generate_key_button.grid(row=0, column=2, padx=10, pady=5)

# Rótulo e campo de entrada para os dados
data_label = tk.Label(root, text="Dados:")
data_label.grid(row=1, column=0, padx=10, pady=5)
data_entry = tk.Entry(root, width=50)
data_entry.grid(row=1, column=1, padx=10, pady=5)

# Botão para criptografar
encrypt_button = tk.Button(root, text="Criptografar", command=encrypt)
encrypt_button.grid(row=2, column=0, padx=10, pady=5)

# Botão para descriptografar
decrypt_button = tk.Button(root, text="Descriptografar", command=decrypt)
decrypt_button.grid(row=2, column=1, padx=10, pady=5)

# Rótulo e campo de entrada para os dados criptografados
encrypted_label = tk.Label(root, text="Dados Criptografados:")
encrypted_label.grid(row=3, column=0, padx=10, pady=5)
encrypted_entry = tk.Entry(root, width=50)
encrypted_entry.grid(row=3, column=1, padx=10, pady=5)

# Rótulo e campo de entrada para os dados descriptografados
decrypted_label = tk.Label(root, text="Dados Descriptografados:")
decrypted_label.grid(row=4, column=0, padx=10, pady=5)
decrypted_entry = tk.Entry(root, width=50)
decrypted_entry.grid(row=4, column=1, padx=10, pady=5)

root.mainloop()
