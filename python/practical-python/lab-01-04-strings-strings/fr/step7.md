# Immutabilité des chaînes de caractères

Les chaînes de caractères sont "immuables" ou en lecture seule. Une fois créées, leur valeur ne peut pas être modifiée.

```python
>>> s = 'Hello World'
>>> s[1] = 'a'
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError:'str' object does not support item assignment
>>>
```

**Toutes les opérations et méthodes qui manipulent les données de chaîne de caractères créent toujours de nouvelles chaînes de caractères.**
