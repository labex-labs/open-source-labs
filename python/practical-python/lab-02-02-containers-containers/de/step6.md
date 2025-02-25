# Wörterbuchabfragen

Sie können die Existenz eines Schlüssels testen.

```python
if key in d:
    # JA
else:
    # NEIN
```

Sie können einen Wert abfragen, der möglicherweise nicht existiert, und einen Standardwert angeben, falls dies der Fall ist.

```python
name = d.get(key, default)
```

Ein Beispiel:

```python
>>> prices.get('IBM', 0.0)
93.37
>>> prices.get('SCOX', 0.0)
0.0
>>>
```
