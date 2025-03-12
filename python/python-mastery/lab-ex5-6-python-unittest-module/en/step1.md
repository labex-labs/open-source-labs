# Creating Your First Unit Test

Python's `unittest` module is a powerful tool that offers a structured way to organize and execute tests. Before we dive into writing our first unit test, let's understand some key concepts. Test fixtures are methods like `setUp` and `tearDown` that help prepare the environment before a test and clean it up afterward. Test cases are individual units of testing, test suites are collections of test cases, and test runners are responsible for executing these tests and presenting the results.

In this first step, we're going to create a basic test file for the `Stock` class, which is already defined in the `stock.py` file.

1. First, let's open the `stock.py` file. This will help us understand the `Stock` class we'll be testing. By looking at the code in `stock.py`, we can see how the class is structured, what attributes it has, and what methods it provides. To view the contents of the `stock.py` file, run the following command in your terminal:

```bash
cat stock.py
```

2. Now, it's time to create a new file named `teststock.py` using your preferred text editor. This file will contain our test cases for the `Stock` class. Here's the code you need to write in the `teststock.py` file:

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

Let's break down the key components of this code:

- `import unittest`: This line imports the `unittest` module, which provides the necessary tools and classes for writing and running tests in Python.
- `import stock`: This imports the module that contains our `Stock` class. Without this import, we wouldn't be able to access the `Stock` class in our test code.
- `class TestStock(unittest.TestCase)`: We create a new class named `TestStock` that inherits from `unittest.TestCase`. This makes our `TestStock` class a test case class, which can contain multiple test methods.
- `def test_create(self)`: This is a test method. In the `unittest` framework, all test methods must start with the prefix `test_`. This method creates an instance of the `Stock` class and then uses the `assertEqual` method to check if the attributes of the `Stock` instance match the expected values.
- `assertEqual`: This is a method provided by the `TestCase` class. It checks if two values are equal. If they are not equal, the test will fail.
- `unittest.main()`: When this script is executed directly, `unittest.main()` will run all the test methods in the `TestStock` class and display the results.

3. After writing the code in the `teststock.py` file, save it. Then, run the following command in your terminal to execute the test:

```bash
python3 teststock.py
```

You should see output similar to this:

```
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
```

The single dot (`.`) in the output indicates that one test has passed successfully. If a test fails, you'll see an `F` instead of the dot, along with detailed information about what went wrong in the test. This output helps you quickly identify if your code is working as expected or if there are any issues that need to be fixed.
