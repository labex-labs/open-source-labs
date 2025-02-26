# Ausführen von `unittest`

Um die Tests auszuführen, verwandeln Sie den Code in ein Skript.

```python
# test_simple.py

...

if __name__ == '__main__':
    unittest.main()
```

Dann führen Sie Python auf der Testdatei aus.

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
