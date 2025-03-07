import hashlib
import secrets

# Gerar um salt aleatorio, usando o modelo secrets 
salt = secrets.token_hex(16)
print(salt)

# definir uma senha 
password = "manga"

# hash para a senha, usando o salt e o algoritmo sha-256
hash_object =  hashlib.sha256((password +salt).encode())

hash_hex =  hash_object.hexdigest()
print(hash_hex)