# =====================================================================
# Reto Semanal 2: Interacción, Cálculo y Git
# Programa: Calculadora de IMC
# =====================================================================

print("--- Calculadora de IMC ---")

# 1. Solicitar datos al usuario con input()
# Nota: input() siempre devuelve un string (texto)
nombre = input("Ingresa tu nombre: ")
apellido_paterno = input("Ingresa tu apellido paterno: ")
apellido_materno = input("Ingresa tu apellido materno: ")

# 2. Casting (conversión de tipos)
# Convertimos la edad a entero (int) y peso/estatura a flotante (float)
edad = int(input("Ingresa tu edad (años): "))
peso = float(input("Ingresa tu peso (kg): "))
estatura = float(input("Ingresa tu estatura (m): "))

# 3. Calcular el IMC
# Fórmula: peso dividido entre la estatura al cuadrado
imc = peso / (estatura ** 2)

# 4. Mostrar los resultados
print("\n--- Resultados ---")
print(f"Paciente: {nombre} {apellido_paterno} {apellido_materno}")
print(f"Edad: {edad} años")
print(f"Peso: {peso} kg")
print(f"Estatura: {estatura} m")
print(f"Tu IMC es: {round(imc, 2)}")

# 5. Evaluar el IMC (Opcional, pero recomendado)
if imc < 18.5:
    print("Clasificación: Bajo peso")
elif imc >= 18.5 and imc < 25:
    print("Clasificación: Peso normal")
elif imc >= 25 and imc < 30:
    print("Clasificación: Sobrepeso")
else:
    print("Clasificación: Obesidad")

# Reto Semanal 2 finalizado - Segundo commit