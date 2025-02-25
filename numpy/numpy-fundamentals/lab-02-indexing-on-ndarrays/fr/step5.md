# Accès aux champs

Si l'objet ndarray est un tableau structuré, les champs du tableau peuvent être accédés en indexant le tableau avec des chaînes de caractères, de manière similaire à un dictionnaire.

```python
x = np.array([(1, 2), (3, 4), (5, 6)], dtype=[('a', np.int32), ('b', np.int32)])
print(x['a'])  # Sortie : [1, 3, 5]
```
