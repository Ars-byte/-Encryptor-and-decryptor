import tkinter as tk
from cryptography.fernet import Fernet

clave = Fernet.generate_key()
keybind = Fernet(clave)

def encrypt_message():
    message = message_entry.get()
    encrypted_message = keybind.encrypt(message.encode())
    encrypted_message_text.delete(1.0, tk.END)
    encrypted_message_text.insert(tk.INSERT, encrypted_message.decode())

def decrypt_message():
    encrypted_message = encrypted_message_text.get(1.0, tk.END)
    decrypted_message = keybind.decrypt(encrypted_message.encode()).decode()
    decrypted_message_text.delete(1.0, tk.END)
    decrypted_message_text.insert(tk.INSERT, decrypted_message)

ventana = tk.Tk()
ventana.title("SMS Encryption and Decryption")


main_frame = tk.Frame(ventana, bg="#f0f0f0")
main_frame.pack(fill="both", expand=True)

message_label = tk.Label(main_frame, text="Enter the message you want to encrypt:", font=("Arial", 12), bg="#f0f0f0")
message_label.pack(pady=10)

message_entry = tk.Entry(main_frame, width=40, font=("Arial", 12))
message_entry.pack(pady=10)

encrypt_button = tk.Button(main_frame, text="Encrypt", command=encrypt_message, font=("Arial", 12), bg="#007bff", fg="white")
encrypt_button.pack(pady=10)

encrypted_message_label = tk.Label(main_frame, text="Encrypted message:", font=("Arial", 12), bg="#f0f0f0")
encrypted_message_label.pack(pady=10)

encrypted_message_text = tk.Text(main_frame, width=40, height=5, font=("Arial", 12))
encrypted_message_text.pack(pady=10)

decrypt_button = tk.Button(main_frame, text="Decrypt", command=decrypt_message, font=("Arial", 12), bg="#007bff", fg="white")
decrypt_button.pack(pady=10)

decrypted_message_label = tk.Label(main_frame, text="Decrypted message:", font=("Arial", 12), bg="#f0f0f0")
decrypted_message_label.pack(pady=10)

decrypted_message_text = tk.Text(main_frame, width=40, height=5, font=("Arial", 12))
decrypted_message_text.pack(pady=10)

ventana.mainloop()


