# Módulo `unittest`

Suponha que você tenha algum código em `simple.py`.

```python
# simple.py

def add(x, y):
    return x + y
```

Agora, suponha que você queira testá-lo. Crie um arquivo de teste separado como este em `/home/labex/project/test_simple.py`.

```python
# test_simple.py

import simple
import unittest
```

Em seguida, defina uma classe de teste.

```python
# test_simple.py

import simple
import unittest

# Observe que ela herda de unittest.TestCase
class TestAdd(unittest.TestCase):
    ...
```

A classe de teste deve herdar de `unittest.TestCase`.

Na classe de teste, você define os métodos de teste.

```python
# test_simple.py

import simple
import unittest

# Observe que ela herda de unittest.TestCase
class TestAdd(unittest.TestCase):
    def test_simple(self):
        # Test with simple integer arguments
        r = simple.add(2, 2)
        self.assertEqual(r, 5)
    def test_str(self):
        # Test with strings
        r = simple.add('hello', 'world')
        self.assertEqual(r, 'helloworld')
```

\*Importante: Cada método deve começar com `test`.
