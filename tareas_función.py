def calcular_total_compra(precio_unitario, cantidad):
    total = precio_unitario * cantidad
    return total


if __name__ == "__main__":
    precio = float(input("Ingrese el precio unitario del producto: $"))
    cantidad = int(input("Ingrese la cantidad comprada: "))

    resultado = calcular_total_compra(precio, cantidad)

    print(f"El total a pagar es: ${resultado:.2f}")