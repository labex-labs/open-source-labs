# Testen mit ausschließlich negativen Werten

Als letzten Test behandeln wir den Fall, in dem alle Werte im Wörterbuch negativ sind. Fügen Sie diese Methode zu `TestKeyOfMax` hinzu:

```python
    def test_all_negative_values(self):
        self.assertEqual(key_of_max({'x': -5, 'y': -2, 'z': -10}), 'y')
```

Dieser Test stellt sicher, dass unsere Funktion den _wenigsten negativen_ Wert (der in diesem Fall der maximale Wert ist) korrekt erkennt und den zugehörigen Schlüssel zurückgibt.

Führen Sie die Tests ein letztes Mal aus (`python3 test_key_of_max.py`). Alle vier Tests sollten bestanden werden. Dies gibt uns ein hohes Maß an Vertrauen, dass unsere Funktion korrekt funktioniert.

Ihre vollständige `test_key_of_max.py`-Datei sollte jetzt wie folgt aussehen:

```python
import unittest
from key_of_max import key_of_max

class TestKeyOfMax(unittest.TestCase):

    def test_basic_case(self):
        self.assertEqual(key_of_max({'a': 4, 'b': 0, 'c': 13}), 'c')

    def test_another_case(self):
        self.assertEqual(key_of_max({'apple': 10, 'banana': 5, 'orange': 10}), 'apple')

    def test_empty_dictionary(self):
        self.assertIsNone(key_of_max({}))

    def test_all_negative_values(self):
        self.assertEqual(key_of_max({'x': -5, 'y': -2, 'z': -10}), 'y')

if __name__ == '__main__':
    unittest.main()
```

Führen Sie die Tests erneut aus (`python3 test_key_of_max.py`). Alle vier Tests sollten bestanden werden. Dies gibt uns ein hohes Maß an Vertrauen, dass unsere Funktion korrekt funktioniert.

```python
python3 test_key_of_max.py
```

```plaintext
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```
