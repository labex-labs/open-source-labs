# In Liste umwandeln

Schreiben Sie eine Funktion `cast_list(val)`, die einen Wert als Argument nimmt und ihn als Liste zurückgibt. Wenn der Wert bereits eine Liste ist, geben Sie ihn unverändert zurück. Wenn der Wert keine Liste ist, aber iterierbar ist, geben Sie ihn als Liste zurück. Wenn der Wert nicht iterierbar ist, geben Sie ihn als Liste mit einem einzelnen Element zurück.

```python
def cast_list(val):
  return list(val) if isinstance(val, (tuple, list, set, dict)) else [val]
```

```python
cast_list('foo') # ['foo']
cast_list([1]) # [1]
cast_list(('foo', 'bar')) # ['foo', 'bar']
```
