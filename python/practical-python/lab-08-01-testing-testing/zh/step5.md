# 使用 `unittest`

`unittest` 提供了几个内置断言。每个断言都用于验证不同的情况。

```python
# 断言表达式 expr 为真
self.assertTrue(expr)

# 断言 x 等于 y
self.assertEqual(x,y)

# 断言 x 不等于 y
self.assertNotEqual(x,y)

# 断言 x 近似等于 y
self.assertAlmostEqual(x,y,places)

# 断言可调用对象 callable(arg1,arg2,...) 引发异常 exc
self.assertRaises(exc, callable, arg1, arg2,...)
```

这并非完整列表。该模块中还有其他断言。
