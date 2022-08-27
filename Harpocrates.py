from des import DesKey
import hashlib
import base64
import time


crypto_level = 15

def keep_secret(package):

    msg = package

    for key in range(crypto_level):

        key = hashlib.sha512(bytes(str(key), encoding='utf-8')).hexdigest()
        package = msg
        package = bytes(str(package), encoding= 'utf-8')
        secret = bytes(key[0:24], encoding= 'utf-8')
        key = DesKey(secret)
        msg = base64.b64encode(DesKey.encrypt(key, package, padding= True)).decode()

    return msg

msg = keep_secret("{nib};{nome};{cpf};{dtn};{tel1};{tel2}")
print(msg)

for i in range(crypto_level-1, -1, -1):

    key = i
    key = hashlib.sha512(bytes(str(key), encoding='utf-8')).hexdigest()
    package = msg
    package = bytes(str(package), encoding='utf-8')
    secret = bytes(key[0:24], encoding='utf-8')
    key = DesKey(secret)
    msg = base64.b64decode(msg)
    msg = DesKey.decrypt(key, msg, padding=True).decode()

print(msg)