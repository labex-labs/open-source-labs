# Creating Your First Unit Test

Python's `unittest` module provides a framework for organizing tests. It is built on the concept of test fixtures (setUp and tearDown methods), test cases, test suites, and test runners.

In this first step, you will create a basic test file for the `Stock` class which already exists in the `stock.py` file.

1. First, let's open the `stock.py` file to understand the class we'll be testing:

```bash
cat stock.py
```

2. Now, create a new file named `teststock.py` using the editor:

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

Let's understand the key components of this code:

- `import unittest`: Imports the unittest module
- `import stock`: Imports the module containing our `Stock` class
- `class TestStock(unittest.TestCase)`: Creates a test case class by inheriting from `unittest.TestCase`
- `def test_create(self)`: A test method - all test methods must start with `test_`
- `assertEqual`: A method provided by TestCase to check if two values are equal
- `unittest.main()`: Runs all tests when this script is executed

3. Save the file and run it to execute the test:

```bash
python3 teststock.py
```

You should see output similar to:

```
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
```

The `.` indicates a passing test. If a test fails, you would see an `F` instead, along with details about the failure.
