# Insérer des données manquantes

Ici, nous allons voir comment insérer des valeurs manquantes dans nos données.

```python
# Insérer des valeurs manquantes
s = pd.Series([1., 2., 3.])
s.loc[0] = None
```
