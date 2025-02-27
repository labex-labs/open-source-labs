# Moindres carrés ordinaires

> Commencez avec [Supervised Learning: Regression](https://labex.io/courses/supervised-learning-regression), si vous n'avez pas d'expérience antérieure en apprentissage automatique.

Les moindres carrés ordinaires (OLS) est une méthode de régression linéaire qui minimise la somme des carrés des différences entre les cibles observées et les cibles prédites. Mathématiquement, il résout un problème de la forme :
$$\min_{w} || X w - y||_2^2$$

Commenceons par ajuster un modèle de régression linéaire en utilisant les OLS.

```python
from sklearn import linear_model

reg = linear_model.LinearRegression()
X = [[0, 0], [1, 1], [2, 2]]
y = [0, 1, 2]
reg.fit(X, y)

print(reg.coef_)
```

- Nous importons le module `linear_model` de scikit-learn.
- Nous créons une instance de `LinearRegression`.
- Nous utilisons la méthode `fit` pour ajuster le modèle aux données d'entraînement.
- Nous affichons les coefficients du modèle linéaire.
