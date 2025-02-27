# Obtenir les probabilités de classes pour le premier échantillon du jeu de données

Nous allons obtenir les probabilités de classes pour le premier échantillon du jeu de données et les stocker dans class1_1 et class2_1.

```python
class1_1 = [pr[0, 0] for pr in probas]
class2_1 = [pr[0, 1] for pr in probas]
```
