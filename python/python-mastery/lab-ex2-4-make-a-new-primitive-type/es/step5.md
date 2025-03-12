# Añadiendo conversiones de tipos

Nuestra clase `MutInt` actualmente admite operaciones de suma y comparación. Sin embargo, no funciona con las funciones de conversión integradas de Python, como `int()` y `float()`. Estas funciones de conversión son muy útiles en Python. Por ejemplo, cuando se desea convertir un valor a un entero o a un número de punto flotante para diferentes cálculos u operaciones, se dependen de estas funciones. Entonces, agreguemos a nuestra clase `MutInt` la capacidad de trabajar con ellas.

1. Abre `mutint.py` en el WebIDE y actualízalo con el siguiente código:

```python
# mutint.py

from functools import total_ordering

@total_ordering
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
        """Return a developer - friendly string representation."""
        return f'MutInt({self.value!r})'

    def __format__(self, fmt):
        """Support string formatting with format specifications."""
        return format(self.value, fmt)

    def __add__(self, other):
        """Handle addition: self + other."""
        if isinstance(other, MutInt):
            return MutInt(self.value + other.value)
        elif isinstance(other, int):
            return MutInt(self.value + other)
        else:
            return NotImplemented

    def __radd__(self, other):
        """Handle reversed addition: other + self."""
        return self.__add__(other)

    def __iadd__(self, other):
        """Handle in - place addition: self += other."""
        if isinstance(other, MutInt):
            self.value += other.value
            return self
        elif isinstance(other, int):
            self.value += other
            return self
        else:
            return NotImplemented

    def __eq__(self, other):
        """Handle equality comparison: self == other."""
        if isinstance(other, MutInt):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        else:
            return NotImplemented

    def __lt__(self, other):
        """Handle less - than comparison: self < other."""
        if isinstance(other, MutInt):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        else:
            return NotImplemented

    def __int__(self):
        """Convert to int."""
        return self.value

    def __float__(self):
        """Convert to float."""
        return float(self.value)

    __index__ = __int__  # Support array indexing and other operations requiring an index
```

Hemos agregado tres nuevos métodos a la clase `MutInt`:

1. `__int__()`: Este método se llama cuando se utiliza la función `int()` en un objeto de nuestra clase `MutInt`. Por ejemplo, si se tiene un objeto `MutInt` llamado `a`, y se escribe `int(a)`, Python llamará al método `__int__()` del objeto `a`.
2. `__float__()`: De manera similar, este método se llama cuando se utiliza la función `float()` en nuestro objeto `MutInt`.
3. `__index__()`: Este método se utiliza para operaciones que específicamente requieren un índice entero. Por ejemplo, cuando se desea acceder a un elemento en una lista utilizando un índice, o realizar operaciones de longitud de bits, Python necesita un índice entero.

El método `__index__` es crucial para operaciones que requieren un índice entero, como la indexación de listas, el corte (slicing) y las operaciones de longitud de bits. En nuestra implementación simple, lo configuramos para que sea el mismo que `__int__` porque el valor de nuestro objeto `MutInt` se puede utilizar directamente como un índice entero.

2. Crea un nuevo archivo de prueba llamado `test_conversions.py` para probar estos nuevos métodos:

```python
# test_conversions.py

from mutint import MutInt

# Create a MutInt object
a = MutInt(3)

# Test conversions
print(f"int(a): {int(a)}")
print(f"float(a): {float(a)}")

# Test using as an index
names = ['Dave', 'Guido', 'Paula', 'Thomas', 'Lewis']
print(f"names[a]: {names[a]}")

# Test using in bit operations (requires __index__)
print(f"1 << a: {1 << a}")  # Shift left by 3

# Test hex/oct/bin functions (requires __index__)
print(f"hex(a): {hex(a)}")
print(f"oct(a): {oct(a)}")
print(f"bin(a): {bin(a)}")

# Modify and test again
a.value = 5
print(f"\nAfter changing value to 5:")
print(f"int(a): {int(a)}")
print(f"names[a]: {names[a]}")
```

3. Ejecuta el script de prueba:

```bash
python3 /home/labex/project/test_conversions.py
```

Deberías ver una salida similar a esta:

```
int(a): 3
float(a): 3.0
names[a]: Paula
1 << a: 8
hex(a): 0x3
oct(a): 0o3
bin(a): 0b11

After changing value to 5:
int(a): 5
names[a]: Lewis
```

Ahora nuestra clase `MutInt` se puede convertir a tipos estándar de Python y utilizarse en operaciones que requieren un índice entero.

El método `__index__` es particularmente importante. Fue introducido en Python para permitir que los objetos se utilicen en situaciones donde se requiere un índice entero, como la indexación de listas, las operaciones bit a bit y varias funciones como `hex()`, `oct()` y `bin()`.

Con estas adiciones, nuestra clase `MutInt` es ahora un tipo primitivo bastante completo. Se puede utilizar en la mayoría de los contextos donde se utilizaría un entero normal, con el beneficio adicional de ser mutable.

## Implementación completa de MutInt

Aquí está nuestra implementación completa de `MutInt` con todas las características que hemos agregado:

```python
# mutint.py

from functools import total_ordering

@total_ordering
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
        """Return a developer - friendly string representation."""
        return f'MutInt({self.value!r})'

    def __format__(self, fmt):
        """Support string formatting with format specifications."""
        return format(self.value, fmt)

    def __add__(self, other):
        """Handle addition: self + other."""
        if isinstance(other, MutInt):
            return MutInt(self.value + other.value)
        elif isinstance(other, int):
            return MutInt(self.value + other)
        else:
            return NotImplemented

    def __radd__(self, other):
        """Handle reversed addition: other + self."""
        return self.__add__(other)

    def __iadd__(self, other):
        """Handle in - place addition: self += other."""
        if isinstance(other, MutInt):
            self.value += other.value
            return self
        elif isinstance(other, int):
            self.value += other
            return self
        else:
            return NotImplemented

    def __eq__(self, other):
        """Handle equality comparison: self == other."""
        if isinstance(other, MutInt):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        else:
            return NotImplemented

    def __lt__(self, other):
        """Handle less - than comparison: self < other."""
        if isinstance(other, MutInt):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        else:
            return NotImplemented

    def __int__(self):
        """Convert to int."""
        return self.value

    def __float__(self):
        """Convert to float."""
        return float(self.value)

    __index__ = __int__  # Support array indexing and other operations requiring an index
```

Esta implementación cubre los aspectos clave de la creación de un nuevo tipo primitivo en Python. Para hacerlo aún más completo, se podrían implementar métodos adicionales para otras operaciones como la resta, la multiplicación, la división, etc.
