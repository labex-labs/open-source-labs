# Implementación de Atributos Privados

En Python, cuando diseñamos una clase, hay ciertos atributos que solo están destinados a ser utilizados dentro de la propia clase. Estos atributos son parte de la implementación interna de la clase. Para indicar esto a otros desarrolladores, seguimos una convención de nomenclatura. Anteponemos un guión bajo (`_`) a estos atributos internos. Esto es como una señal que dice que estos atributos no forman parte de la API pública. La API pública es el conjunto de métodos y atributos con los que otras partes del código deben interactuar. Por lo tanto, los atributos con un guión bajo no deben ser accedidos directamente desde fuera de la clase.

Echemos un vistazo a la clase `Stock` actual en el archivo `stock.py`. Esta clase se utiliza para representar acciones y tiene una variable de clase llamada `types`.

```python
class Stock:
    # Class variable for type conversions
    types = (str, int, float)

    # Rest of the class...
```

La variable de clase `types` se utiliza dentro de la clase para convertir datos de filas. Por ejemplo, cuando obtenemos datos en una fila, usamos estos tipos para convertir los datos al formato correcto. Dado que esto es solo un detalle de implementación y no algo con lo que otras partes del código deben interactuar directamente, debemos marcarlo como privado.

## Instrucciones:

1. Primero, necesitamos abrir el archivo `stock.py` en el editor. Podemos hacer esto utilizando el siguiente comando en la terminal. Este comando abrirá el archivo en el editor de código.

   ```bash
   code /home/labex/project/stock.py
   ```

2. Ahora, vamos a modificar la variable de clase `types`. Le agregamos un guión bajo al principio, convirtiéndola en `_types`. Este cambio indica que esta variable es privada y no debe ser accedida directamente desde fuera de la clase.

   ```python
   class Stock:
       # Class variable for type conversions
       _types = (str, int, float)

       # Rest of the class...
   ```

3. Después de renombrar la variable, necesitamos actualizar el método `from_row`. Este método utiliza la variable `types` para convertir datos de filas. Ahora que la hemos renombrado a `_types`, necesitamos actualizar el método en consecuencia.

   ```python
   @classmethod
   def from_row(cls, row):
       values = [func(val) for func, val in zip(cls._types, row)]
       return cls(*values)
   ```

4. Una vez que hayamos realizado estos cambios, necesitamos guardar el archivo. Guardar el archivo asegura que nuestros cambios se almacenen y puedan ser utilizados más tarde.

5. Para probar nuestros cambios, vamos a crear un script de Python llamado `test_stock.py`. Podemos abrir el archivo en el editor utilizando el siguiente comando.

   ```bash
   code /home/labex/project/test_stock.py
   ```

6. Ahora, agregamos el siguiente código al archivo `test_stock.py`. Este código crea instancias de la clase `Stock`, tanto directamente como utilizando el método `from_row`. Luego imprime información sobre estas instancias, como el nombre, el número de acciones, el precio y el costo.

   ```python
   from stock import Stock

   # Create a stock instance
   s = Stock('GOOG', 100, 490.10)
   print(f"Name: {s.name}, Shares: {s.shares}, Price: {s.price}")
   print(f"Cost: {s.cost()}")

   # Create from row
   row = ['AAPL', '50', '142.5']
   apple = Stock.from_row(row)
   print(f"Name: {apple.name}, Shares: {apple.shares}, Price: {apple.price}")
   print(f"Cost: {apple.cost()}")
   ```

7. Finalmente, ejecutamos el script de prueba utilizando el siguiente comando en la terminal. Esto ejecutará el código en el archivo `test_stock.py` y nos mostrará la salida.

   ```bash
   python /home/labex/project/test_stock.py
   ```

Deberías ver una salida similar a:

```
Name: GOOG, Shares: 100, Price: 490.1
Cost: 49010.0
Name: AAPL, Shares: 50, Price: 142.5
Cost: 7125.0
```
