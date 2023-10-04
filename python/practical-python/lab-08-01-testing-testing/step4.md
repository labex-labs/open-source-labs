# `unittest` Module

Suppose you have some code in `/home/labex/project/test_simple.py`

```python
# test_simple.py

def add(x, y):
    return x + y
```

Now, suppose you want to test it. Create a separate testing file like this.

```python
# test_simple.py

import simple
import unittest
```

Then define a testing class.

```python
# test_simple.py

import simple
import unittest

# Notice that it inherits from unittest.TestCase
class TestAdd(unittest.TestCase):
    ...
```

The testing class must inherit from `unittest.TestCase`.

In the testing class, you define the testing methods.

```python
# test_simple.py

import simple
import unittest

# Notice that it inherits from unittest.TestCase
class TestAdd(unittest.TestCase):
    def test_simple(self):
        # Test with simple integer arguments
        r = simple.add(2, 2)
        self.assertEqual(r, 5)
    def test_str(self):
        # Test with strings
        r = simple.add('hello', 'world')
        self.assertEqual(r, 'helloworld')
```

\*Important: Each method must start with `test`.
