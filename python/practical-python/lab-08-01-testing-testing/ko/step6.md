# `unittest` 실행하기

테스트를 실행하려면 코드를 스크립트로 만듭니다.

```python
# test_simple.py

...

if __name__ == '__main__':
    unittest.main()
```

그런 다음 테스트 파일에서 Python 을 실행합니다.

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
