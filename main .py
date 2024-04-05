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

def cargar_libros():
    libros = []
    try:
        file = open("Llibres.txt", "r")
        for line in file.readlines():
            datos = line.strip().split("|")
            libro = {
                'Título': datos[0],
                'Autor/a': datos[1],
                'Año de publicación': datos[2],
                'Género': datos[3],
                'ISBN': datos[4]
            }
            libros.append(libro)
        file.close()
    except FileNotFoundError:
        print("ERROR: No se encontró el archivo 'Llibres.txt'.")
    except Exception as e:
        print("ERROR: Algo salió mal al cargar libros:", e)
    return libros