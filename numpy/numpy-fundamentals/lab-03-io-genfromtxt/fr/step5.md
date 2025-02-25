# Définition du type de données

L'argument `dtype` est utilisé pour contrôler la conversion des chaînes de caractères en d'autres types. Cela peut être un seul type, une séquence de types, une chaîne de caractères séparée par des virgules, un dictionnaire, une séquence de tuples, un objet `numpy.dtype` existant ou `None` pour déterminer le type à partir des données elles-mêmes.

```python
np.genfromtxt(StringIO(data), dtype=float)
```
