# `unittest` の実行

テストを実行するには、コードをスクリプトに変換します。

```python
# test_simple.py

...

if __name__ == '__main__':
    unittest.main()
```

そして、テストファイルで Python を実行します。

```bash
$ python3 test_simple.py
F.
========================================================
FAIL: test_simple (__main__.TestAdd)
--------------------------------------------------------
Traceback (most recent call last):
  File "testsimple.py", line 8, in test_simple
    self.assertEqual(r, 5)
AssertionError: 4!= 5
--------------------------------------------------------
Ran 2 tests in 0.000s
FAILED (failures=1)
```
