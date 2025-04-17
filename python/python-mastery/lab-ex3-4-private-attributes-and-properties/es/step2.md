# Conversión de Métodos a Propiedades

Las propiedades (properties) en Python le permiten acceder a valores calculados como si fueran atributos. Esto elimina la necesidad de paréntesis al llamar a un método, lo que hace que su código sea más limpio y consistente.

Actualmente, nuestra clase `Stock` tiene un método `cost()` que calcula el costo total de las acciones.

```python
def cost(self):
    return self.shares * self.price
```

Para obtener el valor del costo, tenemos que llamarlo con paréntesis:

```python
s = Stock('GOOG', 100, 490.10)
print(s.cost())  # Calls the method
```

Podemos mejorar esto convirtiendo el método `cost()` en una propiedad, lo que nos permite acceder al valor del costo sin paréntesis:

```python
s = Stock('GOOG', 100, 490.10)
print(s.cost)  # Accesses the property
```

**Instrucciones:**

1.  Abra el archivo `stock.py` en el editor.

2.  Reemplace el método `cost()` con una propiedad utilizando el decorador `@property`:

    ```python
    @property
    def cost(self):
        return self.shares * self.price
    ```

3.  Guarde el archivo `stock.py`.

4.  Cree un nuevo archivo llamado `test_property.py` en el editor:

    ```bash
    touch /home/labex/project/test_property.py
    ```

5.  Añada el siguiente código al archivo `test_property.py` para crear una instancia de `Stock` y acceder a la propiedad `cost`:

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

6.  Ejecute el script de prueba:

    ```bash
    python /home/labex/project/test_property.py
    ```

    Debería ver una salida similar a:

    ```
    Stock: GOOG
    Shares: 100
    Price: 490.1
    Cost: 49010.0
    ```
