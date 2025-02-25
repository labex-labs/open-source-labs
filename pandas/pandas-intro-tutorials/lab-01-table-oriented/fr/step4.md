# Effectuez des statistiques de base

Pandas fournit de nombreuses fonctionnalités pour effectuer des statistiques. Par exemple, vous pouvez trouver la valeur maximale d'une colonne en utilisant `max()`.

```python
# Finding the maximum age
df["Age"].max()
```

Vous pouvez également obtenir une vue d'ensemble rapide des données numériques d'un DataFrame en utilisant `describe()`.

```python
# Describing the numerical data
df.describe()
```
