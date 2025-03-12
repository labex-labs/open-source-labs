# Formatear e imprimir los datos de la cartera

En este paso, vamos a crear una función que nos ayudará a mostrar los datos de la cartera en una tabla bien organizada. Una cartera es una colección de acciones, y es importante presentar estos datos de manera clara y legible. Aquí es donde entra en juego la función `print_portfolio(portfolio)`. Esta función tomará una cartera como entrada y la mostrará en una tabla con encabezados y alineación adecuada.

## Formateo de cadenas en Python

En Python, hay múltiples formas de formatear cadenas. El formateo de cadenas es una habilidad crucial, ya que te permite presentar los datos de manera más organizada y amigable para el usuario.

- El operador `%` es un estilo más antiguo de formateo de cadenas. Es como una plantilla donde puedes insertar valores en lugares específicos de una cadena.
- El método `str.format()` es otra forma. Proporciona más flexibilidad y una sintaxis más limpia para formatear cadenas.
- Las f - cadenas son una característica introducida en Python 3.6 y versiones posteriores. Son muy convenientes, ya que te permiten incrustar expresiones dentro de literales de cadena.

Para este ejercicio, usaremos el operador `%`. Es especialmente útil cuando quieres crear columnas de ancho fijo, que es exactamente lo que necesitamos para nuestra tabla de cartera.

## Instrucciones de implementación

1. Primero, abre el archivo `stock.py` en tu editor. Si ya está abierto, está bien. En este archivo escribiremos nuestra función `print_portfolio`.

2. Una vez que el archivo esté abierto, busca el comentario `# TODO: Add print_portfolio(portfolio) function here`. Este comentario es un marcador que nos indica dónde agregar nuestra nueva función.

3. Debajo de ese comentario, agrega la siguiente función:

```python
def print_portfolio(portfolio):
    """
    Print the portfolio data in a nicely formatted table.

    Args:
        portfolio (list): A list of Stock objects
    """
    # Print the header row
    print('%10s %10s %10s' % ('name', 'shares', 'price'))

    # Print a separator line
    print('-' * 10 + ' ' + '-' * 10 + ' ' + '-' * 10)

    # Print each stock in the portfolio
    for stock in portfolio:
        print('%10s %10d %10.2f' % (stock.name, stock.shares, stock.price))
```

Esta función primero imprime la fila de encabezados de la tabla, luego una línea separadora y, finalmente, recorre cada acción en la cartera e imprime sus detalles de manera formateada.

4. Después de agregar la función, guarda el archivo. Puedes hacer esto presionando `Ctrl+S` o seleccionando "Archivo > Guardar" desde el menú. Guardar el archivo asegura que tus cambios se conserven.

5. Ahora, necesitamos probar nuestra función. Crea un nuevo archivo llamado `test_print.py`. Este archivo será nuestro script de prueba. Agrega el siguiente código a él:

```python
# test_print.py
from stock import read_portfolio, print_portfolio

# Read the portfolio from the CSV file
portfolio = read_portfolio('portfolio.csv')

# Print the portfolio as a formatted table
print_portfolio(portfolio)
```

Este script importa las funciones `read_portfolio` y `print_portfolio` del archivo `stock.py`. Luego lee los datos de la cartera de un archivo CSV y usa nuestra recién creada función `print_portfolio` para mostrarlos.

6. Finalmente, ejecuta el script de prueba. Abre tu terminal y escribe el siguiente comando:

```bash
python3 test_print.py
```

Si todo está funcionando correctamente, deberías ver una salida como esta:

```
      name     shares      price
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
```

Esta salida confirma que tu función `print_portfolio` está funcionando como se espera. Formatea y muestra los datos de la cartera en una tabla con encabezados y columnas alineadas, lo que lo hace fácil de leer.

## Comprender el formateo de cadenas

Echemos un vistazo más de cerca a cómo funciona el formateo de cadenas en la función `print_portfolio`.

- `%10s` se utiliza para formatear una cadena. El `10` indica el ancho del campo, y la `s` representa una cadena. Alinea la cadena a la derecha dentro de un campo de ancho 10.
- `%10d` es para formatear un entero. El `10` es el ancho del campo, y `d` representa un entero. También alinea el entero a la derecha en un campo de ancho 10.
- `%10.2f` se utiliza para formatear un número de punto flotante. El `10` es el ancho del campo, y el `.2` especifica que queremos mostrar el número de punto flotante con 2 decimales. Alinea el número de punto flotante a la derecha en un campo de ancho 10.

Este formateo asegura que todas las columnas en nuestra tabla estén adecuadamente alineadas, lo que hace que la salida sea mucho más fácil de leer y entender.
