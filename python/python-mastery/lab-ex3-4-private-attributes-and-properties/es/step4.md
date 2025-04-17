# Usando `__slots__` para la Optimización de Memoria

El atributo `__slots__` restringe los atributos que una clase puede tener. Evita añadir nuevos atributos a las instancias y reduce el uso de memoria.

En nuestra clase `Stock`, utilizaremos `__slots__` para:

1.  Restringir la creación de atributos solo a los atributos que hemos definido.
2.  Mejorar la eficiencia de la memoria, especialmente al crear muchas instancias.

**Instrucciones:**

1.  Abra el archivo `stock.py` en el editor.
2.  Añada una variable de clase `__slots__`, listando todos los nombres de atributos privados utilizados por la clase:

    ```python
    class Stock:
        # Class variable for type conversions
        _types = (str, int, float)

        # Define slots to restrict attribute creation
        __slots__ = ('name', '_shares', '_price')

        # Rest of the class...
    ```

3.  Guarde el archivo.

4.  Cree un script de prueba llamado `test_slots.py`:

    ```bash
    touch /home/labex/project/test_slots.py
    ```

5.  Añada el siguiente código al archivo `test_slots.py`:

    ```python
    from stock import Stock

    # Create a stock instance
    s = Stock('GOOG', 100, 490.10)

    # Access existing attributes
    print(f"Name: {s.name}")
    print(f"Shares: {s.shares}")
    print(f"Price: {s.price}")
    print(f"Cost: {s.cost}")

    # Try to add a new attribute
    try:
        s.extra = "This will fail"
        print(f"Extra: {s.extra}")
    except AttributeError as e:
        print(f"Error: {e}")
    ```

6.  Ejecute el script de prueba:

    ```bash
    python /home/labex/project/test_slots.py
    ```

    Debería ver una salida que muestre que puede acceder a los atributos definidos, pero al intentar añadir un nuevo atributo se genera un `AttributeError`.

    ```plaintext
    Name: GOOG
    Shares: 100
    Price: 490.1
    Cost: 49010.0
    Error: 'Stock' object has no attribute 'extra'
    ```
