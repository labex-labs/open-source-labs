# Использование `unittest`

`unittest` предоставляет несколько встроенных утверждений. Каждое из них проверяет разные условия.

```python
# Проверить, что выражение expr истинно
self.assertTrue(expr)

# Проверить, что x равно y
self.assertEqual(x,y)

# Проверить, что x не равно y
self.assertNotEqual(x,y)

# Проверить, что x близко к y
self.assertAlmostEqual(x,y,places)

# Проверить, что вызов callable(arg1,arg2,...) вызывает исключение exc
self.assertRaises(exc, callable, arg1, arg2,...)
```

Это не исчерпывающий список. В модуле есть и другие утверждения.
