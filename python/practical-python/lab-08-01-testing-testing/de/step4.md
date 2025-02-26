# `unittest`-Modul

Angenommen, Sie haben einige Code in `simple.py`.

```python
# simple.py

def add(x, y):
    return x + y
```

Nun möchten Sie ihn testen. Erstellen Sie eine separate Testdatei wie folgt in `/home/labex/project/test_simple.py`.

```python
# test_simple.py

import simple
import unittest
```

Dann definieren Sie eine Testklasse.

```python
# test_simple.py

import simple
import unittest

# Beachten Sie, dass sie von unittest.TestCase erbt
class TestAdd(unittest.TestCase):
  ...
```

Die Testklasse muss von `unittest.TestCase` erben.

In der Testklasse definieren Sie die Testmethoden.

```python
# test_simple.py

import simple
import unittest

# Beachten Sie, dass sie von unittest.TestCase erbt
class TestAdd(unittest.TestCase):
    def test_simple(self):
        # Testen Sie mit einfachen ganzzahligen Argumenten
        r = simple.add(2, 2)
        self.assertEqual(r, 5)
    def test_str(self):
        # Testen Sie mit Zeichenketten
        r = simple.add('hello', 'world')
        self.assertEqual(r, 'helloworld')
```

\*Wichtig: Jede Methode muss mit `test` beginnen.
