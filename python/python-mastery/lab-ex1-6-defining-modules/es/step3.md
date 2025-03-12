# Crear tu propio módulo

Ahora que entiendes cómo usar módulos existentes, es hora de crear un nuevo módulo desde cero. Un módulo en Python es un archivo que contiene definiciones y declaraciones de Python. Te permite organizar tu código en piezas reutilizables y manejables. Al crear tu propio módulo, puedes agrupar funciones y variables relacionadas, lo que hace que tu código sea más modular y fácil de mantener.

## Crear un módulo de informes

Vamos a crear un módulo simple para generar informes de acciones. Este módulo tendrá funciones para leer un archivo de cartera e imprimir un informe formateado de las acciones en la cartera.

1. Primero, necesitamos crear un nuevo archivo llamado `report.py`. Para hacer esto, usaremos la línea de comandos. Navega al directorio `project` en tu directorio principal y crea el archivo usando el comando `touch`.

```bash
cd ~/project
touch report.py
```

2. Ahora, abre el archivo `report.py` en tu editor de texto preferido y agrega el siguiente código. Este código define dos funciones y un bloque principal.

```python
# report.py

def read_portfolio(filename):
    """
    Read a stock portfolio file into a list of dictionaries with
    keys: name, shares, price
    """
    portfolio = []
    with open(filename, 'r') as f:
        for line in f:
            fields = line.split()
            try:
                stock = {
                    'name': fields[0],
                    'shares': int(fields[1]),
                    'price': float(fields[2])
                }
                portfolio.append(stock)
            except (ValueError, IndexError):
                print(f"Couldn't parse: {line}")
    return portfolio

def print_report(portfolio):
    """
    Print a report showing the stock name, shares, price, and total value
    """
    print("Name    Shares    Price    Value")
    print("-" * 40)
    total_value = 0.0
    for stock in portfolio:
        value = stock['shares'] * stock['price']
        total_value += value
        print(f"{stock['name']:6s} {stock['shares']:9d} {stock['price']:9.2f} {value:9.2f}")
    print("-" * 40)
    print(f"Total Value: {total_value:16.2f}")

if __name__ == "__main__":
    portfolio = read_portfolio('portfolio.dat')
    print_report(portfolio)
```

La función `read_portfolio` lee un archivo que contiene información de acciones y devuelve una lista de diccionarios, donde cada diccionario representa una acción con las claves `name`, `shares` y `price`. La función `print_report` toma una cartera (una lista de diccionarios de acciones) e imprime un informe formateado que muestra el nombre de la acción, el número de acciones, el precio y el valor total. El bloque principal al final se ejecuta cuando el archivo se ejecuta directamente. Lee el archivo de cartera e imprime el informe.

3. Después de agregar el código, guarda y cierra el editor.

## Probar tu módulo

Vamos a probar nuestro nuevo módulo para asegurarnos de que funcione como se espera.

1. Primero, ejecutaremos el script directamente desde la línea de comandos. Esto ejecutará el bloque principal en el archivo `report.py`.

```bash
python3 report.py
```

Deberías ver un informe formateado que muestra las acciones de la cartera y sus valores. Este informe incluye el nombre de la acción, el número de acciones, el precio y el valor total, así como el valor total de toda la cartera.

```
Name    Shares    Price    Value
----------------------------------------
AA         100     32.20   3220.00
IBM         50     91.10   4555.00
CAT        150     83.44  12516.00
MSFT       200     51.23  10246.00
GE          95     40.37   3835.15
MSFT        50     65.10   3255.00
IBM        100     70.44   7044.00
----------------------------------------
Total Value:         44671.15
```

2. A continuación, usaremos el módulo desde el intérprete de Python. Inicia el intérprete de Python ejecutando el comando `python3` en la terminal.

```bash
python3
```

Una vez que el intérprete esté en funcionamiento, podemos importar el módulo `report` y usar sus funciones.

```python
import report
portfolio = report.read_portfolio('portfolio.dat')
len(portfolio)  # Should return 7, the number of stocks
portfolio[0]    # First stock in the portfolio
```

La declaración `import report` hace que las funciones y variables definidas en el archivo `report.py` estén disponibles en la sesión actual de Python. Luego usamos la función `read_portfolio` para leer el archivo de cartera y almacenar el resultado en la variable `portfolio`. La declaración `len(portfolio)` devuelve el número de acciones en la cartera, y `portfolio[0]` devuelve la primera acción en la cartera.

Deberías ver la siguiente salida:

```
7
{'name': 'AA', 'shares': 100, 'price': 32.2}
```

3. Ahora, usemos el módulo importado para calcular el costo total de la cartera nosotros mismos. Iteraremos sobre las acciones en la cartera y sumaremos el valor total de cada acción.

```python
total = 0.0
for stock in portfolio:
    total += stock['shares'] * stock['price']
print(total)
```

La salida debe ser `44671.15`, que es el mismo valor total que imprime la función `print_report`.

4. Finalmente, creemos un informe personalizado para un tipo de acción específico. Filtraremos la cartera para incluir solo las acciones IBM y luego usaremos la función `print_report` para imprimir un informe para esas acciones.

```python
ibm_stocks = [stock for stock in portfolio if stock['name'] == 'IBM']
report.print_report(ibm_stocks)
```

Esto debería imprimir un informe que muestra solo las acciones IBM y sus valores.

```
Name    Shares    Price    Value
----------------------------------------
IBM         50     91.10   4555.00
IBM        100     70.44   7044.00
----------------
Total Value:         11599.00
```

5. Cuando hayas terminado de probar, sal del intérprete de Python ejecutando el comando `exit()`.

```python
exit()
```

Ahora has creado y usado con éxito tu propio módulo de Python, combinando tanto funciones como un bloque principal que solo se ejecuta cuando el archivo se ejecuta directamente. Este enfoque modular de la programación te permite reutilizar código y hacer que tus proyectos estén más organizados y sean más fáciles de mantener.
