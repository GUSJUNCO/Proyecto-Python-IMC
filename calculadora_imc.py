# =====================================================================
# Proyecto Final: Calculadora de IMC Robusta
# Fundamentos de Python - M1S4
# =====================================================================

print("--- Calculadora de IMC ---")

# ---------------------------------------------------------------------
# VALIDACIÓN 1: Evitar campos vacíos en texto
# Usamos un bucle 'while' que se repite hasta que el usuario escriba algo.
# ---------------------------------------------------------------------
while True:
    nombre = input("Ingresa tu nombre: ").strip().title()
    if nombre != "":
        break # Si escribió algo, salimos del bucle
    print("Error: El nombre no puede estar vacío. Intenta de nuevo.")

while True:
    apellido_paterno = input("Ingresa tu apellido paterno: ").strip().title()
    if apellido_paterno != "":
        break
    print("Error: El apellido paterno no puede estar vacío.")

while True:
    apellido_materno = input("Ingresa tu apellido materno: ").strip().title()
    if apellido_materno != "":
        break
    print("Error: El apellido materno no puede estar vacío.")

# ---------------------------------------------------------------------
# VALIDACIÓN 2: Asegurar que edad, peso y estatura sean números válidos
# Usamos 'try' (intentar) y 'except' (capturar el error).
# Si el usuario escribe letras, Python lanzará un error (ValueError),
# el 'except' lo atrapará y le pedirá el dato de nuevo.
# ---------------------------------------------------------------------

# Validar Edad 
while True:
    try:
        edad = int(input("Ingresa tu edad (años): "))
        if edad > 0: # Validación extra: la edad no puede ser negativa o cero
            break
        else:
            print("Error: La edad debe ser un número positivo.")
    except ValueError:
        print("Error: Debes ingresar un número entero (sin letras ni decimales).")

# Validar Peso 
while True:
    try:
        peso = float(input("Ingresa tu peso (kg): "))
        if peso > 0:
            break
        else:
            print("Error: El peso debe ser un número positivo.")
    except ValueError:
        print("Error: Debes ingresar un número válido para el peso.")

# Validar Estatura 
while True:
    try:
        estatura = float(input("Ingresa tu estatura (m): "))
        if estatura > 0:
            break
        else:
            print("Error: La estatura debe ser un número positivo.")
    except ValueError:
        print("Error: Debes ingresar un número válido para la estatura.")

# ---------------------------------------------------------------------
# CÁLCULO DEL IMC
# ---------------------------------------------------------------------

imc = peso / (estatura ** 2)

# ---------------------------------------------------------------------
# MOSTRAR RESULTADOS
# ---------------------------------------------------------------------
print("\n--- Resultados ---")
print(f"Paciente: {nombre} {apellido_paterno} {apellido_materno}")
print(f"Edad: {edad} años")
print(f"Peso: {peso} kg")
print(f"Estatura: {estatura} m")
print(f"Tu IMC es: {imc:.2f}")

if imc < 18.5:
    print("Clasificación: Bajo peso")
elif imc >= 18.5 and imc < 25:
    print("Clasificación: Peso normal")
elif imc >= 25 and imc < 30:
    print("Clasificación: Sobrepeso")
else:
    print("Clasificación: Obesidad")