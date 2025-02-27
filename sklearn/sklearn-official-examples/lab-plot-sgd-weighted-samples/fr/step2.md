# Création d'un ensemble de données pondéré

Nous créons un ensemble de données pondéré à l'aide de la bibliothèque numpy. Nous générons 20 points avec des valeurs aléatoires et attribuons un poids plus élevé aux 10 derniers échantillons.

```python
np.random.seed(0)
X = np.r_[np.random.randn(10, 2) + [1, 1], np.random.randn(10, 2)]
y = [1] * 10 + [-1] * 10
sample_weight = 100 * np.abs(np.random.randn(20))
sample_weight[:10] *= 10
```
