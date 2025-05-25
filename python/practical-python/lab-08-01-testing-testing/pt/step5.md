# Usando `unittest`

Existem várias asserções (assertions) embutidas que vêm com `unittest`. Cada uma delas afirma uma coisa diferente.

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

Esta não é uma lista exaustiva. Existem outras asserções no módulo.
