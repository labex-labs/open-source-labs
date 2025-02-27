# Charger les données

Tout d'abord, nous allons charger l'ensemble de données du diabète.

```python
diabetes = datasets.load_diabetes()
X, y = diabetes.data, diabetes.target
```
