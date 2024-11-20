import hashlib

password_save = "CasaInformatica"
password_save_hash = hashlib.sha256(password_save.lower().encode("utf-8")).hexdigest()
password = input("Password: ")
password_hash = hashlib.sha256(password.lower().encode("utf-8")).hexdigest()

if(password_hash == password_save_hash):
    print(f"Contraseña correcta")
else:
    print(f"Contraseña incorrecta")