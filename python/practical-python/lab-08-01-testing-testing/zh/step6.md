# 运行 `unittest`

要运行测试，需将代码转换为脚本。

```python
# test_simple.py

...

if __name__ == '__main__':
    unittest.main()
```

然后在测试文件上运行 Python。

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
