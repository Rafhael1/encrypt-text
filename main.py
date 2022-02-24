from cryptography.fernet import Fernet

newFile = open('decrypt_key.txt', 'x')

key = Fernet.generate_key()
print(key)
fernet = Fernet(key)
array = 'pizza'

#Create a file with the encryption/decryption key
def save_key(encDecKey):
    return encDecKey

# Function to encrypt the password
def pass_encrypt(encKey):
    encMessage = fernet.encrypt(encKey.encode())
    print(encMessage)
    return encMessage

encryptedMessage = pass_encrypt(array)

# Function to decrypt the password
def pass_decrypt(encMessage):
    decMessage = fernet.decrypt(encMessage).decode()
    return decMessage

print(pass_decrypt(encryptedMessage))
