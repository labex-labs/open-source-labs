# Conversión de Métodos en Propiedades

En Python, las propiedades son una característica poderosa que te permite acceder a valores calculados de manera similar a cómo accedes a los atributos. Normalmente, cuando quieres obtener un valor de un método, necesitas usar paréntesis para llamar a ese método. Sin embargo, las propiedades eliminan la necesidad de estos paréntesis, lo que hace que tu código se vea más limpio y más consistente con cómo accedes a los atributos normales.

Echemos un vistazo a nuestra clase `Stock` actual. Tiene un método `cost()` que calcula el costo total de las acciones. Este método multiplica el número de acciones por el precio por acción para darnos el costo total. Así es como se ve el método `cost()`:

```python
def cost(self):
    return self.shares * self.price
```

Para obtener el valor del costo utilizando este método, tenemos que llamarlo con paréntesis, así:

```python
s = Stock('GOOG', 100, 490.10)
print(s.cost())  # Calls the method
```

Pero podemos mejorar nuestro código. Al convertir el método `cost()` en una propiedad, podemos acceder al valor del costo de la misma manera que accedemos a otros atributos, sin usar paréntesis. Así es como se vería:

```python
s = Stock('GOOG', 100, 490.10)
print(s.cost)  # Accesses the property
```

## Instrucciones:

1. Primero, necesitamos abrir el archivo `stock.py` en el editor. Aquí es donde se define la clase `Stock`, y realizaremos cambios en ella. Utiliza el siguiente comando en la terminal:

   ```bash
   code /home/labex/project/stock.py
   ```

2. Dentro del archivo `stock.py`, vamos a reemplazar el método `cost()` con una propiedad. Usaremos el decorador `@property` para hacer esto. El decorador `@property` le dice a Python que el siguiente método debe tratarse como una propiedad. Reemplaza el método `cost()` con el siguiente código:

   ```python
   @property
   def cost(self):
       return self.shares * self.price
   ```

3. Después de realizar los cambios, guarda el archivo `stock.py`. Esto asegura que nuestras modificaciones se almacenen y se puedan usar más tarde.

4. Ahora, necesitamos crear un sencillo script de Python para probar nuestra nueva propiedad. Abre un nuevo archivo llamado `test_property.py` en el editor utilizando el siguiente comando:

   ```bash
   code /home/labex/project/test_property.py
   ```

5. En el archivo `test_property.py`, agregaremos algún código para crear una instancia de `Stock` y acceder a la propiedad `cost`. Aquí está el código que debes agregar:

   ```python
   from stock import Stock

   # Create a stock instance
   s = Stock('GOOG', 100, 490.10)

   # Access cost as a property (no parentheses)
   print(f"Stock: {s.name}")
   print(f"Shares: {s.shares}")
   print(f"Price: {s.price}")
   print(f"Cost: {s.cost}")  # Using the property
   ```

6. Finalmente, ejecuta el script de prueba para ver si nuestra propiedad funciona como se espera. Utiliza el siguiente comando en la terminal:
   ```bash
   python /home/labex/project/test_property.py
   ```

Deberías ver una salida similar a:

```
Stock: GOOG
Shares: 100
Price: 490.1
Cost: 49010.0
```

Observa cómo ahora podemos acceder a `cost` como un atributo (sin paréntesis), lo que hace que nuestro código sea más consistente con cómo accedemos a otros atributos como `name`, `shares` y `price`. Esto hace que nuestro código sea más fácil de leer y mantener.
