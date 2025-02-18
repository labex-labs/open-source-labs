# 空の辞書のテスト（エッジケース）

空の辞書のケースに特化したテストを追加しましょう。`test_key_of_max.py` の `TestKeyOfMax` クラスに以下のメソッドを追加します。

```python
    def test_empty_dictionary(self):
        self.assertIsNone(key_of_max({}))
```

- **`self.assertIsNone(...)`**: このアサーションは、値が具体的に `None` であるかどうかをチェックします。これは重要です。なぜなら、`self.assertEqual(..., None)` は `None` に _評価される_ ものに対して合格する可能性がありますが、実際に `None` ではない場合もあります。`assertIsNone` はより厳密です。

再度テストを実行します（`python3 test_key_of_max.py`）。3 つのテスト（2 つの基本テストと空の辞書のテスト）がすべて合格するはずです。

```python
python3 test_key_of_max.py
```

```plaintext
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```
