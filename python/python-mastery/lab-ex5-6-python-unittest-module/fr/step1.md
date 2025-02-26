# Préliminaires

Dans les exercices précédents, vous avez créé un fichier `stock.py` qui contenait une classe `Stock`. Dans un fichier séparé, `teststock.py`, définissez le code de test suivant :

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

Vérifiez que vous pouvez exécuter le fichier :

````bash
python3 teststock.py
.
------------------------------------------------------------------```
Exécuté 1 test en 0,001s

OK
````
