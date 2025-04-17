# Implementación de Atributos Privados

En Python, utilizamos una convención de nomenclatura para indicar que un atributo está destinado al uso interno dentro de una clase. Prefijamos estos atributos con un guion bajo (`_`). Esto indica a otros desarrolladores que estos atributos no forman parte de la API pública y no deben accederse directamente desde fuera de la clase.

Veamos la clase `Stock` actual en el archivo `stock.py`. Tiene una variable de clase llamada `types`.

```python
class Stock:
    # Class variable for type conversions
    types = (str, int, float)

    # Rest of the class...
```

La variable de clase `types` se utiliza internamente para convertir los datos de las filas. Para indicar que se trata de un detalle de implementación, la marcaremos como privada.

**Instrucciones:**

1.  Abra el archivo `stock.py` en el editor.

2.  Modifique la variable de clase `types` añadiendo un guion bajo al principio, cambiándola a `_types`.

    ```python
    class Stock:
        # Class variable for type conversions
        _types = (str, int, float)

        # Rest of the class...
    ```

3.  Actualice el método `from_row` para utilizar la variable renombrada `_types`.

    ```python
    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)
    ```

4.  Guarde el archivo `stock.py`.

5.  Cree un script de Python llamado `test_stock.py` para probar sus cambios. Puede crear el archivo en el editor utilizando el siguiente comando:

    ```bash
    touch /home/labex/project/test_stock.py
    ```

6.  Añada el siguiente código al archivo `test_stock.py`. Este código crea instancias de la clase `Stock` e imprime información sobre ellas.

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

7.  Ejecute el script de prueba utilizando el siguiente comando en la terminal:

    ```bash
    python /home/labex/project/test_stock.py
    ```

    Debería ver una salida similar a:

    ```
    Name: GOOG, Shares: 100, Price: 490.1
    Cost: 49010.0
    Name: AAPL, Shares: 50, Price: 142.5
    Cost: 7125.0
    ```
