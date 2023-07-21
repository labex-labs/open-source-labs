# Using `unittest`

There are several built in assertions that come with `unittest`. Each of them asserts a different thing.

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

This is not an exhaustive list. There are other assertions in the
module.
