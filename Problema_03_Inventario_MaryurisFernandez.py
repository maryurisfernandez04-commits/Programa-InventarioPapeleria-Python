# Nombre: Maryuris Fernandez de Castro
# Codigo: 213022_61
# Programa: Ingenieria de Sistemas
# Problema 03: Inventario - Fase 5 


inventario = [
    ["A01", "Lapiz", 25, 10],
    ["A02", "Zacapunta", 15, 5],
    ["A03", "Borrador", 4, 8],
    ["A04", "Cuaderno", 10, 20],
    ["A05", "Colores", 9, 18],
    ["A06", "Juego de geometria", 12, 12],
    ["A07", "Marcadores", 5, 10],
    ["A08", "Carpeta", 3, 7],
]


def calcular_cantidad_pedir(stock_actual, stock_minimo):
    """Determina la cantidad exacta a pedir para cada articulo."""
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0


print("--- Informe de Reabastecimiento del Inventario ---")
for articulo in inventario:
    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    cantidad_a_pedir = calcular_cantidad_pedir(stock_actual, stock_minimo)
    print(f"\nArticulo: {nombre} (Codigo: {codigo})")
    print(f"Stock actual: {stock_actual}")
    print(f"Stock minimo: {stock_minimo}")
    if cantidad_a_pedir > 0:
        print(f"Cantidad a pedir: {cantidad_a_pedir}")
    else:
        print("No requiere reabastecimiento.")

