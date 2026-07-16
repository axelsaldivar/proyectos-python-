# 1. Definimos la clave correcta y el número de intentos permitidos
clave_correcta = "axel123"
intentos_restantes = 3

print("=== SISTEMA DE SEGURIDAD MÓVIL ===")
print("Tienes 3 intentos para desbloquear el dispositivo.")
print("-------------------------------------------------")

# 2. El bucle while se repite MIENTRAS queden intentos
while intentos_restantes > 0:
    # Le pedimos la clave al usuario en vivo
    clave_ingresada = input("Introduce la contraseña de acceso: ")
    
    # Verificamos si la clave es correcta usando IF / ELSE
    if clave_ingresada == clave_correcta:
        print("¡ACCESO CONCEDIDO! Bienvenido de vuelta.")
        break  # El comando 'break' rompe el bucle de inmediato porque ya ganaste
    else:
        # Si falla, le restamos un intento
        intentos_restantes = intentos_restantes - 1
        print("Contraseña incorrecta.")
        print("Te quedan", intentos_restantes, "intentos restantes.\n")

# 3. Si se acaban los intentos y el bucle termina, bloqueamos el sistema
if intentos_restantes == 0:
    print("¡ALERTA DE SEGURIDAD! Dispositivo BLOQUEADO por 30 minutos.")
