# Running `unittest`

To run the tests, turn the code into a script.

```python
# test_simple.py

...

if __name__ == '__main__':
    unittest.main()
```

Then run Python on the test file.

```bash
$ python3 test_simple.py
F.
========================================================
FAIL: test_simple (__main__.TestAdd)
--------------------------------------------------------
Traceback (most recent call last):
  File "testsimple.py", line 8, in test_simple
    self.assertEqual(r, 5)
AssertionError: 4 != 5
--------------------------------------------------------
Ran 2 tests in 0.000s
FAILED (failures=1)
```
