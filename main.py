from cryptography.fernet import Fernet

clave = Fernet.generate_key()
keybind = Fernet(clave)

sms = input("Enter the message you want to encrypt in bytes:")
mensaje_cifrado = keybind.encrypt(sms.encode())
print("Encrypted message in bytes:", mensaje_cifrado)


mensaje_descifrado = keybind.decrypt(mensaje_cifrado).decode()
print("Original message:", mensaje_descifrado)


