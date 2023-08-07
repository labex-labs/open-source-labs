# Preliminaries

In previous exercises, you created a file `stock.py` that contained
a `Stock` class. In a separate file, `teststock.py`, define the following
testing code:

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

Make sure you can run the file:

````bash
python3 teststock.py
.
------------------------------------------------------------------```
Ran 1 tests in 0.001s

OK

````
