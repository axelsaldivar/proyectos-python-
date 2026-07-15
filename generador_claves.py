import random

# 1. Definimos los componentes de una contraseña segura
letras_minusculas = "abcdefghijklmnopqrstuvwxyz"
letras_mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"
simbolos = "!@#$%^&*()_+"

# Juntamos todos los caracteres para crear la súper base de datos
todos_los_caracteres = letras_minusculas + letras_mayusculas + numeros + simbolos

# 2. El programa genera una contraseña aleatoria de 12 caracteres
contrasena_generada = "".join(random.sample(todos_los_caracteres, 12))

print("=== SISTEMA DE CIBERSEGURIDAD DE AXEL ===")
print("Tu nueva contraseña segura generada es:", contrasena_generada)
print("----------------------------------------")

# 3. Probamos tu lógica con un IF / ELSE para validar la seguridad
longitud = len(contrasena_generada)

if longitud >= 10:
    print("RESULTADO DEL ANÁLISIS: ¡Contraseña altamente segura! Bloquea ataques de hackers.")
else:
    print("RESULTADO DEL ANÁLISIS: Alerta, contraseña muy corta y vulnerable.")
