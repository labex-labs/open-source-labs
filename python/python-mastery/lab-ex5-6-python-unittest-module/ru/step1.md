# Предварительные условия

В предыдущих упражнениях вы создали файл `stock.py`, содержащий класс `Stock`. В отдельном файле `teststock.py` определите следующий тестовый код:

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

Убедитесь, что вы можете запустить файл:

````bash
python3 teststock.py
.
------------------------------------------------------------------```
Ran 1 tests in 0.001s

OK
````
