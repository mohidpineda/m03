import hashlib

def cifrar_contraseña(contraseña):
    return hashlib.md5(contraseña.encode()).hexdigest()