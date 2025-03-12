# Mejorando la representación en cadena

Cuando imprimes un objeto `MutInt` en Python, verás una salida como `<__main__.MutInt object at 0x...>`. Esta salida no es muy útil porque no te dice el valor real del objeto `MutInt`. Para facilitar la comprensión de lo que representa el objeto, implementaremos métodos especiales para la representación en cadena.

1. Abre `mutint.py` en el WebIDE y actualízalo con el siguiente código:

```python
# mutint.py

class MutInt:
    """
    A mutable integer class that allows its value to be modified after creation.
    """
    __slots__ = ['value']

    def __init__(self, value):
        """Initialize with an integer value."""
        self.value = value

    def __str__(self):
        """Return a string representation for printing."""
        return str(self.value)

    def __repr__(self):
        """Return a developer-friendly string representation."""
        return f'MutInt({self.value!r})'

    def __format__(self, fmt):
        """Support string formatting with format specifications."""
        return format(self.value, fmt)
```

Hemos agregado tres métodos importantes a la clase `MutInt`:

- `__str__()`: Este método se llama cuando se utiliza la función `str()` en el objeto o cuando se imprime el objeto directamente. Debe devolver una cadena legible por humanos.
- `__repr__()`: Este método proporciona la representación en cadena "oficial" del objeto. Se utiliza principalmente para depuración y, idealmente, debe devolver una cadena que, si se pasa a la función `eval()`, recrearía el objeto.
- `__format__()`: Este método permite utilizar el sistema de formato de cadenas de Python con los objetos `MutInt`. Puedes utilizar especificaciones de formato como relleno y formato numérico.

2. Crea un nuevo archivo de prueba llamado `test_string_repr.py` para probar estos nuevos métodos:

```python
# test_string_repr.py

from mutint import MutInt

# Create a MutInt object
a = MutInt(3)

# Test string representation
print(f"str(a): {str(a)}")
print(f"repr(a): {repr(a)}")

# Test direct printing
print(f"Print a: {a}")

# Test string formatting
print(f"Formatted with padding: '{a:*^10}'")
print(f"Formatted as decimal: '{a:d}'")

# Test mutability
a.value = 42
print(f"After changing value, repr(a): {repr(a)}")
```

En este archivo de prueba, primero importamos la clase `MutInt`. Luego creamos un objeto `MutInt` con el valor `3`. Probamos los métodos `__str__()` y `__repr__()` utilizando las funciones `str()` y `repr()`. También probamos la impresión directa, el formato de cadenas y la mutabilidad del objeto `MutInt`.

3. Ejecuta el script de prueba:

```bash
python3 /home/labex/project/test_string_repr.py
```

Cuando ejecutes este comando, Python ejecutará el script `test_string_repr.py`. Deberías ver una salida similar a esta:

```
str(a): 3
repr(a): MutInt(3)
Print a: 3
Formatted with padding: '****3*****'
Formatted as decimal: '3'
After changing value, repr(a): MutInt(42)
```

Ahora nuestros objetos `MutInt` se muestran correctamente. La representación en cadena muestra el valor subyacente y podemos utilizar el formato de cadenas al igual que con los enteros normales.

La diferencia entre `__str__()` y `__repr__()` es que `__str__()` está destinado a producir una salida amigable para el usuario, mientras que `__repr__()` debe, idealmente, producir una cadena que, cuando se pase a `eval()`, recrearía el objeto. Es por eso que incluimos el nombre de la clase en el método `__repr__()`.

El método `__format__()` permite que nuestro objeto funcione con el sistema de formato de Python, por lo que podemos utilizar especificaciones de formato como relleno y formato numérico.
