# Testing the Empty Dictionary (Edge Case)

Let's add a test specifically for the empty dictionary case. Add this method to your `TestKeyOfMax` class in `test_key_of_max.py`:

```python
    def test_empty_dictionary(self):
        self.assertIsNone(key_of_max({}))
```

- **`self.assertIsNone(...)`**: This assertion checks if the value is specifically `None`. This is important because `self.assertEqual(..., None)` could pass for things that _evaluate_ to `None`, but aren't actually `None`. `assertIsNone` is more strict.

Run the tests again (`python3 test_key_of_max.py`). All three tests (the two basic tests and the empty dictionary test) should now pass.
