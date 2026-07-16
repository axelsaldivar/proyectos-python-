# 1. Definimos las palabras clave que usan los hackers para estafar
palabras_peligrosas = ["banco", "ganaste", "premio", "contraseña", "urgente", "clonación"]

# 2. El correo que el sistema va a analizar (Puedes cambiar este texto para probar)
correo_recibido = "Urgente: Hemos detectado un problema en su cuenta de banco, cambie su contraseña aquí"

# Pasamos todo el texto a minúsculas para que la búsqueda sea exacta
correo_minusculas = correo_recibido.lower()

print("=== ANALIZADOR DE CORREOS CON IA DE AXEL ===")
print("Analizando mensaje...")
print("--------------------------------------------")

# 3. La lógica de filtrado: Verificamos si alguna palabra peligrosa está en el correo
es_phishing = False

for palabra in palabras_peligrosas:
    if palabra in correo_minusculas:
        es_phishing = True

# 4. Tomamos la decisión final con nuestro conocido IF / ELSE
if es_phishing == True:
    print("¡ALERTA MÁXIMA! Correo bloqueado por seguridad. Contiene enlaces sospechosos.")
else:
    print("Correo seguro. El mensaje ha sido entregado a la bandeja de entrada.")
