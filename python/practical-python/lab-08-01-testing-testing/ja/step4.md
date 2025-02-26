# `unittest` モジュール

`simple.py` にいくつかのコードがあるとしましょう。

```python
# simple.py

def add(x, y):
    return x + y
```

次に、それをテストしたいとします。`/home/labex/project/test_simple.py` にこのような別のテストファイルを作成します。

```python
# test_simple.py

import simple
import unittest
```

そして、テストクラスを定義します。

```python
# test_simple.py

import simple
import unittest

# 注意：unittest.TestCase から継承しています
class TestAdd(unittest.TestCase):
  ...
```

テストクラスは `unittest.TestCase` から継承する必要があります。

テストクラスの中で、テストメソッドを定義します。

```python
# test_simple.py

import simple
import unittest

# 注意：unittest.TestCase から継承しています
class TestAdd(unittest.TestCase):
    def test_simple(self):
        # 単純な整数引数でテスト
        r = simple.add(2, 2)
        self.assertEqual(r, 5)
    def test_str(self):
        # 文字列を使ったテスト
        r = simple.add('hello', 'world')
        self.assertEqual(r, 'helloworld')
```

\*重要：各メソッドは `test` で始める必要があります。
