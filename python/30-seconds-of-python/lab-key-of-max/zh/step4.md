# 测试空字典（边界情况）

让我们专门为空字典的情况添加一个测试。在 `test_key_of_max.py` 的 `TestKeyOfMax` 类中添加以下方法：

```python
    def test_empty_dictionary(self):
        self.assertIsNone(key_of_max({}))
```

- **`self.assertIsNone(...)`**：这个断言用于检查值是否确切为 `None`。这很重要，因为 `self.assertEqual(..., None)` 可能会对那些 _求值结果_ 为 `None` 但实际上并非 `None` 的情况判定为通过。`assertIsNone` 更为严格。

再次运行测试（`python3 test_key_of_max.py`）。现在，所有三个测试（两个基础测试和空字典测试）都应该通过。

```python
python3 test_key_of_max.py
```

```plaintext
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```
