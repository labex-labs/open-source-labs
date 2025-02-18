# すべての値が負の場合のテスト

最後のテストとして、辞書内のすべての値が負の場合を扱いましょう。`TestKeyOfMax` に以下のメソッドを追加します。

```python
    def test_all_negative_values(self):
        self.assertEqual(key_of_max({'x': -5, 'y': -2, 'z': -10}), 'y')
```

このテストは、関数が「最も負の値が小さい」（この場合の最大値）を正しく識別し、それに関連付けられたキーを返すことを保証します。

最後に一度テストを実行しましょう（`python3 test_key_of_max.py`）。4 つのテストすべてが合格するはずです。これにより、関数が正しく動作していることを高い確信を持って確認できます。

完成した `test_key_of_max.py` は以下のようになるはずです。

```python
import unittest
from key_of_max import key_of_max

class TestKeyOfMax(unittest.TestCase):

    def test_basic_case(self):
        self.assertEqual(key_of_max({'a': 4, 'b': 0, 'c': 13}), 'c')

    def test_another_case(self):
        self.assertEqual(key_of_max({'apple': 10, 'banana': 5, 'orange': 10}), 'apple')

    def test_empty_dictionary(self):
        self.assertIsNone(key_of_max({}))

    def test_all_negative_values(self):
        self.assertEqual(key_of_max({'x': -5, 'y': -2, 'z': -10}), 'y')

if __name__ == '__main__':
    unittest.main()
```

再度テストを実行します（`python3 test_key_of_max.py`）。4 つのテストすべてが合格するはずです。これにより、関数が正しく動作していることを高い確信を持って確認できます。

```python
python3 test_key_of_max.py
```

```plaintext
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```
