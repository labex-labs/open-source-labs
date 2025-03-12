# Procesando los datos

Ahora que hemos aprendido cómo leer un archivo, el siguiente paso es procesar cada línea del archivo para calcular el costo de cada compra de acciones. Esta es una parte importante de trabajar con datos en Python, ya que nos permite extraer información significativa del archivo.

Cada línea del archivo sigue un formato específico: `[Stock Symbol] [Number of Shares] [Price per Share]`. Para calcular el costo de cada compra de acciones, necesitamos extraer el número de acciones y el precio por acción de cada línea. Luego, multiplicamos estos dos valores juntos para obtener el costo de esa compra de acciones en particular. Finalmente, agregamos este costo a nuestro total acumulado para encontrar el costo total de la cartera.

Modifiquemos la función `portfolio_cost()` en el archivo `pcost.py` para lograr esto. Aquí está el código modificado:

```python
def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file
    """
    total_cost = 0.0

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

            # Calculate the cost of this stock purchase
            cost = shares * price

            # Add to the total cost
            total_cost += cost

            # Print some debug information
            print(f'{fields[0]}: {shares} shares at ${price:.2f} = ${cost:.2f}')

    # Return the total cost
    return total_cost
```

Analicemos paso a paso lo que hace esta función modificada:

1. **Elimina espacios en blanco**: Utilizamos el método `strip()` para eliminar cualquier espacio en blanco inicial o final de cada línea. Esto asegura que no incluyamos accidentalmente espacios adicionales cuando dividimos la línea en campos.
2. **Omite líneas vacías**: Si una línea está vacía (es decir, contiene solo espacios en blanco), utilizamos la declaración `continue` para omitirla. Esto nos ayuda a evitar errores al intentar dividir una línea vacía.
3. **Divide la línea en campos**: Utilizamos el método `split()` para dividir cada línea en una lista de campos basada en espacios en blanco. Esto nos permite acceder a cada parte de la línea por separado.
4. **Extrae los datos relevantes**: Extraemos el número de acciones y el precio por acción de la lista de campos. El número de acciones es el segundo campo, y el precio por acción es el tercer campo. Convertimos estos valores a los tipos de datos adecuados (`int` para las acciones y `float` para el precio) para poder realizar operaciones aritméticas con ellos.
5. **Calcula el costo**: Multiplicamos el número de acciones por el precio por acción para calcular el costo de esta compra de acciones.
6. **Agrega al total**: Agregamos el costo de esta compra de acciones al total acumulado.
7. **Imprime información de depuración**: Imprimimos información sobre cada compra de acciones para ayudarnos a ver lo que está sucediendo. Esto incluye el símbolo de la acción, el número de acciones, el precio por acción y el costo total de la compra.

Ahora, ejecutemos el código para ver si funciona. Abre tu terminal y ejecuta el siguiente comando:

```bash
python3 ~/project/pcost.py
```

Después de ejecutar el comando, deberías ver información detallada sobre cada compra de acciones, seguida del costo total de la cartera. Esta salida te ayudará a verificar que la función está funcionando correctamente y que has calculado el costo total con precisión.
