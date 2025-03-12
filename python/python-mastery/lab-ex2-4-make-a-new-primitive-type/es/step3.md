# Añadiendo operaciones matemáticas

Actualmente, nuestra clase `MutInt` no admite operaciones matemáticas como la suma. En Python, para habilitar tales operaciones en una clase personalizada, necesitamos implementar métodos especiales. Estos métodos especiales también se conocen como "métodos mágicos" o "métodos dunder" porque están rodeados de dos guiones bajos. Vamos a agregar la funcionalidad de suma implementando los métodos especiales relevantes para las operaciones aritméticas.

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
        # For commutative operations like +, we can reuse __add__
        return self.__add__(other)

    def __iadd__(self, other):
        """Handle in-place addition: self += other."""
        if isinstance(other, MutInt):
            self.value += other.value
            return self
        elif isinstance(other, int):
            self.value += other
            return self
        else:
            return NotImplemented
```

Hemos agregado tres nuevos métodos a la clase `MutInt`:

- `__add__()`: Este método se llama cuando se utiliza el operador `+` con nuestro objeto `MutInt` en el lado izquierdo. Dentro de este método, primero comprobamos si el operando `other` es una instancia de `MutInt` o un `int`. Si es así, realizamos la suma y devolvemos un nuevo objeto `MutInt` con el resultado. Si el operando `other` es algo diferente, devolvemos `NotImplemented`. Esto le dice a Python que intente otros métodos o levante un `TypeError`.
- `__radd__()`: Este método se llama cuando se utiliza el operador `+` con nuestro objeto `MutInt` en el lado derecho. Dado que la suma es una operación conmutativa (es decir, `a + b` es lo mismo que `b + a`), podemos simplemente reutilizar el método `__add__`.
- `__iadd__()`: Este método se llama cuando se utiliza el operador `+=` en nuestro objeto `MutInt`. En lugar de crear un nuevo objeto, modifica el objeto `MutInt` existente y lo devuelve.

2. Crea un nuevo archivo de prueba llamado `test_math_ops.py` para probar estos nuevos métodos:

```python
# test_math_ops.py

from mutint import MutInt

# Create MutInt objects
a = MutInt(3)
b = MutInt(5)

# Test regular addition
c = a + b
print(f"a + b = {c}")

# Test addition with int
d = a + 10
print(f"a + 10 = {d}")

# Test reversed addition
e = 7 + a
print(f"7 + a = {e}")

# Test in-place addition
print(f"Before a += 5: a = {a}")
a += 5
print(f"After a += 5: a = {a}")

# Test in-place addition with reference sharing
f = a  # f and a point to the same object
print(f"Before a += 10: a = {a}, f = {f}")
a += 10
print(f"After a += 10: a = {a}, f = {f}")

# Test unsupported operation
try:
    result = a + 3.5  # Adding a float is not supported
    print(f"a + 3.5 = {result}")
except TypeError as e:
    print(f"Error when adding float: {e}")
```

En este archivo de prueba, primero importamos la clase `MutInt`. Luego creamos algunos objetos `MutInt` y realizamos diferentes tipos de operaciones de suma. También probamos la suma in-place y el caso en el que se intenta una operación no admitida (sumar un número de punto flotante).

3. Ejecuta el script de prueba:

```bash
python3 /home/labex/project/test_math_ops.py
```

Deberías ver una salida similar a esta:

```
a + b = MutInt(8)
a + 10 = MutInt(13)
7 + a = MutInt(10)
Before a += 5: a = MutInt(3)
After a += 5: a = MutInt(8)
Before a += 10: a = MutInt(8), f = MutInt(8)
After a += 10: a = MutInt(18), f = MutInt(18)
Error when adding float: unsupported operand type(s) for +: 'MutInt' and 'float'
```

Ahora nuestra clase `MutInt` admite operaciones de suma básicas. Observa que cuando usamos `+=`, tanto `a` como `f` se actualizaron. Esto muestra que `a += 10` modificó el objeto existente en lugar de crear uno nuevo.

Este comportamiento con objetos mutables es similar al de los tipos mutables integrados de Python, como las listas. Por ejemplo:

```python
a = [1, 2, 3]
b = a
a += [4, 5]  # Both a and b are updated
```

En contraste, para tipos inmutables como las tuplas, `+=` crea un nuevo objeto:

```python
c = (1, 2, 3)
d = c
c += (4, 5)  # c is a new object, d still points to the old one
```
