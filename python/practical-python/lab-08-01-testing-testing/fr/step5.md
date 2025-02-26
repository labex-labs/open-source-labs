# Utilisation de `unittest`

Il existe plusieurs assertions intégrées dans `unittest`. Chacune d'entre elles affirme une chose différente.

```python
# Affirmer que expr est vraie
self.assertTrue(expr)

# Affirmer que x == y
self.assertEqual(x,y)

# Affirmer que x!= y
self.assertNotEqual(x,y)

# Affirmer que x est proche de y
self.assertAlmostEqual(x,y,places)

# Affirmer que callable(arg1,arg2,...) lève exc
self.assertRaises(exc, callable, arg1, arg2,...)
```

Ce n'est pas une liste exhaustive. Il y a d'autres assertions dans le module.
