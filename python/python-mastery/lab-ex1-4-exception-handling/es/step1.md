# Definición de una función

En este paso, aprenderemos cómo crear una función. Una función en Python es un bloque de código organizado y reutilizable que se utiliza para realizar una única acción relacionada. Aquí, nuestra función leerá los datos de una cartera (portfolio) desde un archivo y calculará el costo total. Esto es útil porque una vez que tenemos esta función, podemos usarla múltiples veces con diferentes archivos de cartera, evitando tener que escribir el mismo código una y otra vez.

## Comprensión del problema

En el laboratorio anterior, es posible que hayas escrito algún código para leer los datos de una cartera y calcular el costo total. Pero ese código probablemente se escribió de una manera que no se puede reutilizar fácilmente. Ahora, vamos a convertir ese código en una función reutilizable.

Los archivos de datos de cartera tienen un formato específico. Contienen información en la forma de "Símbolo Acciones Precio". Cada línea en el archivo representa una inversión en una acción. Por ejemplo, en un archivo llamado `portfolio.dat`, podrías ver líneas como esta:

```
AA 100 32.20
IBM 50 91.10
...
```

Aquí, la primera parte (como "AA" o "IBM") es el símbolo de la acción, que es un identificador único para la acción. La segunda parte es el número de acciones que posees de esa acción, y la tercera parte es el precio por acción.

## Creación de la función

Vamos a crear un archivo de Python llamado `pcost.py` en el directorio `/home/labex/project`. Este archivo contendrá nuestra función. Aquí está el código que pondremos en el archivo `pcost.py`:

```python
def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file

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
            # Extract the data (symbol, shares, price)
            shares = int(fields[1])
            price = float(fields[2])
            # Add the cost to our running total
            total_cost += shares * price

    return total_cost

# Call the function with the portfolio.dat file
if __name__ == '__main__':
    cost = portfolio_cost('/home/labex/project/portfolio.dat')
    print(cost)
```

En este código, primero definimos una función llamada `portfolio_cost` que toma un `filename` como argumento. Dentro de la función, inicializamos una variable `total_cost` a 0.0. Luego abrimos el archivo usando la función `open` en modo lectura (`'r'`). Usamos un bucle `for` para recorrer cada línea del archivo. Para cada línea, la dividimos en campos usando el método `split()`. Luego extraemos el número de acciones y lo convertimos a un entero, y el precio y lo convertimos a un número de punto flotante. Calculamos el costo de esa inversión en acciones multiplicando el número de acciones por el precio y lo sumamos al `total_cost`. Finalmente, devolvemos el `total_cost`.

La parte `if __name__ == '__main__':` se utiliza para llamar a la función cuando el script se ejecuta directamente. Pasamos la ruta al archivo `portfolio.dat` a la función y mostramos el resultado.

## Prueba de la función

Ahora, vamos a ejecutar el programa para ver si funciona. Necesitamos navegar al directorio donde se encuentra el archivo `pcost.py` y luego ejecutar el script de Python. Aquí están los comandos para hacer eso:

```bash
cd /home/labex/project
python3 pcost.py
```

Después de ejecutar estos comandos, deberías ver la salida:

```
44671.15
```

Esta salida representa el costo total de todas las acciones en la cartera.

## Comprensión del código

Vamos a desglosar lo que hace nuestra función paso a paso:

1. Toma un `filename` como parámetro de entrada. Esto nos permite usar la función con diferentes archivos de cartera.
2. Abre el archivo y lo lee línea por línea. Esto se hace usando la función `open` y un bucle `for`.
3. Para cada línea, la divide en campos usando el método `split()`. Este método divide la línea en una lista de cadenas basada en los espacios en blanco.
4. Convierte el número de acciones a un entero y el precio a un número de punto flotante. Esto es necesario porque los datos leídos del archivo están en formato de cadena, y necesitamos realizar operaciones aritméticas con ellos.
5. Calcula el costo (acciones \* precio) para cada inversión en acciones y lo suma al total acumulado. Esto nos da el costo total de la cartera.
6. Devuelve el costo total final. Esto nos permite usar el resultado en otras partes de nuestro programa si es necesario.

Esta función ahora es reutilizable. Podemos llamarla con diferentes archivos de cartera para calcular sus costos, lo que hace que nuestro código sea más eficiente y más fácil de mantener.
