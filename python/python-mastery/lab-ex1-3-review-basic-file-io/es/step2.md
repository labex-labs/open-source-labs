# Abriendo y leyendo el archivo

En este paso, aprenderemos cómo abrir y leer un archivo en Python. La entrada/salida (I/O) de archivos es un concepto fundamental en la programación. Permite que tu programa interactúe con archivos externos, como archivos de texto, archivos CSV, etc. En Python, una de las formas más comunes de trabajar con archivos es utilizando la función `open()`.

La función `open()` se utiliza para abrir un archivo en Python. Toma dos argumentos importantes. El primer argumento es el nombre del archivo que deseas abrir. El segundo argumento es el modo en el que deseas abrir el archivo. Cuando quieres leer un archivo, utilizas el modo 'r'. Esto le dice a Python que solo quieres leer el contenido del archivo y no hacer ningún cambio en él.

Ahora, agreguemos algo de código al archivo `pcost.py` para abrir y leer el archivo `portfolio.dat`. Abre el archivo `pcost.py` en tu editor de código y agrega el siguiente código:

```python
# pcost.py
# Calculate the total cost of a portfolio of stocks

def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file
    """
    total_cost = 0.0

    # Open the file
    with open(filename, 'r') as file:
        # Read all lines in the file
        for line in file:
            print(line)  # Just for debugging, to see what we're reading

    # Return the total cost
    return total_cost

# Call the function with the portfolio file
total_cost = portfolio_cost('portfolio.dat')
print(f'Total cost: ${total_cost}')
```

Analicemos lo que hace este código:

1. Primero, definimos una función llamada `portfolio_cost()`. Esta función toma un nombre de archivo como parámetro de entrada. El propósito de esta función es calcular el costo total de una cartera de acciones basado en los datos del archivo.
2. Dentro de la función, utilizamos la función `open()` para abrir el archivo especificado en modo lectura. La declaración `with` se utiliza aquí para garantizar que el archivo se cierre correctamente después de terminar de leerlo. Esta es una buena práctica para evitar fugas de recursos.
3. Luego, utilizamos un bucle `for` para leer el archivo línea por línea. Para cada línea del archivo, la imprimimos. Esto es solo con fines de depuración, para que podamos ver qué datos estamos leyendo del archivo.
4. Después de leer el archivo, la función devuelve el costo total. Actualmente, el costo total se establece en 0.0 porque aún no hemos implementado el cálculo real.
5. Fuera de la función, llamamos a la función `portfolio_cost()` con el nombre de archivo 'portfolio.dat'. Esto significa que estamos pidiendo a la función que calcule el costo total basado en los datos del archivo `portfolio.dat`.
6. Finalmente, imprimimos el costo total utilizando una f-string.

Ahora, ejecutemos este código para ver qué hace. Puedes ejecutar el archivo de Python desde la terminal utilizando el siguiente comando:

```bash
python3 ~/project/pcost.py
```

Cuando ejecutes este comando, deberías ver cada línea del archivo `portfolio.dat` impresa en la terminal, seguida del costo total, que actualmente está establecido en 0.0. Esta salida te ayuda a verificar que el archivo se esté leyendo correctamente.
