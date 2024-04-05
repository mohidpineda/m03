import hashlib

def cifrar_contraseña(contraseña):
    return hashlib.md5(contraseña.encode()).hexdigest()

def cargar_usuarios():
    usuarios = {}
    try:
        file = open("Usuaris.txt", "r")
        for line in file.readlines():
            usuario, contraseña_cifrada = line.strip().split("|")
            usuarios[usuario] = contraseña_cifrada
        file.close()
    except FileNotFoundError:
        print("ERROR: No se encontró el archivo 'Usuaris.txt'.")
    except Exception as e:
        print("ERROR: Algo salió mal al cargar usuarios:", e)
    return usuarios