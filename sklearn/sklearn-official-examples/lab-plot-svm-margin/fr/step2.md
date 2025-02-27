# Générer des données

Nous générons 40 points séparables à l'aide de la fonction `random.randn` de numpy. Les 20 premiers points ont une moyenne de [-2, -2] et les 20 suivants ont une moyenne de [2, 2]. Nous attribuons ensuite une étiquette de classe 0 aux 20 premiers points et une étiquette de classe 1 aux 20 suivants.

```python
np.random.seed(0)
X = np.r_[np.random.randn(20, 2) - [2, 2], np.random.randn(20, 2) + [2, 2]]
Y = [0] * 20 + [1] * 20
```
