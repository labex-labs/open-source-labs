# Finalizando el programa

Ahora, vamos a limpiar nuestro código y crear la versión final del programa `pcost.py`. Limpiar el código significa eliminar cualquier parte innecesaria y asegurarnos de que la salida se vea bien. Este es un paso importante en la programación porque hace que nuestro código sea más profesional y fácil de entender.

Comenzaremos eliminando las declaraciones de impresión de depuración. Estas declaraciones se utilizan durante el desarrollo para verificar los valores de las variables y el flujo del programa, pero no son necesarias en la versión final. Luego, nos aseguraremos de que la salida final esté bien formateada.

Aquí está la versión final del código de `pcost.py`:

```python
# pcost.py
# Calculate the total cost of a portfolio of stocks

def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file
    """
    total_cost = 0.0

    try:
        # Open the file
        with open(filename, 'r') as file:
            # Read all lines in the file
            for line in file:
                # Strip any leading/trailing whitespace
                line = line.strip()

                # Skip empty lines
                if not line:
                    continue

                # Split the line into fields
                fields = line.split()

                # Extract the relevant data
                # fields[0] is the stock symbol (which we don't need for the calculation)
                shares = int(fields[1])  # Number of shares (second field)
                price = float(fields[2])  # Price per share (third field)

                # Calculate the cost of this stock purchase and add to the total
                total_cost += shares * price

    except FileNotFoundError:
        print(f"Error: Could not find file '{filename}'")
        return 0.0
    except Exception as e:
        print(f"Error processing file: {e}")
        return 0.0

    # Return the total cost
    return total_cost

# Main block to run when the script is executed directly
if __name__ == '__main__':
    # Call the function with the portfolio file
    total_cost = portfolio_cost('portfolio.dat')
    print(f'Total cost: ${total_cost:.2f}')
```

Esta versión final del código tiene varias mejoras:

1. Manejo de errores: Hemos agregado código para capturar dos tipos de errores. El `FileNotFoundError` se levanta cuando el archivo especificado no existe. Si esto sucede, el programa imprimirá un mensaje de error y devolverá 0.0. El bloque `Exception` captura cualquier otro error que pueda ocurrir mientras se procesa el archivo. Esto hace que nuestro programa sea más robusto y menos propenso a fallar inesperadamente.
2. Formato adecuado: El costo total se formatea con dos decimales utilizando el especificador de formato `:.2f` en la f-string. Esto hace que la salida se vea más profesional y sea más fácil de leer.
3. Verificación de `__name__ == '__main__'`: Este es un término común en Python. Asegura que el código dentro del bloque `if` solo se ejecute cuando el script se ejecuta directamente. Si el script se importa como un módulo en otro script, este código no se ejecutará. Esto nos da más control sobre cómo se comporta nuestro script.

Ahora, ejecutemos el código final. Abre tu terminal y escribe el siguiente comando:

```bash
python3 ~/project/pcost.py
```

Cuando ejecutes este comando, el programa leerá el archivo `portfolio.dat`, calculará el costo total de la cartera y imprimirá el resultado. Deberías ver el costo total de la cartera, que debería ser $44671.15.

¡Felicidades! Has creado con éxito un programa en Python que lee datos de un archivo, los procesa y calcula un resultado. Este es un gran logro y muestra que estás en el camino de convertirse en un programador Python competente.
