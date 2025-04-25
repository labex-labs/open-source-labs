# 単体テストの作成：基本的なテスト

では、関数が正しく動作することを確認するためにいくつかのテストを書きましょう。Python の `unittest` モジュールを使用します。`test_key_of_max.py` という名前の新しいファイルを作成し、以下のコードを追加します。

```python
import unittest
from key_of_max import key_of_max  # Import our function

class TestKeyOfMax(unittest.TestCase):

    def test_basic_case(self):
        self.assertEqual(key_of_max({'a': 4, 'b': 0, 'c': 13}), 'c')

    def test_another_case(self):
        self.assertEqual(key_of_max({'apple': 10, 'banana': 5, 'orange': 10}), 'apple')

if __name__ == '__main__':
    unittest.main()
```

説明：

1.  **`import unittest`**: テストフレームワークをインポートします。
2.  **`from key_of_max import key_of_max`**: テスト対象の関数をインポートします。
3.  **`class TestKeyOfMax(unittest.TestCase):`**: _テストクラス_ を定義します。テストクラスは関連するテストをまとめます。
4.  **`def test_basic_case(self):`**: _テストメソッド_ を定義します。各テストメソッドは関数の特定の側面をチェックします。テストメソッド名は必ず `test_` で始める必要があります。
5.  **`self.assertEqual(...)`**: これは _アサーション_ です。2 つの値が等しいかどうかをチェックします。等しくない場合、テストは失敗します。この場合、`key_of_max({'a': 4, 'b': 0, 'c': 13})` が `'c'` を返すかどうかをチェックしています。
6.  **`def test_another_case(self):`**: 最大値のキーが一意でない場合を検証するための別のテストケースを追加しました。
7.  **`if __name__ == '__main__': unittest.main()`**: この標準的な Python の慣用句は、スクリプトを直接実行するときにテストを実行します（例：`python3 test_key_of_max.py`）。

ターミナルからテストを実行します：`python3 test_key_of_max.py`。2 つのテストが合格したことを示す出力が表示されるはずです。

```python
python3 test_key_of_max.py
```

```plaintext
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```
