# =====================================================================
# Reto Semanal 3: Formateo y Estética de Datos
# Programa: Calculadora de IMC
# =====================================================================

print("--- Calculadora de IMC ---")

# 1. Solicitar datos al usuario con input()
# ¡NUEVO! Usamos .title() para que la primera letra de cada palabra sea mayúscula.
# Ejemplo: Si el usuario escribe "gustavo", se guardará como "Gustavo".
nombre = input("Ingresa tu nombre: ").title()
apellido_paterno = input("Ingresa tu apellido paterno: ").title()
apellido_materno = input("Ingresa tu apellido materno: ").title()

# 2. Casting (conversión de tipos)
edad = int(input("Ingresa tu edad (años): "))
peso = float(input("Ingresa tu peso (kg): "))
estatura = float(input("Ingresa tu estatura (m): "))

# 3. Calcular el IMC
imc = peso / (estatura ** 2)

# 4. Mostrar los resultados usando f-strings
print("\n--- Resultados ---")
# Usamos f-strings para mezclar texto y variables de forma limpia
print(f"Paciente: {nombre} {apellido_paterno} {apellido_materno}")
print(f"Edad: {edad} años")
print(f"Peso: {peso} kg")
print(f"Estatura: {estatura} m")

# ¡NUEVO! Mostramos el IMC redondeado a 2 decimales usando f-string.
# El formato :.2f indica que queremos 2 números después del punto decimal.
print(f"Tu IMC es: {imc:.2f}")

# 5. Evaluar el IMC
if imc < 18.5:
    print("Clasificación: Bajo peso")
elif imc >= 18.5 and imc < 25:
    print("Clasificación: Peso normal")
elif imc >= 25 and imc < 30:
    print("Clasificación: Sobrepeso")
else:
    print("Clasificación: Obesidad")