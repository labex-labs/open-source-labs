# Incorporación del manejo de errores

Cuando se trabaja con datos del mundo real, es muy común encontrar inconsistencias o errores. Por ejemplo, los datos pueden tener valores faltantes, formatos incorrectos u otros problemas. Python ofrece mecanismos de manejo de excepciones para tratar estas situaciones de manera elegante. El manejo de excepciones permite que tu programa siga ejecutándose incluso cuando encuentra un error, en lugar de terminar abruptamente.

## Comprensión del problema

Echemos un vistazo al archivo `portfolio3.dat`. Este archivo contiene algunos datos sobre una cartera (portfolio), como el símbolo de la acción, el número de acciones y el precio por acción. Para ver el contenido de este archivo, podemos usar el siguiente comando:

```bash
cat /home/labex/project/portfolio3.dat
```

Cuando ejecutes este comando, notarás que algunas líneas del archivo tienen guiones (`-`) en lugar de números para el número de acciones. Aquí tienes un ejemplo de lo que podrías ver:

```
AA 100 32.20
IBM 50 91.10
C - 53.08
...
```

Si intentamos ejecutar nuestro código actual con este archivo, se detendrá con un error. La razón es que nuestro código espera convertir el número de acciones en un entero, pero no puede convertir un guión (`-`) en un entero. Intentemos ejecutar el código y veamos qué sucede:

```bash
python3 -c "import sys; sys.path.append('/home/labex/project'); from pcost import portfolio_cost; print(portfolio_cost('/home/labex/project/portfolio3.dat'))"
```

Verás un mensaje de error como este:

```
ValueError: invalid literal for int() with base 10: '-'
```

Este error se produce porque Python no puede convertir el carácter `-` en un entero cuando intenta ejecutar `int(fields[1])`.

## Introducción al manejo de excepciones

El manejo de excepciones en Python utiliza bloques `try` y `except`. El bloque `try` contiene el código que podría generar una excepción. Una excepción es un error que ocurre durante la ejecución de un programa. El bloque `except` contiene el código que se ejecutará si se produce una excepción en el bloque `try`.

Aquí tienes un ejemplo de cómo funcionan los bloques `try` y `except`:

```python
try:
    # Code that might raise an exception
    result = risky_operation()
except ExceptionType as e:
    # Code to handle the exception
    print(f"An error occurred: {e}")
```

Cuando Python ejecuta el código en el bloque `try`, si se produce una excepción, la ejecución salta inmediatamente al bloque `except` coincidente. El `ExceptionType` en el bloque `except` especifica el tipo de excepción que queremos manejar. La variable `e` contiene información sobre la excepción, como el mensaje de error.

## Modificación de la función con manejo de excepciones

Vamos a actualizar nuestro archivo `pcost.py` para manejar los errores en los datos. Usaremos los bloques `try` y `except` para omitir las líneas con datos incorrectos y mostrar un mensaje de advertencia.

```python
def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file
    Handles lines with bad data by skipping them and showing a warning.

    Args:
        filename: The name of the portfolio file

    Returns:
        The total cost of the portfolio as a float
    """
    total_cost = 0.0

    # Open the file and read through each line
    with open(filename, 'r') as f:
        for line in f:
            fields = line.split()
            try:
                # Extract the data (symbol, shares, price)
                shares = int(fields[1])
                price = float(fields[2])
                # Add the cost to our running total
                total_cost += shares * price
            except ValueError as e:
                # Print a warning for lines that can't be parsed
                print(f"Couldn't parse: '{line}'")
                print(f"Reason: {e}")

    return total_cost

# Call the function with the portfolio3.dat file
if __name__ == '__main__':
    cost = portfolio_cost('/home/labex/project/portfolio3.dat')
    print(cost)
```

En este código actualizado, primero abrimos el archivo y lo leemos línea por línea. Para cada línea, la dividimos en campos. Luego, intentamos convertir el número de acciones en un entero y el precio en un número de punto flotante. Si esta conversión falla (es decir, se produce un `ValueError`), mostramos un mensaje de advertencia y omitimos esa línea. De lo contrario, calculamos el costo de las acciones y lo sumamos al costo total.

## Prueba de la función actualizada

Ahora, ejecutemos el programa actualizado con el archivo problemático. Primero, debemos navegar al directorio del proyecto y luego podemos ejecutar el script de Python.

```bash
cd /home/labex/project
python3 pcost.py
```

Deberías ver una salida como esta:

```
Couldn't parse: 'C - 53.08
'
Reason: invalid literal for int() with base 10: '-'
Couldn't parse: 'DIS - 34.20
'
Reason: invalid literal for int() with base 10: '-'
44671.15
```

El programa ahora hace lo siguiente:

1. Intenta procesar cada línea del archivo.
2. Si una línea contiene datos no válidos, captura el `ValueError`.
3. Muestra un mensaje útil sobre el problema.
4. Continúa procesando el resto del archivo.
5. Devuelve el costo total basado en las líneas válidas.

Este enfoque hace que nuestro programa sea mucho más robusto al tratar con datos imperfectos. Puede manejar los errores de manera elegante y aún proporcionar resultados útiles.
