# Vorbedingungen

In früheren Übungen haben Sie eine Datei `stock.py` erstellt, die eine `Stock`-Klasse enthielt. In einer separaten Datei `teststock.py` definieren Sie den folgenden Testcode:

```python
# teststock.py

import unittest
import stock

class TestStock(unittest.TestCase):
    def test_create(self):
        s = stock.Stock('GOOG', 100, 490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

if __name__ == '__main__':
    unittest.main()
```

Stellen Sie sicher, dass Sie die Datei ausführen können:

````bash
python3 teststock.py
.
------------------------------------------------------------------```
Durchlaufen 1 Test in 0,001s

OK
````
