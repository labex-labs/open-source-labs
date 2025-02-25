# Ejercicio 1.30: Convertir un script en una función

Tome el código que escribió para el programa `pcost.py` en el Ejercicio 1.27 y conviértalo en una función `portfolio_cost(filename)`. Esta función toma un nombre de archivo como entrada, lee los datos del portafolio en ese archivo y devuelve el costo total del portafolio como un número de punto flotante.

Para usar su función, cambie su programa de modo que se vea más o menos así:

```python
# pcost.py
def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file
    """
    total_cost = 0.0

    with open(filename, "rt") as f:
        rows = f.readlines()
        headers = rows[0].strip().split(",")
        for row in rows[1:]:
            row_data = row.strip().split(",")
            nshares = int(row_data[1])
            price = float(row_data[2])
            total_cost += nshares * price

    return total_cost


import sys

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input("Enter a filename:")

cost = portfolio_cost(filename)
print("Total cost:", cost)
```

Cuando ejecute su programa, debería ver la misma salida que antes. Después de ejecutar su programa, también puede llamar a su función de manera interactiva escribiendo esto:

```bash
$ python3 -i pcost.py
```

Esto le permitirá llamar a su función desde el modo interactivo.

```python
>>> portfolio_cost('portfolio.csv')
44671.15
>>>
```

Poder experimentar con su código de manera interactiva es útil para probar y depurar.
