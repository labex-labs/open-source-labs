# Módulo `unittest`

Supongamos que tienes un código en `simple.py`.

```python
# simple.py

def add(x, y):
    return x + y
```

Ahora, supongamos que quieres probarlo. Crea un archivo de prueba separado como este en `/home/labex/project/test_simple.py`.

```python
# test_simple.py

import simple
import unittest
```

Luego, define una clase de prueba.

```python
# test_simple.py

import simple
import unittest

# Observa que hereda de unittest.TestCase
class TestAdd(unittest.TestCase):
 ...
```

La clase de prueba debe heredar de `unittest.TestCase`.

En la clase de prueba, defines los métodos de prueba.

```python
# test_simple.py

import simple
import unittest

# Observa que hereda de unittest.TestCase
class TestAdd(unittest.TestCase):
    def test_simple(self):
        # Prueba con argumentos enteros simples
        r = simple.add(2, 2)
        self.assertEqual(r, 5)
    def test_str(self):
        # Prueba con cadenas
        r = simple.add('hello', 'world')
        self.assertEqual(r, 'helloworld')
```

\*Importante: Cada método debe comenzar con `test`.
