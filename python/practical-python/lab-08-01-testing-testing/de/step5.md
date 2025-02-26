# Verwendung von `unittest`

`unittest` bietet mehrere integrierte Assertionen. Jede von ihnen stellt etwas anderes fest.

```python
# Stellt sicher, dass expr True ist
self.assertTrue(expr)

# Stellt sicher, dass x == y
self.assertEqual(x,y)

# Stellt sicher, dass x!= y
self.assertNotEqual(x,y)

# Stellt sicher, dass x in der Nähe von y ist
self.assertAlmostEqual(x,y,places)

# Stellt sicher, dass die aufrufbare Funktion (callable) mit den Argumenten (arg1,arg2,...) eine Ausnahme vom Typ exc auslöst
self.assertRaises(exc, callable, arg1, arg2,...)
```

Dies ist keine erschöpfende Liste. Es gibt weitere Assertionen in diesem Modul.
