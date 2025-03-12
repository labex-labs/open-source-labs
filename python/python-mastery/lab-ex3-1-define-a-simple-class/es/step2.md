# Leer una cartera desde un archivo CSV

En este paso, vamos a crear una función que lea datos de acciones desde un archivo CSV y devuelva una lista de objetos `Stock`. Un objeto `Stock` representa una participación en acciones, y al final de este paso, podrás leer una cartera de acciones desde un archivo CSV.

## Comprender los archivos CSV

CSV, que significa Valores Separados por Comas (Comma-Separated Values en inglés), es un formato muy común para almacenar datos tabulares. Puedes pensar en él como una hoja de cálculo simple. Cada línea en un archivo CSV representa una fila de datos, y las columnas dentro de esa fila están separadas por comas. Por lo general, la primera línea de un archivo CSV contiene encabezados. Estos encabezados describen qué tipo de datos hay en cada columna. Por ejemplo, en un archivo CSV de una cartera de acciones, los encabezados podrían ser "Nombre", "Acciones" y "Precio".

## Instrucciones de implementación

1. Primero, abre el archivo `stock.py` en tu editor de código. Si ya está abierto, ¡estupendo! Si no, encuéntralo y ábrelo. Aquí es donde agregaremos nuestra nueva función.

2. Una vez que el archivo `stock.py` esté abierto, busca el comentario `# TODO: Add read_portfolio(filename) function here`. Este comentario es un marcador que nos indica dónde colocar nuestra nueva función.

3. Debajo de ese comentario, agrega la siguiente función. Esta función se llama `read_portfolio` y toma un nombre de archivo como argumento. El propósito de esta función es leer el archivo CSV, extraer los datos de las acciones y crear una lista de objetos `Stock`.

```python
def read_portfolio(filename):
    """
    Read a CSV file containing portfolio data and return a list of Stock objects.

    Args:
        filename (str): Path to the CSV file

    Returns:
        list: A list of Stock objects
    """
    portfolio = []

    with open(filename, 'r') as f:
        headers = next(f).strip().split(',')  # Skip the header line

        for line in f:
            row = line.strip().split(',')
            name = row[0]
            shares = int(row[1])
            price = float(row[2])

            # Create a Stock object and add it to the portfolio list
            stock = Stock(name, shares, price)
            portfolio.append(stock)

    return portfolio
```

Analicemos lo que hace esta función. Primero, crea una lista vacía llamada `portfolio`. Luego, abre el archivo CSV en modo lectura. La declaración `next(f)` omite la primera línea, que es la línea de encabezados. Después de eso, recorre cada línea del archivo. Para cada línea, divide la línea en una lista de valores, extrae el nombre, la cantidad de acciones y el precio, crea un objeto `Stock` y lo agrega a la lista `portfolio`. Finalmente, devuelve la lista `portfolio`.

4. Después de agregar la función, guarda el archivo `stock.py`. Puedes hacer esto presionando `Ctrl+S` en tu teclado o seleccionando "Archivo > Guardar" desde el menú de tu editor de código. Guardar el archivo asegura que tus cambios se conserven.

5. Ahora, necesitamos probar nuestra función `read_portfolio`. Crea un nuevo script de Python llamado `test_portfolio.py`. Este script importará la función `read_portfolio` del archivo `stock.py`, leerá la cartera desde un archivo CSV e imprimirá información sobre cada acción en la cartera.

```python
# test_portfolio.py
from stock import read_portfolio

# Read the portfolio from the CSV file
portfolio = read_portfolio('portfolio.csv')

# Print information about each stock
for stock in portfolio:
    print(f"Name: {stock.name}, Shares: {stock.shares}, Price: ${stock.price:.2f}")

# Print the total number of stocks in the portfolio
print(f"\nTotal number of stocks in portfolio: {len(portfolio)}")
```

En este script, primero importamos la función `read_portfolio`. Luego, llamamos a la función con el nombre de archivo `portfolio.csv` para obtener la lista de objetos `Stock`. Después de eso, recorremos la lista e imprimimos información sobre cada acción. Finalmente, imprimimos el número total de acciones en la cartera.

6. Para ejecutar el script de prueba, abre tu terminal o símbolo del sistema, navega hasta el directorio donde se encuentra el archivo `test_portfolio.py` y ejecuta el siguiente comando:

```bash
python3 test_portfolio.py
```

Si todo está funcionando correctamente, deberías ver una salida que enumere todas las acciones del archivo `portfolio.csv`, junto con sus nombres, cantidad de acciones y precios. También deberías ver el número total de acciones en la cartera.

```
Name: AA, Shares: 100, Price: $32.20
Name: IBM, Shares: 50, Price: $91.10
Name: CAT, Shares: 150, Price: $83.44
Name: MSFT, Shares: 200, Price: $51.23
Name: GE, Shares: 95, Price: $40.37
Name: MSFT, Shares: 50, Price: $65.10
Name: IBM, Shares: 100, Price: $70.44

Total number of stocks in portfolio: 7
```

Esta salida confirma que tu función `read_portfolio` está leyendo correctamente el archivo CSV y creando objetos `Stock` a partir de sus datos.
