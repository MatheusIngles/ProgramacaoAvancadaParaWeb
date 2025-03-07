import hashlib


text = "Ola mundo!"
hash_obejeo = hashlib.md5(text.encode())
## Não usar o modelo md5, ele já foi quebrado
print(hash_obejeo.hexdigest())
# Manter a base em hexdecimal

hash_sh1 = hashlib.sha1(text.encode())
# mais atual podemos encontrar no momento, podemos contralar o tamanho.
print(hash_sh1.hexdigest())

hash_sh256 = hashlib.sha256(text.encode())
# mais atual podemos encontrar no momento, podemos contralar o tamanho.
print(hash_sh256.hexdigest())

hash_sh512 = hashlib.sha512(text.encode())
# mais atual podemos encontrar no momento, podemos contralar o tamanho.
print(hash_sh512.hexdigest())