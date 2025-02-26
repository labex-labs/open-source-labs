# Usando `unittest`

Hay varias aserciones incorporadas que vienen con `unittest`. Cada una de ellas afirma algo diferente.

```python
# Asegura que expr sea True
self.assertTrue(expr)

# Asegura que x == y
self.assertEqual(x,y)

# Asegura que x!= y
self.assertNotEqual(x,y)

# Asegura que x sea cercano a y
self.assertAlmostEqual(x,y,places)

# Asegura que callable(arg1,arg2,...) lance exc
self.assertRaises(exc, callable, arg1, arg2,...)
```

Esta no es una lista exhaustiva. Hay otras aserciones en el módulo.
