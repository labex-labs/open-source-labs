# `unittest` 모듈

`simple.py`에 코드가 있다고 가정해 보겠습니다.

```python
# simple.py

def add(x, y):
    return x + y
```

이제, 이를 테스트하고 싶다고 가정해 보겠습니다. `/home/labex/project/test_simple.py`와 같이 별도의 테스트 파일을 만듭니다.

```python
# test_simple.py

import simple
import unittest
```

그런 다음 테스트 클래스를 정의합니다.

```python
# test_simple.py

import simple
import unittest

# Notice that it inherits from unittest.TestCase
class TestAdd(unittest.TestCase):
    ...
```

테스트 클래스는 `unittest.TestCase`를 상속받아야 합니다.

테스트 클래스에서 테스트 메서드를 정의합니다.

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

\*중요: 각 메서드는 `test`로 시작해야 합니다.
