# `unittest` 사용하기

`unittest`에는 여러 가지 내장 어서션 (assertion) 이 있습니다. 각각은 서로 다른 것을 어서션합니다.

```python
# Assert that expr is True
self.assertTrue(expr)

# Assert that x == y
self.assertEqual(x,y)

# Assert that x != y
self.assertNotEqual(x,y)

# Assert that x is near y
self.assertAlmostEqual(x,y,places)

# Assert that callable(arg1,arg2,...) raises exc
self.assertRaises(exc, callable, arg1, arg2, ...)
```

이것은 완전한 목록이 아닙니다. 모듈에는 다른 어서션도 있습니다.
