# Utilisation de valeurs manquantes et de remplissage

Les arguments `missing_values` et `filling_values` sont utilisés pour gérer les données manquantes. L'argument `missing_values` est utilisé pour reconnaître les données manquantes, et l'argument `filling_values` est utilisé pour fournir une valeur pour les entrées manquantes.

```python
np.genfromtxt(StringIO(data), missing_values="N/A", filling_values=0)
```
