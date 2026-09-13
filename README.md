Nombre del Estudiante:

ANTONIO FRANCISCO POZO ZAMBRANO

# Calcular el total de una compra

## Objetivo

Calcular el total a pagar por una compra a partir del precio unitario de un producto y la cantidad comprada.

## Funcionamiento

El programa define una función calcular_total_compra(precio_unitario, cantidad) que multiplica el precio por la cantidad y retorna el total. Desde el bloque principal se piden esos datos al usuario, se llama a la función y se muestra el resultado en pantalla.

## Pseudocódigo


INICIO

DEFINIR FUNCION calcular_total_compra(precio_unitario, cantidad)
    total <- precio_unitario * cantidad
    RETORNAR total
FIN FUNCION

// Bloque principal
LEER precio_unitario
LEER cantidad

resultado <- calcular_total_compra(precio_unitario, cantidad)

ESCRIBIR "El total a pagar es:", resultado

FIN


## Cómo ejecutar

bash
python3 calcular_total_compra.py


Ejemplo:


Ingrese el precio unitario del producto: $10.5
Ingrese la cantidad comprada: 3
El total a pagar es: $31.50
