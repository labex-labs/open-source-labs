# Preliminares

En ejercicios anteriores, creaste un archivo `stock.py` que contenía una clase `Stock`. En un archivo separado, `teststock.py`, define el siguiente código de prueba:

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

Asegúrate de poder ejecutar el archivo:

````bash
python3 teststock.py
.
------------------------------------------------------------------```
Ejecutados 1 tests en 0.001s

OK
````
