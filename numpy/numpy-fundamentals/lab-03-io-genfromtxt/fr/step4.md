# Sélection des colonnes

L'argument `usecols` est utilisé pour sélectionner les colonnes à importer. Il accepte un seul entier ou une séquence d'entiers correspondant aux indices des colonnes à importer.

```python
np.genfromtxt(StringIO(data), usecols=(0, -1))
```
