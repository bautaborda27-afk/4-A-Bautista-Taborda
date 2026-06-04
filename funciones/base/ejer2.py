def usuario_valido (clave, usu):
    
    if clave == "1234" and usu.lower() == "admin":
        print("True")
    else:
        print("Flase")
print("Nombre de usuario: ")
nom = input()
print("Contraseña: ")
cont = input()
usuario_valido(cont,nom)