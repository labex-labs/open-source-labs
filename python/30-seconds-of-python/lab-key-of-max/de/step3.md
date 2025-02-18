# Erstellen von Unittests: Grundlegende Tests

Jetzt schreiben wir einige Tests, um sicherzustellen, dass unsere Funktion korrekt funktioniert. Wir verwenden das `unittest`-Modul von Python. Erstellen Sie eine neue Datei mit dem Namen `test_key_of_max.py` und fügen Sie den folgenden Code hinzu:

```python
import unittest
from key_of_max import key_of_max  # Import our function

class TestKeyOfMax(unittest.TestCase):

    def test_basic_case(self):
        self.assertEqual(key_of_max({'a': 4, 'b': 0, 'c': 13}), 'c')

    def test_another_case(self):
        self.assertEqual(key_of_max({'apple': 10, 'banana': 5, 'orange': 10}), 'apple')

if __name__ == '__main__':
    unittest.main()
```

Erklärung:

1.  **`import unittest`**: Importiert das Testframework.
2.  **`from key_of_max import key_of_max`**: Importiert die Funktion, die wir testen möchten.
3.  **`class TestKeyOfMax(unittest.TestCase):`**: Definiert eine _Testklasse_. Testklassen gruppieren verwandte Tests zusammen.
4.  **`def test_basic_case(self):`**: Definiert eine _Testmethode_. Jede Testmethode überprüft einen bestimmten Aspekt unserer Funktion. Die Namen von Testmethoden _müssen_ mit `test_` beginnen.
5.  **`self.assertEqual(...)`**: Dies ist eine _Behauptung_ (assertion). Sie prüft, ob zwei Werte gleich sind. Wenn sie nicht gleich sind, schlägt der Test fehl. In diesem Fall überprüfen wir, ob `key_of_max({'a': 4, 'b': 0, 'c': 13})` `'c'` zurückgibt, was es tun sollte.
6.  **`def test_another_case(self):`**: Fügt einen weiteren Testfall hinzu, um den Schlüssel des maximalen Werts zu überprüfen, der möglicherweise nicht eindeutig ist.
7.  **`if __name__ == '__main__': unittest.main()`**: Diese Standard-Idiomatik in Python führt die Tests aus, wenn Sie das Skript direkt ausführen (z.B. `python3 test_key_of_max.py`).

Führen Sie die Tests in Ihrem Terminal aus: `python3 test_key_of_max.py`. Sie sollten eine Ausgabe sehen, die anzeigt, dass die beiden Tests bestanden wurden.

```python
python3 test_key_of_max.py
```

```plaintext
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```
