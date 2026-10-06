# Calculadora de IMC en Python

Este proyecto es la entrega final del módulo 1 **Fundamentos de Python**.

## Descripción del Programa
Es un script interactivo que solicita al usuario sus datos personales (nombre, apellidos, edad, peso y estatura) a través de la consola. El programa calcula el Índice de Masa Corporal (IMC) utilizando la fórmula estándar y clasifica el resultado en bajo peso, peso normal, sobrepeso u obesidad. 

Además, el programa ha sido desarrollado con **validaciones robustas** para evitar errores:
- No permite campos de texto vacíos.
- Evita que el programa falle si el usuario ingresa letras en lugar de números (manejo de excepciones).
- Formatea los nombres para que siempre tengan mayúsculas iniciales.

## Instrucciones de Ejecución
Para ejecutar este programa en tu computadora, necesitas tener instalado Python 3.

1. Descarga o clona este repositorio.
2. Abre una terminal (o la terminal integrada de VS Code) en la carpeta del proyecto.
3. Ejecuta el siguiente comando:
   ```bash
   python calculadora_imc.py