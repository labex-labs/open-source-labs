# Entfernen von Elementen aus Listen

Sie können Elemente entweder nach Elementwert oder nach Index entfernen:

```python
# Mit dem Wert
names.remove('Curtis')

# Mit dem Index
del names[1]
```

Beim Entfernen eines Elements wird kein Loch erzeugt. Andere Elemente werden nach unten verschoben, um den freigelegten Platz zu füllen. Wenn das Element mehrfach vorkommt, entfernt `remove()` nur das erste Vorkommen.
